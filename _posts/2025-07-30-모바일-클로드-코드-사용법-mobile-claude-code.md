---
comments: true
title: 모바일로 Claude Code 사용하는 법
key: 202507300
picture_frame: shadow
tags:
  - AI
  - 생산성
---

바이브코더가 되는 방법...

<!--more-->

![vibetunnel](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/vibetunnel/0.png)

간단하게 말하면 컴퓨터의 터미널을 웹으로 컨트롤 할 수 있도록 로컬에 띄우고, cloudflared를 통해 외부 접근을 열어서 폰으로 접근하는 방식입니다.

## 설치

[vibetunnel](https://vibetunnel.sh/)이라는 툴을 설치합니다.

vibetunnel 실행하면 설명에 따라 어떤 터미널 앱을 사용할 지 고르라고 나옵니다. 저는 기본 터미널앱만 사용 가능으로 떠서 그걸 썼습니다.

## 설정

vibetunnel 설정창의 Remote 탭을 보면 cloudflared를 설치하고 자동으로 연동시켜주는 버튼이 있습니다. 연동하면 Public URL이 생성됩니다.

vibetunnel 앱에서 세션을 생성하고, 해당 URL을 모바일로 접근하여 컴퓨터 비밀번호를 입력하면 이제 터미널을 모바일로 제어할 수 있습니다.

## 사용

혼밥하면서 클로드코드에게 코딩을 시키는 바이브코더가 됩니다.
