---
layout: post
comments: true
title: 논문 요약&#58; Using Automated Metaphor Identification to Aid in Detection and Prediction of First-Episode Schizophrenia
key: 201807051
tags:
  - ML
  - NLP
  - 논문
  - EMNLP
---

> EMNLP 2017

Metaphor Identification으로 조현병 진단하기.

<!--more-->

[논문 링크](http://aclweb.org/anthology/D17-1316)

## Introduction

token-level metaphor detection을 이용하여 조헌병을 진단한다. metaphor detection 모델은 [(Do Dinh and Gurevych, 2016)](http://www.aclweb.org/anthology/W16-1104) 요걸 사용했다.
저 모델이 이 논문이 쓰일 당시의 state-of-the-art였단다. sentiment analysis로 4가지 feature, metaphor identification으로 1가지 feature (metaphor tags) 추출해서 그 feature들로 조현병인지 아닌지 classification한다.

## Feature Set

### Metaphoricity

input은 300-dim Word2Vec skip-gram negative sampling word embedding으로 POS-tag 정보를 one-hot encoding으로 추가하고, 앞 2 token, 뒤 2 token과 함께 concatenate되어 들어간다.
이후 affine layer가 10개 있고 각 activation function은 tanh, output은 softmax로 token마다 literal인지 metaphorical인지 classify해준다.

이 모델은 VU Amsterdam Metaphor Corpus (VUAMC)로 학습된다. 

### Sentiment

sentiment analysis가 emotional language의 disturbance를 포착할 수 있다는 가정하에 이 feature들을 추출하여 사용한다.
[(Socher et al., 2012)](https://ai.stanford.edu/~ang/papers/emnlp12-SemanticCompositionalityRecursiveMatrixVectorSpaces.pdf)의 Recursive Neural Tensor Network sentiment analysis algorithm으로 sentiment를 1 (very negative) ~ 5 (very positive) 이렇게 token별, phrase별로 점수를 매긴다.
























