---
layout: post
comments: true
title: 논문 요약&#58; Convolutional Neural Networks for Sentence Classification
key: 201806161
tags:
  - ML
  - NLP
  - 논문
  - EMNLP
---

> EMNLP 2014

Sentence Classification을 위한 CNN 모델

<!--more-->

이번 학기에 NLP 프로젝트들이랑 과제만 하다보니 이 모델을 두번이나 쓰게 되었다.
모델 외에 덧붙일 말은 별로 없을 것 같다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/YKim-EMNLP2014/model.png)

pre-trained word vector를 token마다 적용하여 embedding을 만들고, Convolutional Layer -> Max-pooling -> Fully Connected Layer -> Softmax 구조를 가진다.

여기서 중요한 점이 두 가지 있는데,

첫째로, filter는 한 token의 정보를 쪼개서 가져가면 안되므로 filter의 row size는 word vector의 dimension과 동일하게 유지한다.

둘째로, 초기의 word vector가 train이 되어 변하는 경우는 non-static, 변하지 않는 경우는 static, pre-trained word vector가 아닌 random initialization을 가질 수 있는 variation들이 있다.

- CNN-rand : n x k의 word embedding matrix를 random한 range(-a,a)에서 초기화 및 학습.
- CNN-static : n x k의 word embedding matrix를 word2vec로부터 초기화 및 해당 weight에 대해서 학습.
- CNN-non-static : n x k의 word embedding matrix를 word2vec로부터 초기화 및 해당 weight에 대해서 학습.
- CNN-multichannel : 2개의 static, non-static n x k word embedding matrix를 사용하며, 두가지 결과를 합쳐서 학. 

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/YKim-EMNLP2014/result.png)

각 방식별 결과와 다른 approach들과의 비교.















