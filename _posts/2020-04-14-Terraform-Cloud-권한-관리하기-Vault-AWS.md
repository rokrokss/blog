---
comments: true
title: wip - Terraform Cloud 권한 관리하기 (feat. Vault, AWS)
key: 202004140
picture_frame: shadow
tags:
  - DevOps
---

TFC step-by-step 가이드는 아니다. TFC의 AWS 자격을 Vault를 이용해 관리하는 방법에 대해 정리하겠다.

<!--more-->

# Terraform Cloud

기본적으로 테라폼 리소스는 `terraform init/plan/apply` 등의 cli 커맨드로 배포를 해야하는데,
GitHub 등의 소스 팀 단위 협업을 해야하는 경우 타겟 브랜치에 코드 푸시가 됐을 때만 `terraform apply`가 되게 한다던가 PR의 변경사항이 `terraform plan`을 문제없이 통과했을때만 머지 가능하도록 설정한다던가 등의 파이프라인 설정이 필요하다.
테라폼은 앞서 말한 커맨드처럼 자체적인 Workflow가 있기 때문에 그를 위한 CI/CD 구축 방법은 여러가지가 있는데
그 중 hashicorp가 공식적으로 만들어놓은 솔루션으로 Terraform Enterprise, 혹은 hashicorp가 직접 리모트 머신을 관리해주는 Terraform Cloud(이하 TFC)가 있다.

TFC를 사용할 경우 리모트머신이 우리가 환경변수로 주입한 static credential을 이용해 AWS 등의 provider에 인증하는 절차를 걸친다. 이 포스트에서는 그에 대해 다뤄보겠다.
기본적인 TFC 구축(Workspace 생성, Git저장소 VCS 연동, Notification 등)에 대한 정보가 필요하다면
[공식 Document](https://www.terraform.io/docs/cloud/getting-started/index.html)도 괜찮고
[이 포스트](https://medium.com/swlh/an-intro-to-terraform-cloud-github-and-aws-for-ci-cd-7cee09790005)처럼 참고할만한 자료가 많다.




