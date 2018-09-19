---
comments: true
title: 논문 요약&#58; Word Embedding and WordNet Based Metaphor Identification and Interpretation
key: 201808011
picture_frame: shadow
tags:
  - ML
  - NLP
  - 논문
  - ACL
---

> ACL 2018

WordNet을 사용하는 unsupervised metaphor detection과 더불어 metaphor phrase의 literal fit을 추측, 교체하여 NMT task에서 성능 향상을 만들었다.

<!--more-->

[논문 링크](http://aclweb.org/anthology/P18-1113)

## Introduction

Metaphor Detection task를 수행하는 연구는 많이 되어있다. 이제 Metphorical Sense를 detection이 아닌 다른 task에서 응용해야 하는 시기라고 생각한다.
헌데 그 일을 해내는 것이 아직 어려운 지 metaphor interpretation 연구는 된 게 거의 없다.
이 논문에서는 metaphorical sense를 NMT에서 활용하여 해결하였는데, 그 핵심으로 WordNet, Word2Vec, cosine-similarity가 쓰였다.

## WordNet

대충 뭔지 알 것 같아서 자세하게는 찾아보지 않았다.
실제 사전이 그러한 것처럼 단어를 넣으면 상위어(hypernym), 동의어(synonym) 등을 얻을 수 있는 프로그램이다.

## Hypothesis

1. metaphorical word는 구별될 수 있다. metaphorical word의 literal sense와 context의 domain이 차이가 있기 때문이다. (ex. "하늘이 향기롭다" 에서의 '하늘'과 '향기롭다'는 보통 함께 등장하는 단어들이 아니다.)
2. word가 literal sense에 준하며 등장하는 횟수가 metaphoric sense에 의한 것보다 크다.

## Model

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Mao-ACL2018/1.png){:width="400px"}

<br>

1. 먼저 Wikipedia dump로 Word2Vec을 학습시킨다. (본 논문에서는 CBOW, Skip-gram 방식 각각 실험했다.)
2. input sentence를 가지고 각 word를 target word로 설정, 주변을 context로 설정한다. target word를 WordNet에 넣어서 hypernym과 synonym들을 구하여 candidate word set W를 만든다.
3. context vector는 context word들을 평균내어 구하고, word set W 중에서 context vector와 가장 similar한 word를 best fit word로 정한다.
4. best fit word와 기존 target word의 similarity를 구하여, 특정 역치 이상이면 literal, 아니면 metaphorical word로 정한다.
5. 위 4번 과정까지가 metaphor detection인데, 이후 metaphorical word들을 best fit word로 교체하여 NMT task에 이용한다.

## 소감

WordNet을 이용하는 과정이 특별하다.
아직까지 deep하게 논의되어야 할 점이 굉장히 많지만 Machine Learning Approach들이 원체 인간 본연의 process를 재구현하는 것이었는데, NLP task에 대해 인간은 본래 사전을 아주 많이 사용하는데도 WordNet을 활용하는 시도가 현재는 그리 많지 않다.








































