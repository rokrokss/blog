---
layout: post
comments: true
title: 논문 요약&#58; Refining Source Representations with Relation Networks for Neural Machine Translation
key: 201805151
tags:
  - NLP
  - NMT
  - 논문
---

> 학회 불명 2018

NMT에 Relation Network를 이용하여 RNN이 오래된 정보를 잊는 문제를 해결.

이제부터는 논문 요약의 길이를 확 줄여야지.

<!--more-->

내가 쓰던 논문 요약은 너무너무 길어서 앞으로는 https://shagunsodhani.in/papers-I-read/ 요 블로그의 요약 형식을 따라해보겠다.

[논문 링크](https://arxiv.org/abs/1709.03980)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Zhang-2017/1.png)

## Introduction

NMT의 Encoder와 Attention Layer 사이에 Relation Network(CNN + Graph Propagation Layer + MLP Layer)를 추가하여 오래된 정보를 잊던 RNN의 문제를 해결한다.

NMT는 word간의 관계를 직접적으로 명시하지 않는다.(GCN이나 RNNG로 해결하던 문제)

## 기존 NMT의 한계

RNN encoder-decoder는 현재 일반적인 NMT의 구조다. 헌데, RNN은 오래된 information을 잊는다.(RNN이 원래 이 성향을 띄게 design되긴 했다.)

## Contibutions of the paper

word간의 관계(RN이 word의 위치 관계를 포착함)를 직접적으로 학습시킨다.

RN은 input(encoder가 만든 hidden states)와 같은 길이의 output sequence를 생성하므로 encoder와 attention layer의 사이에 위치하며 전체 구조에 얽히는 문제를 만들지 않는다.

## Relation Network

Relation Network는 relational reasoning을 위해 design된 Neural Network다.

set of inputs $$O = o_1,..., o_n$$이 주어졌을 때,

RN은 O를 $$RN(O) = f(sum(g(o_i, o_j)))$$로 만든다. $$f$$와 $$g$$는 내부 feed forward network에서 relation을 학습시키기 위한 함수들.

### 구조

#### CNN Layer

word가 사로간의 위치를 인식하게 되므로 이웃 단어간의 관계(context) 정보를 추출하게 된다.

#### Graph Propagation(GP) Layer

그래프 형식으로, 모든 word를 연결하는 edge를 만든다.

CNN에서 나온 모든 output vector는 그래프의 node를 뜻하고 모든 node 사이 edge가 존재하게 한다.

edge를 통해 정보가 흐르게 하여 각 node가 모든 node에게서 메세지를 받게 한다.

위는 굉장히 추상적인 표현이고 내부를 뜯어 보면, 모든 node를 나타내는 vector set $$c_1, c_2,..., c_l$$을 받았다면,
그 vector들 간의 차를 이용해 edge를 나타내는 vector set $$c_{ik}$$들을 만든다.

$$r_{ik} = LRelu(W_{mlp1}c_{ik} + b_{mlp1})$$를 이용해 새로운 vector set $$r_{ik}$$를 만들고,

$$r_i = \sum_{k=1}^l (r_{ik})$$를 이용하여 새로운 vector set $$r_1, r_2,..., r_l$$를 output으로 생성한다.

#### Multi-Layer Perceptron(MLP) Layer

GP Layer의 output이 MLP Layer로 들어간다.

해당 MLP에서는 residual connection을 이용한다.

## Datasets

- IWSLT Data - 44K sentences from tourism and travel domain.
- NIST Data - 1M Chinese-English parallel sentence pairs.

## Models

- MOSES - Open source translation system
    http://www.statmt.org/moses/
- NMT - Attention based NMT
- NMT+ - NMT with improved decoder
- TRANSFORMER - Google’s new NMT
- RNMT+ - Relation Network integrated with NMT+

## Evaluation Metric

- case-insensitive 4-gram BLEU score

## Observations

sentence의 길이가 길어질수록(50 words을 넘어가면), RNMT가 성능이 더 좋아진다.

Qualitative evaluation을 보면 RNMT+가 NMT+보다 word alignment를 더 잘 포착함을 알 수 있다.

NMT에 사용되는 Layer가 RNN이 아닌 CNN이어도 long-term dependency를 포착하는 성능은 RNMT이 더 좋다.
