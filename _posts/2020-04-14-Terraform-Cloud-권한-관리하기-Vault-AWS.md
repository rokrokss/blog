---
comments: true
title: Terraform Cloud 권한 관리하기 (feat. Vault, AWS)
key: 202004140
picture_frame: shadow
tags:
  - DevOps
---

TFC step-by-step 가이드는 아니다. TFC의 AWS 자격을 Vault를 이용해 관리하는 방법에 대해 정리하겠다.

<!--more-->

# Intro

기본적으로 테라폼 리소스는 `terraform init/plan/apply` 등의 cli 커맨드로 배포를 해야하는데,
GitHub 등의 소스 팀 단위 협업을 해야하는 경우 타겟 브랜치에 코드 푸시가 됐을 때만 `terraform apply`가 되게 한다던가 PR의 변경사항이 `terraform plan`을 문제없이 통과했을때만 머지 가능하도록 설정한다던가 등의 파이프라인 설정이 필요하다.
테라폼은 앞서 말한 커맨드처럼 자체적인 Workflow가 있기 때문에 그를 위한 CI/CD 구축 방법은 여러가지가 있는데
그 중 hashicorp가 공식적으로 만들어놓은 솔루션으로 Terraform Enterprise, 혹은 hashicorp가 직접 리모트 머신을 관리해주는 Terraform Cloud(이하 TFC)가 있다.

TFC를 사용할 경우 리모트머신이 하드코딩된 static credential 혹은 환경변수로 주입된 credential을 이용해 AWS 등의 provider에 인증하는 절차를 걸친다. 이 포스트에서는 그에 대해 다뤄보겠다.
기본적인 TFC 구축(Workspace 생성, Git저장소 VCS 연동, Notification 등)에 대한 정보가 필요하다면
[공식 Document](https://www.terraform.io/docs/cloud/getting-started/index.html)도 괜찮고
[이 포스트](https://medium.com/swlh/an-intro-to-terraform-cloud-github-and-aws-for-ci-cd-7cee09790005)처럼 참고할만한 자료가 많다.

이 포스트에서는 기본적인 TFC 환경 인터페이스에 대한 지식이 있는 것을 가정하고 설명하겠다.

# Vault

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/tfc/0.png)

AWS credential을 코드에 직접 넣어서 인증하게 만드는 것은 당연히 피해야한다.
그렇다면 환경변수로 AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY를 주입해서 사용해야할까, 이 부분에서 Vault를 이용하면 이를 피할 수 있다.
또한 Vault는 aws user, assumerole, ssh access control 뿐 아니라 기본적인 secret store로 사용할 수 있고, 쿠버네티스 환경에서 접근성이 좋고(serviceaccount token 활용) audit도 제공하는 만큼  access control, secret store 관련 기능을 모두 Vault를 이용하여 중앙관리하면 취할 수 있는 이득이 많다.
그런 의미에서 Vault를 이용하여 AWS Provider 인증을 거치도록 구성하겠다.

## Background

이왕 정리하는 김에 평소에 긴가민가했던 부분을 좀 적으려합니다. 도움이 되는 내용이 아닐 수도 있으니 필요 없다면 내려서 구현 내용을 확인바랍니다(어감이 너무 세서 존댓말 혼용...)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/tfc/1.png)

공식페이지에서 Architecture overview 느낌으로 보여주는 그래프인데 여기 나오는 키워드 그대로 설명하진 않는다. 설명하기에는 복잡한데 굳이 자세한 아키텍쳐를 첨부한 느낌이다. 공식 설명은 이보다 좀 더 개념적으로 이루어져 있다.

### 주요 개념

- Storage Backend
  - Vault는 암호화된 데이터를 저장하기 위해 별도 Storage를 필요로 하는데, S3, MySQL, DynamoDB, Consul 등이 있다.
  - 그 중 Consul, Zookeeper, etcd, DynamoDB 등은 High Availability를 가지고 그 중 Consul이 hashicorp 물건이라 공식 가이드도 자세하고 레퍼런스도 많아서 Vault + Consul 구조로 많이들 구축한다.
  - 그런데 최근 [v1.4.0](https://www.hashicorp.com/blog/vault-1-4/)에서 Integrated Storage 기능이 Vault에 추가되었다. 외부 Storage를 쓰지 않고서도 Vault만 이용해서 HA mode 구성이 가능해졌다. 어느 정도 시간이 지난 후에 적용할지 결정하면 좋을 듯.
- Secrets Engine
  - 말그대로 Secret을 다루는 컴포넌트다. `kv` secrets engine은 간단한 key-value storage를 관리하고, 나아가 임시 자격증명키를 발급할 수 있는 AWS secrets engine도 있다.
- Auth Method
  - secret 혹은 system configuration, status, policy 등의 리소스에 접근/조작을 하기 위해서는 인증 과정이 필요하며 그 Authentication을 하는 방법을 말한다. 굉장히 다양한 방법이 있다. Vault Token을 이용할 수도 있고, LDAP, Kubernetes(serviceaccount token) 등을 지원한다. 그리고 정해진 방식의 인증을 통과할 경우 해당 유저/어플리케이션이 취할 수 있는 권한은 policy와 role로 관리하게 된다.
- Barrier
  - 공식 설명에서는 Vault server를 둘러싼 벽으로 표현을 하는데, Storage Backend와의 트래픽을 포함해서 Vault server를 오고가는 모든 data는 암호화됨을 나타낸다. Storage와의 통신에는 AES256 암호화가 사용되며 클라이언트와의 통신의 경우 Master key를 이용해 unsealed 상태로 전환된 Vault server는 인증 절차를 걸친 클라이언트에게 데이터를 전달한다. 클라이언트는 매번 client token을 헤더에 포함해야하며 TLS가 사용된다.

### Security

Vault의 핵심인 Security Model.

- External Threat 방지
  - Barrier 항목에서 설명한 것과 같다.
  - Storage와의 연결에 TLS도 추가로 사용할 수 있다.
- Internal Threat 방지
  - Internal Threat은 attacker가 어느 정도 레벨의 접근 권한을 획득하였을 경우의 보안사항을 말한다.
  - authorized 되지 않은 secret은 ACL policy로 보호된다. 특정 Auth method를 추가할 경우 해당 method로 접근하는 클라이언트가 가지는 권한을 항상 policy로 제한하므로 이것이 가능하다.
  - **Key Rotation**

### Key Rotation

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/tfc/2.png)

Vault server는 *sealed* 상태로 실행된다. [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir's_Secret_Sharing) 알고리즘을 사용하여 n개의 unseal key를 생성하며 k개의 key를 제공해야만 내부적으로 master key를 얻어 unsealed 상태로 전환할 수 있다. 그리고 이 master key는 backend와의 traffic을 암호화하는 encryption key를 암호화한다. 이를 통해 unseal key를 분산시켜 관리하면 특정 key가 노출되어도 unseal을 할 수 없다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/tfc/3.png)

- Shamir's Secret Sharing
  - 간단하게 설명하자면 k-1차 함수 f(x)가 있을때 f(x)가 어떤 함수인지 알아내기 위해서는 k개의 점이 필요하며, k개의 점이 있다면 f(0)를 구할 수 있는 원리를 이용한 것이다. k보다 큰 n개의 좌표는 unseal key, f(0)는 master key에 대응된다.

### Plugin System

모든 auth, secret backend는 plugin인이며, 이 plugin은 각자 다른 경로에 위치하여 각자 다른 process로 실행된다. Vault와 mutual TLS가 적용된 RPC를 이용해 통신한다.
이를 통해 plugin crash가 Vault 전체 장애로 이어지지 않도록 한다.

## Deploy Vault

1.4 전까지만 해도 vault document랑 consul document랑 왔다갔다하면서 참고해서 구축해야했다.
개인적으로 vault와 consul의 helm chart를 이용해서 kubernetes 위에 구축하면 기존 방식을 이용할 때 bastion host나 vpn 연결하고 EC2 인스턴스 접근해가면서 해야하는 일을 훨씬 편하게 할 수 있어서 kubernetes에 구축하는게 괜찮다고 생각했다.

근데 1.4 버전 나오고 Intergrated Storage 추가되면서 Consul이 필요가 없으니까 구축 가이드가 꽤 친절해졌다.
[요런 문서](https://learn.hashicorp.com/vault/new-release/raft-storage-aws) 보면서 따라하면 금방 만들 수 있을 것이다.

# Terraform Cloud

```
// vault provider는 write-only 값으로 주입된 환경변수 VAULT_TOKEN을 이용한다.
provider "vault" {
  address = "~"
}

terraform {
  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "~"

    workspaces {
      name = "~"
    }
  }
}

data "vault_aws_access_credentials" "tfc" {
  backend = "aws"
  role    = "tfc"
  type    = "sts"
}

provider "aws" {
  region     = "~"
  access_key = data.vault_aws_access_credentials.tfc.access_key
  secret_key = data.vault_aws_access_credentials.tfc.secret_key
  token      = data.vault_aws_access_credentials.tfc.security_token
}
```

먼저 AWS를 사용한다고 가정한다.
결론부터 보자면 위와 같은 코드를 통해 TFC 리모트머신에서 aws provider 인증을 통과할 수 있다.

terraform을 이용해 vault resource를 구현해봤다면 알겠지만 위 코드가 제대로 적용되기 위해서 해야하는 기반 작업이 몇 가지있다.

- `aws/tfc` secret backend, 그리고 iam 임시키를 생성할 수 있고 생성하려하는 aws resource에 대한 policy에 대해 AussumeRole이 가능한 iam role을 가진 iam user(iam 권한 설정에 AssumeRole이 섞이면 항상 한눈에 이해하기 어려워진다...)
- 입력된 VAULT_TOKEN은 `aws/sts/tfc`의 read 권한을 가져야한다.
- root token을 사용하지 않을 것이므로 TFC api를 통해 VAULT_TOKEN을 변경하는 cron을 만들거나, VAULT_TOKEN 자체를 [periodic token](https://www.vaultproject.io/docs/concepts/tokens.html#periodic-tokens)으로 만들어서 수명 연장 cron을 만든다.

**아래 설명할 코드는 위 코드와 달리 TFC가 아닌 로컬에서 apply해야한다. aws provider, vault provider는 로컬 credential을 입력하자**

## IAM

```
// aws/config/root에 입력될 user
resource "aws_iam_user" "tfc" {
  name     = "terraform-cloud"
}

resource "aws_iam_user_policy" "tfc" {
  name     = "terraform-cloud-policy"
  user     = aws_iam_user.tfc.name
  policy   = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sts:AssumeRole"
      ],
      "Resource": [
        "arn:aws:iam::ACCOUNTID:role/TerraformCloud"
      ]
    }
  ]
}
EOF
}

resource "aws_iam_access_key" "tfc" {
  user     = aws_iam_user.tfc.name
}

// 실제로 TFC가 발급 받아서 사용하는 role
resource "aws_iam_role" "tfc" {
  name     = "TerraformCloud"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNTID:user/terraform-cloud"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

// TFC가 사용하게될 policy, 꼭 AdministratorAccess일 필요는 없다.
resource "aws_iam_role_policy_attachment" "tfc" {
  role       = aws_iam_role.tfc.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}
```

## Secret Backend

```
resource "vault_aws_secret_backend" "tfc" {
  path                      = "aws"
  access_key                = aws_iam_access_key.tfc.id
  secret_key                = aws_iam_access_key.tfc.secret
  default_lease_ttl_seconds = 3600
  max_lease_ttl_seconds     = 36000
}

resource "vault_aws_secret_backend_role" "tfc" {
  backend         = vault_aws_secret_backend.tfc.path
  name            = "tfc"
  credential_type = "assumed_role"
  role_arns       = [aws_iam_role.tfc.arn]
}
```

### for EKS

- 위 `vault_aws_secret_backend_role.tfc`는 사실 `credential_type = iam_user`로 설정하여도 TFC 상에서 aws 리소스를 생성할 수 있는데, eks를 이용할 경우 생기는 문제가 있다.
- eks를 다뤄봤다면 알다시피 eks는 `aws-auth` Configmap을 사용해서 iam 권한과 k8s 권한을 연동해주고, 클러스터를 생성한 user는 eks 내부적으로 admin 권한을 부여해준다. 이 때문에 별도의 작업없이도 자신이 생성한 eks에서는 제한없이 모든 api 요쳥이 가능하다.
- 헌데, TFC와 Vault를 엮어서 사용한다면 eks 생성에 사용되는 user, 혹은 role은 사용자가 아닌 Vault가 생성한 임시자격이 된다. 매번 다른 credential이 `terraform plan/apply`에 사용되는 것이다.
- eks 생성 terraform 코드를 스크래치부터 짜려면 코드 양이 많아지기 때문에 [이 모듈](https://github.com/terraform-aws-modules/terraform-aws-eks)을 사용하는 경우가 많을텐데(아마도?) 이 경우 kubernetes provider 인증이 모듈에 포함되어 있기 때문에 `aws-auth`에 vault 임시자격 정보가 들어가있지않다면 "initial apply" 이후 `terraform plan/apply`가 불가능해진다.
- 이를 위해서는 `iam_user`를 이용하든 `assumed_role`을 이용하든 해당 정보를 `aws-auth`에 넣어야하는데 `iam_user`의 이름이 매번 바뀌기 때문에 `assumed_role`을 사용한다.

```
module "eks" {
  source = "terraform-aws-modules/eks/aws"
...
  map_roles = [
    {
      rolearn  = "arn:aws:iam::ACCOUNTID:role/TerraformCloud"
      username = "tfc-remote"
      groups   = ["system:masters"]
    }
  ]
}
```

## VAULT_TOKEN

```
resource "vault_policy" "tfc" {
  name = "terraform-cloud"

  policy = <<EOT
path "aws/sts/tfc" {
  capabilities = ["read", "list", "create", "update"]
}

path "auth/token/renew" {
  capabilities = ["update"]
}

path "auth/token/create" {
  capabilities = ["read", "list", "create", "update"]
}

path "auth/token/lookup-sef" {
  capabilities = ["read"]
}

path "auth/token/lookup-accessor" {
  capabilities = ["update"]
}

path "auth/token/revoke-accessor" {
  capabilities = ["update"]
}
EOT
}

resource "vault_token_auth_backend_role" "tfc" {
  role_name           = "terraform-cloud"
  allowed_policies    = [vault_policy.tfc.name]
  period              = "2592000"
}

// resource "vault_token" "tfc_vault_token" {
//   role_name = vault_token_auth_backend_role.tfc.role_name
// }

// output "tfc_vault_token" {
//   value = vault_token.tfc_vault_token.client_token
// }
```

위 코드는 TFC에 주입할 VAULT_TOKEN을 생성하는 코드다. 다만, `vault_token`을 생성하는 부분을 주석처리했는데,
[이 이슈](https://github.com/terraform-providers/terraform-provider-vault/issues/722) 때문이다.
간단히 설명하자면 vault provider는 입력된 토큰을 그대로 사용하지 않고 해당 토큰으로 TTL이 20분인 child token을 만들어서 리소스 생성에 사용한다.
그렇다보니 `vault_token`이 입력된 토큰의 손자 토큰이 되고 20분이 지나면 `tfc_vault_token`은 자신의 TTL과 상관없이 revoke된다.

periodic token을 만들어서 무기한으로 사용하려면 terraform을 이용해선 아직 해답이 없다.

`$ vault token create -role=terraform-cloud`

이 부분은 terraform을 사용하지 않고 위 커맨드를 통해 토큰을 만들 수 있다.

# 결론

이렇게 하면 Terraform Cloud 위에서 Vault를 이용해 AWS 권한을 얻을 수 있다.
본 포스트는 Terraform Enterprise 사용을 고려하지 않았다. Terraform Enterprise를 사용할 경우 ec2 metadata를 통해 인증할 수도 있을 것 같은데 많이 알아보진 않았다.

TFC 대용으로 [Atlassian을 이용하는 방법](https://www.hashicorp.com/integrations/atlassian/terraform/)도 있고,
굳이 TFC를 사용하지 않고 요즘 핫한 [GitHub Action을 이용하는 방법](https://medium.com/swlh/lets-do-devops-github-actions-terraform-aws-77ef6078e4f2)도 있다.

그리고 포스트에서는 vault provider 인증을 위한 auth method로 token을 사용했지만 이 부분은 LDAP, GitHub access token 등등 굉장히 많은 대안이 있다. vault token은 수명이 한정되어있어 자세히 설명하진 않았지만 periodic token을 만들고 별도 cronjob이 해당 토큰의 수명을 주기적으로 갱신하게 만들었는데 auth method로써 token 사용은 추가적인 관리를 필요로 하므로 다른 대안을 이용하면 관리비용을 줄일 수도 있을 것이다.

