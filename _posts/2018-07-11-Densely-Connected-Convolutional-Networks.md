---
comments: true
title: "논문 요약: Densely Connected Convolutional Networks"
image: "/assets/images/paper-summary/Huang-CVPR2017/1.png"
description: "DenseNet의 핵심 구조를 간단히 정리합니다. 이전 레이어의 특징을 연결하는 dense block과 네트워크 구성, ResNet과의 파라미터·연산 효율 비교를 살펴봅니다."
key: 201807111
tags:
  - AI
  - CV
  - 논문
  - CVPR
image_alt: "이전 레이어의 특징 맵을 모두 연결하는 DenseNet dense block"
---

> CVPR 2017

별 내용없는 cvpr 2017 best paper

<!--more-->

[논문 링크](https://arxiv.org/pdf/1608.06993.pdf)

Resnet 관련된 내용은 설명 안하겠음.

## Model

![이전 레이어의 특징 맵을 모두 연결하는 DenseNet dense block](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Huang-CVPR2017/1.png){:width="500px"}


기본적으로 Resnet에 skip-connection은 다다음 layer의 아웃풋에만 연결됐는데 그 폭을 넓힌 것이다.


![Dense block과 전이층을 연결한 DenseNet 전체 구조](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Huang-CVPR2017/2.png){:width="800px"}


CNN이 쭉 이어질 때, layer마다 사이즈가 달라도 된다. 다른 사이즈일 경우 skip-connection의 정보를 전달할 수 없으므로 블록 단위로 나누고 한 블록에서 사이즈를 맞춰준다.


![Residual block과 dense block의 파라미터·연산량 비교](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Huang-CVPR2017/3.png){:width="800px"}


위 그래프처럼 densenet에서의 output은 앞에서도 전달받는 것이 많으므로 resnet에 비해서 parameter 갯수가 적게 필요하고 그에 따라 computational efficiency가 더 좋다.














