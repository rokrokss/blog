---
layout: post
comments: true
title: 논문 요약&#58; Effective Approaches to Attention-based Neural Machine Translation
key: 201805191
tags:
  - ML
  - NLP
  - NMT
  - 논문
---

> EMNLP 2015

NMT에 Relation Network를 이용하여 RNN이 오래된 정보를 잊는 문제를 해결.

<!--more-->

**15년도 논문이다. 이제 attention은 기본.**

아래는 기존 NMT

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Luong-EMNLP2015/1.png){:width="400px"}


## Introduction

본 논문이 나올 당시에는 attention 구조의 종류별 비교가 없었다. 본 논문에서는 attention-based architectures for NMT, 그 중 global attention과 local attention 간의 성능을 비교한다.

global attention model은 모든 source word에 attended되고, local attention model은 source 중 일부만이 한번에 attended된다. local attention model은 hard attention model과 soft attention model을 섞은 것과 같다. 계산은 global보다 간단하고, hard attention과 달리 local attention은 differentiable하여 implement와 train이 쉽다.

이것으로 BLEU score 기준, English->German translation에서 당시의 new state-of-the-art를 달성했다.


## Neural Machine Translation

[Attention-based NMT를 설명했던 포스트](http://rokrokss.com/2018/05/04/Learning-to-Parse-and-Translate-Improves-Neural-Machine-Translation.html#2-neural-machine-translation)

NMT는 encoder와 decoder로 구성되며 조건부확률 $${p(y|x)}$$ 를 모델링하는 뉴럴넷이다.
식은 아래와 같다.

$$log {\  p(y|x) } =\sum_{ j=1 }^{ m }{ \log { p({ y_j }|{ y }_{ <j },s) } }$$

  - y는 target sentence, x는 source sentence
  - encoder : source sentence를 대표하는 s 벡터를 만드는 과정
  - decoder : target 단어들을 하나씩 순서대로 만드는 과정

가장 일반적으로 decoder로 사용되는 건 RNN이지만, 그 형태는 논문마다 약간씩 다르다.
  - [Kalchbrenner and Blunsom (2013)](https://aclanthology.coli.uni-saarland.de/papers/D13-1176/d13-1176) : 일반적인 RNN 사용, encoder로 CNN 사용.
  - [Sutskever et al. (2014)](https://arxiv.org/abs/1409.3215)  [Luong et al. (2015)](https://arxiv.org/abs/1410.8206) : LSTM을 쌓아서 encoder와 decoder로 사용.
  - [Cho et al. (2014)](https://arxiv.org/abs/1406.1078)  [Bahdanau et al. (2015)](https://arxiv.org/abs/1409.0473)  [Jean et al. (2015)](https://arxiv.org/abs/1412.2007) : GRU를 이용한 encoder and decoder 사용.
decoding을 수식으로 나타내면 아래와 같다.(h는 RNN hidden unit)

$${h_j} = f(h_{j-1},s)$$

$$p({ y_j }|{ y }{ <j },s) = softmax(g({h}_{j}))$$

위에 나열된 paper 대부분이 s를 처음에 decoder의 hidden state를 initialize 할 때 한 번만 사용하지만
[Bahdanau et al. (2015)](https://arxiv.org/abs/1409.0473)와 [Jean et al. (2015)](https://arxiv.org/abs/1412.2007)은,
그리고 이 논문은 s를 전체의 번역 과정에서 사용한다. 이 부분이 attention mechanism을 형성한다.
이 논문에서는 NMT model로 stacking LSTM architecture(figure 1처럼)를 사용한다.


## Attention-based Models












