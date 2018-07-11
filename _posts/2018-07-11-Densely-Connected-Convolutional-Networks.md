---
layout: post
comments: true
title: 논문 요약&#58; Densely Connected Convolutional Networks
key: 201807111
tags:
  - ML
  - CV
  - 논문
  - CVPR
---

> CVPR 2017

별 내용없는 cvpr 2017 best paper

<!--more-->

[논문 링크](https://arxiv.org/pdf/1608.06993.pdf)

Resnet 관련된 내용은 설명 안하겠음.

## Model

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Huang-CVPR2017/1.png){:width="450px"}

기본적으로 Resnet에 skip-connection은 다다음 layer의 아웃풋에만 연결됐는데 그 폭을 넓힌 것이다.

CNN이 쭉 이어질 때, layer마다 사이즈가 달라도 된다. 다른 사이즈일 경우 skip-connection의 정보를 전달할 수 없으므로 블록 단위로 나누고 한 블록에서 사이즈를 맞춰준다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Huang-CVPR2017/2.png){:width="450px"}

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Huang-CVPR2017/3.png){:width="450px"}

위 그래프처럼 densenet에서의 output은 앞에서도 전달받는 것이 많으므로 resnet에 비해서 parameter 갯수가 적게 필요하고 그에 따라 computational efficiency가 더 좋다.














