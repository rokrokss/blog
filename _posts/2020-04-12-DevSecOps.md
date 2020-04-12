---
comments: true
title: DevSecOps
key: 202004120
picture_frame: shadow
tags:
  - DevOps
---

두서 없는 글

<!--more-->

# DevSecOps

나는 평소에 [IBM Cloud의 유튜브 채널](https://www.youtube.com/user/IBMCloud)을 자주 본다.

특히 투명 칠판두고 올라오는 8분 내외의 영상들은 개념 요약이지만 설명도 잘하고 중요한 포인트만 전달해주기 때문에 꼭 챙겨보고 있다. 그 중 **"What is DevSecOps?"** 영상을 보고 들었던 생각이 좀 있어서 한번 풀어내보고자 한다.

## What is DevSecOps? 

<iframe
src="https://www.youtube.com/embed/J73MELGF6u0"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe>

- DevSecOps = DevOps + Security
- keyword는 **Observability, Traceability, Confidence, Compliance**
- 기본적으로 모든 개념을 `code -> build -> deploy -> manage -> learn` pipeline 내에서 설명했다. 
- Observability는 application delivery process가 얼마나 observable한 지에 대해 말하고, 나머지 Traceability, Confidence도 거의 같은 맥락, 그리고 Compliance는 위 pipeline 내에 구축되어야 함을 설명한다.
- 다만 CI/CD 형태의 pipeline을 밑그림으로 전부 다 설명하니 찝찝한 감이 있다.

<iframe
src="https://www.youtube.com/embed/6l0RYbXd86k"
frameborder="0"
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
allowfullscreen
></iframe>

- 짧은 영상 하나를 더 보니 어느 정도는 이해를 했다. DevOps가 operational work을 하나의 개발 프로세스로 끌어왔듯이 security work또한 DevOps 개발 프로세스로 끌어오는 개념으로 보인다.
- 인상 깊은 발언이 있는데, Security 관련 사항이 별도 프로세스로 진행되면 개발자간의 소통은 "Why aren't you listening to me?" 태도가 되고, DevOpsSec 개념을 차용하여 Security 관련 개발을 전체 프로세스의 처음부터 같이 유연하게 엮어야 "How can we work together?"가 된다고 한다. 몇 개의 글에서 슬로건처럼 봤었던 Security by everyone이 이런 의미였나보다.

## DevOps vs DevSecOps

- 찾아본 바에 의하면 크게 다르지 않다. 결국 DevOps 개발 프로세스에 Security work를 결합한 것이다. 물론 기존 DevOps에도 Security는 항상 있었다. AWS는 "DevOps 팀 전체가 보안을 중점으로 두는 경우 때때로 DevSecOps라고 불립니다." 정도로도 설명한다.

## Security as Code?

- 이 개념에 대해 찾다보면 가장 궁금한 것은, Security가 DevOps의 infra 코드와 유사한 선언형 구조로 결합되어  존재할 수 있는지였다. 어느 정도는 가능하겠지만, 레거시(혹은 앞으로 레거시가 될) Security 개발이 *전부* DevOps manner로 이관될 수 있는지.
- CI/CD 파이프라인에서의 Security는 분명 위와 같은 방식으로 가능할 것이다. GitOps와 Security의 integration은 대충 검색해도 굉장히 많은 자료가 나온다.
  - (특히 weave.works가 많다, 그 외로도 fluxcd는 등한시했지만 [helm-operator](https://github.com/fluxcd/helm-operator), [servicemeshinterface](https://github.com/servicemeshinterface/smi-spec)처럼 저쪽 사람들한테서 매력있는 오픈소스가 많이 나와서 시간나면 한번 쭉 리뷰할 예정...)

- 그렇다면 배포된 서비스가 있는 쿠버네티스 클러스터에서의 네트워크 측면의 보안은 어떻게 처리할까? 
  - 개발비용을 문제로 외면받고 있는 end-to-end tls
  - ddos 방지 등 특정 시스템의 proxy 구현
  - 서비스 간의 접근 권한 설계
  - CI/CD로만 설명하기엔 더 많은 것들이 있다.

그래서...

## Service Mesh!?

![text](https://d33wubrfki0l68.cloudfront.net/1369cff9a50c46b58834dbfc302a6cda35548adf/e8abc/images/blog/2018-06-05-11-ways-not-to-get-hacked/service-mesh-@sebiwicb.png)

(블로그에는 언급한 적이 없지만 여기저기서 서비스메쉬 언급을 굉장히 많이 하고 다닌다...)

결국 이 부분에서도 Service Mesh가 중요한 역할, 혹은 트리거가 될 것 같단 기대가 있다.
[Istio의 security documentation](https://istio.io/docs/concepts/security/)만 보아도 mTLS, zero-trusted network, authorization policies 등 MSA의 보안 이슈를 막아줄 기능을 제공한다.
그리고 결국 핵심은 envoy를 통한 full observability라고 생각한다.

다만, 과연 sidecar가 network 측면의 정보만 가진 구조로 궁극적인 시스템을 구현하는지에 대해서는 아직 의문이 든다.
network feature 뿐 아니라 application capability까지 제공하는 구조가 얼마나 효과적일지, 개인적으로 [Dapr](https://github.com/dapr/dapr)의 stable 버전이 나오는 시점에 어떤 변화가 있을지 궁금하다.

## 결론

![text](https://www.viva64.com/media/docx/blog/0710_DevOps_vs_DevSecOps/image1_thm_intoblank_1200x630.png)

DevOps와 크게 다른 점은 없다. 기존의 DevOps 프로세스를 Secure하게 전달하자!

Fast, Secure, Agile!

