---
comments: true
title: Django 노트&#58; ngrok을 이용하여 배포 전 모바일로 접속하기
key: 201902230
picture_frame: shadow
tags:
  - Django
---

ngrok을 이용하여 간단하게 모바일로 접속하자

<!--more-->

[ngrok 다운로드 링크](https://ngrok.com/download)

먼저 ngrok을 다운로드합니다.

압축을 풀고, ngrok 실행파일을 manage.py 파일이 있는 폴더로 옮깁니다.

해당 경로에서 서버 가동 후 ngrok을 아래 명령어로 실행합니다.

    python3 manage.py runserver 8000
    ./ngrok http 8000

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/django/ngrok/0.png){:width="500px"}

ngrok.io로 끝나는 주소가 보입니다.

그 주소를 통해 접속을 하면 되는데, 먼저 settings.py의 ALLOWED_HOSTS에 해당 주소를 추가합니다.

    ALLOWED_HOSTS = ['~~~~.ngrok.io']
