---
comments: true
title: "NbViewer를 통해 Jupyter Notebook 공유하기"
image: "/assets/images/nbviewer/3.png"
description: "Jupyter Notebook을 nbviewer로 공유하는 방법을 정리합니다. GitHub Gist에 노트북을 올리고 공개 URL을 nbviewer에 입력해 읽기 좋은 결과를 만드는 과정입니다."
key: 201901140
picture_frame: shadow
tags:
  - etc
image_alt: "노트북 URL을 입력하는 nbviewer 홈페이지"
---

Jupyter Notebook 작업물 이쁘게 보여주기

<!--more-->

항상 느끼는 것인데, Jupyter Notebook이 기능적으로 편리하지만 그 색과 구조 자체도 이쁘다.

<br>

&nbsp;&nbsp;&nbsp;&nbsp; ![Jupyter nbviewer 로고](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/nbviewer/0.png){:width="400px"}

<br>

그래서 그 ipynb 파일을 그대로 결과물로 보여주고 싶은데, Google Colab으로 등록하거나, GitHub에 파일을 올려도 내가 로컬에서 보는 것만큼 정갈하지가 않더라.
그럴 때 **NbViewer**를 사용하면 된다.

<br>

절차는 다음과 같다.

<br>

- https://gist.github.com/ 에 접속한다. (Filename에는 원하는 파일 이름.ipynb, 내용은 ipynb 파일의 raw source를 복붙해야 한다.)

<br>

&nbsp;&nbsp; ![Jupyter Notebook 파일을 입력하는 GitHub Gist 생성 화면](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/nbviewer/1.png){:width="700px"}

<br>

- ipynb 파일을 텍스트 편집기로 열어 raw source를 복사하던가, GitHub에 올려놓았다면 해당 파일 페이지 상단의 Raw 버튼을 눌러 source를 복사하고, 빈칸에 넣는다.

<br>

&nbsp;&nbsp; ![Gist에 업로드한 노트북의 Raw 링크 위치](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/nbviewer/2.png){:width="700px"}

<br>

- create gist를 누르고 나오는 페이지의 주소가 https://gist.github.com/깃헙아이디/asdfnj32412hiofehwqiof 요런 식으로 맨 뒤에 asdfnj32412hiofehwqiof 처럼 긴 코드가 붙는다. 이걸 복사한다.

<br>

- http://nbviewer.jupyter.org/ 에 접속해 아래 빈칸에 코드를 붙여넣고 Go!를 누른다.

<br>

&nbsp;&nbsp; ![노트북 URL을 입력하는 nbviewer 홈페이지](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/nbviewer/3.png){:width="700px"}

<br>

이제 우리의 Jupyter Notebook 파일이 이쁘게 웹으로 올라간다. 보여주고 싶은 상대방에게 링크만 보내주면 된다.

URL 단축을 위해 Bitly URL Shortener(https://bitly.com/)를 사용하는 것도 좋다.
