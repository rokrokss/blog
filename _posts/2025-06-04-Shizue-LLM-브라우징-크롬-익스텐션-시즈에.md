---
comments: true
title: LLM 크롬 익스텐션 "시즈에" 만들기
key: 202506040
picture_frame: shadow
tags:
  - AI
  - LLM
  - Prototyping
---

*크롬 웹스토어에 게시됐습니다.*

<!--more-->

[링크](https://chromewebstore.google.com/detail/%EC%8B%9C%EC%A6%88%EC%97%90/mpcbgfkoholfgapcgcmfjobnfcbnfanm)

## 서론

&nbsp;&nbsp;LLM 기반으로 브라우징 UX를 개선하는 익스텐션은 이미 시장에 여럿 나와 있다. 대충 훑어본 결과, 이름만 다를 뿐 비슷한 기능 구성을 갖추고 있었다. 주된 유입 요인은 ChatGPT보다 낮은 가격, 탭 전환 없이 사용하는 사이드패널 UI, 콘텐츠 요약 기능 정도다. 부가기능들이 많긴 한데, 대부분 사용자의 시간을 절약해 주는 기능은 아니었다. 주요 익스텐션은 사용자 본인의 API 키를 이용해서 구독 없이도 기본적인 기능을 제공하는데, 페이지 요약과 대조 번역 같은 기능은 유료 플랜으로 묶어 두었다. 구조를 상상했을 때 개발 환경을 잘 잡아두면 금방 구현 가능한 것들이라고 생각했다. 그렇게 직접 개발을 하다 보면 사용자 활동 시퀀스 데이터를 활용해 뾰족한 기능도 만들 수 있을 것이라 생각하지만(결론부터 말하자면) 아직 거기까지 나아가지는 못했다.

이름은 `시즈에`. 닌텐도 동물의숲에서 주인공을 돕는 비서 캐릭터 여울이의 본명을 사용했다.


## 시즈에의 기능

기능 설명은 이미지로 대신하고, 개발 과정에 대한 기록을 남긴다.

기본적으로 [WXT](https://wxt.dev/)라는 익스텐션 개발 프레임워크를 사용했다. 만들어진 프로덕트에서 실행되는 코드는

1. 모든 페이지에 삽입되는 오버레이 메뉴

2. 클릭이나 단축키로 열리는 사이드패널

3. 브라우저 실행 시 생성되는 백그라운드 프로세스

이렇게 크게 세 가지 컨텍스트로 관리된다. 사용자가 입력하는 API 키는 페이지에 삽입되는 오버레이 메뉴에서 읽으면 안 된다. 다른 앱들과 같은 DOM에서 상태가 조회되면 메시지가 탈취될 가능성이 있다. 또, 오버레이 메뉴와 사이드패널은 해당 웹 조작에 따라 언제든 중단될 수 있도록 비동기 LLM API 호출과 공통 상태 관리는 백그라운드에 위치한다. 그렇다 보니 흡사 `클라이언트 <-> 서버` 구조처럼 코드베이스를 구성했다.

### 사이드패널의 채팅

![채팅](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/chat.gif)

웹 익스텐션은 익스텐션 전용의 key-value 로컬스토리지를 사용할 수 있고, 추가로 indexDB라는 인덱싱과 ACID 트랜잭션이 지원되는 데이터 스토리지가 있다. 설정용 상태 관리에는 로컬스토리지를 사용하고, 채팅 스레드와 메시지에는 indexDB를 사용했다.

에이전트의 대답은 `LLM API -> 백그라운드 프로세스 -> 사이드패널`까지 스트리밍 형식으로 출력하도록 구성했다.

### 원 클릭 페이지 요약

![요약](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/summarize.gif)

대화 스레드와 메시지가 저장되는 indexDB는 오버레이 메뉴에서 접근할 수 없다. 사이드패널이 열릴 때 행할 액션 타입과 페이지 데이터를 로컬스토리지에 저장하여, 열릴 때마다 초기화되는 사이드패널이 페이지 요약을 트리거할 수 있도록 했다. 이미 채팅 중인 상황이라면 현재 스레드에서 요약이 실행되도록 이벤트 트리거를 구성했다.

### 대조번역

![대조번역](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/translate.gif)

커스텀 웹 컴포넌트와 스크롤 리스너, 현재 스크린 내의 번역 대상 컴포넌트를 감지하는 DOM 순회 알고리즘을 통한 초안을 전 직장 동료인 [@gompu123](https://github.com/gompu123)님께서 구현해주셨다. 근황 얘기할 겸 만들고 있던 걸 공유드렸더니, 본인도 월 1.5만 원 내고 크롬 익스텐션을 쓰고 있었다고, 직접 만들어 보겠다고 해주셨다.

이후 나는 배치 처리와 컴포넌트 큐, 번역 캐시를 적용해 성능과 안정성을 높였다.

### 실시간 AI 자막

![유튜브자막](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/youtube.gif)

유튜브 영상에 기존 자막이 존재할 때, 원하는 언어로 LLM 번역 자막을 실시간으로 생성하여 보여준다. 사용자가 느끼는 레이턴시을 줄이기 위해 자막을 청크 단위로 나누고, 영상의 어느 부분으로 이동하든 그 시점부터 우선적으로 번역되도록 구성했다. 또한 자막을 여러 줄로 출력할 수 있도록 레이아웃 설정 기능을 추가했다.

### PDF 파일 번역

![PDF번역](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/pdf.gif)

아래는 번역 결과물이다.

![PDF번역결과](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/pdf_result.png)

[BabelDOC](https://github.com/funstory-ai/BabelDOC)이라는 라이브러리를 사용하면 PDF 파일을 기존 구조를 보존하면서 번역한 새로운 파일을 만들 수 있다. 처음에는 서버 없이 구현하고 싶었지만, 자바스크립트 진영에는 이만큼 해주는 오픈소스가 없었다. WASM을 이용해 파이썬을 실행하는 것도 CPython 디펜던시 때문에 한계가 있었다. 결국 서버를 띄워서 해결했는데, OCR 등으로 기본적으로 요구하는 리소스가 꽤 커서 아키텍처를 분리했다. 큐잉해주는 API 서버와 번역 서버를 분리하여, 번역은 GCP의 서버리스 서비스로 구현했다. 주머니 사정상 콜드스타트를 감당해야 한다. 보안상 사용자의 API 키를 요청에 실을 수 없어서 내 토큰으로 동작한다.

### 다크모드

![다크모드](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/shizue/darkmode.gif)

builder.io 블로그에서 오버레이 메뉴를 색상 반전시키는 걸 보고 같은 방식을 적극 활용했다. 추후에는 컬러 팔레트로 주요 색상 리스트를 모듈화해서 커스텀 테마를 제공하고 싶다.

참고로 시즈에에 사용된 각종 캐릭터 에셋은 5달러를 주고 구매했다.

## 추후 계획

- 게시 완료!
  - https://chromewebstore.google.com/detail/%EC%8B%9C%EC%A6%88%EC%97%90/mpcbgfkoholfgapcgcmfjobnfcbnfanm
- PDF 번역 기능까지 구현하고 보니 꽤 그럴 듯한 서비스가 되었다. 제대로 홍보해보고 싶지만, 서버 운영과 토큰 소모 비용이 발생하게 되어 상용화가 불가피해졌다.
