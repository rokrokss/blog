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

local attention-based model과 global attention-based model 비교.

<!--more-->

**15년도 논문이다. 현재 [Vaswani et al.(2017)](https://arxiv.org/abs/1706.03762) 이 분은 CNN, RNN도 없애 버리셨다.**

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

이 논문의 attention-based model은 global과 local로 크게 구분된다.
둘의 차이는 모든 source position을 고려하는지의 여부이다.
둘 다 stacked LSTM의 t번째 hidden state $${h}_{t}$$를 input으로 받는다.

목적은 context vector $${c}_{t}$$를 뽑아내기 위함이다. $${c}_{t}$$는 target 단어 $${y}_{t}$$를 맞추는 데에 필요한 source 쪽의 정보를 저장한다.
두 개의 모델은 이러한 $${c}_{t}$$를 뽑아내는 방법에서의 차이이다.

위 두 벡터를 concatenate하여 새로운 **attentional hidden state vector $$\widetilde { h } $$**를 뽑아낸다
이를 이용하여 target 단어를 생성하는 과정은 아래와 같다.

$${ \widetilde { h } }_{ t }=tanh({ W }{ c }[c_{ t };h_{ t }])$$

$$p({ y }_{ t }|{ y }_{ <t },x)=softmax({ W }_{ s }{ \widetilde { h } }_{ t })$$


### Global Attention

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Luong-EMNLP2015/2.png){:width="400px"}

Global Attention model은 $${c}_{t}$$를 뽑아낼 때, encoder의 모든 hidden state를 고려한다.
이를 위해서는 alignment vector $${a}_{t}$$가 필요하다. $${a}_{t}$$는 source side의 timestep 갯수와 동일한 크기를 가진다.
현재의 target hidden state $$h_{ t }$$와 source hidden state $${ \bar { h } }_{ t }$$를 비교하여 유도된다.

$${ a }_{ t }(s)=align({ h }_{ t },{ \bar { h } }_{ s })=\frac { exp(score({ h }-{ t },{ \bar { h } }_{ s })) }{ \sum _{ { s' } }^{ }{ exp(score({ h }_{ t },{ \bar { h } }_{ s' })) } } $$

score는 content-based 함수이며, 세 가지 방식으로 유도될 수 있다.

$$ score({ h }_{ t },{ \bar { h } }_{ s })=\begin{cases} { h }_{ t }^{ T }{ \bar { h } }_{ s } \\ { h }_{ t }^{ T }{ { W }_{ a }\bar { h } }_{ s } \\ { W }_{ a }[{ h }_{ t }^{ };{ \bar { h } }_{ s }] \end{cases}$$

이들이 앞서 attention-based 모델을 만들 때는 location-based 함수(아래)를 사용했었다.

$${ a }_{ t }=softmax({ W }_{ a }{h}_{t})$$

즉, alignment score를 target hidden state의 가중평균으로 만들었다.
이 후, context vector $${c}_{t}$$는 $${a}_{t}$$을 곱하는 source hidden state의 가중평균으로 만들어진다.

위에서 구한 alignment vector를 이용한 가중평균
이 논문의 모델은 기존에 [Bahdanau et al. (2015)](https://arxiv.org/abs/1409.0473)가 쓴 모델과 비슷하지만 차이가 있다.
이 논문은 stacked LSTM layer의 맨 위층의 hidden state를 사용한다(encoder, decoder 모두)
이와 달리 [Bahdanau et al. (2015)](https://arxiv.org/abs/1409.0473)는 bi-directional encoder의 hidden state와 non-stacked uni-directional decoder의 hidden state를 사용했다.
그리하면 본 논문은 그보다 computational path가 단순하다.
score를 구할 때, 이 논문은 세 가지를 시험했고, [Bahdanau et al. (2015)](https://arxiv.org/abs/1409.0473)는 한 가지(concatenate, 세 번째)만 사용하였다.


### Local Attention

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Luong-EMNLP2015/3.png){:width="400px"}

global attention은 전체 source word를 attend했다.
이는 resource가 많이 필요하고, 긴 문작 혹은 문맥을 해석하는 데에 비실용적이다.
ex) 문단 혹은 글

따라서 target 단어당, 일부의 source position만 보는 모델을 생각했다
그것이 local attention이다.
이 모델은 [Xu et al. (2015)](https://arxiv.org/abs/1502.03044)가 주장한 tradeoff between the soft and hard attention model에서 영감을 받았다.

Soft attention은 global attention과 동일하다.
input image의 모든 부분에 weight를 준다.
Hard attention은 한 번에 attend할 input 이미지의 한 부분(patch)을 정한다.
빠르지만, 미분불가하고 분산감소, 강화학습 등 복잡한 기술을 많이 사용해야한다.
이 논문의 local attention은 문맥의 일부(window)만 고려하며 미분 가능하다
soft attention보다 빠르며, hard attention보다 쉽다.
방법은 아래와 같다.
t시점의 target 단어에 대하여, aligned position $${p}_{t}$$를 정한다.
$${c}_{t}$$는 $$[{p}_{t} - D, {p}_{t} + D]$$ 사이에 있는 source 단어들의 가중 평균이다.
D는 실험적으로 정한다.
따라서 이제 $${a}_{t}$$는 **고정된 크기(2D+1)**를 갖는다.

**$${p}_{t}$$를 찾는데에는 두 가지 방법이 쓰였다.**
1. Monotonic alignment(local-m)
$${p}_{t}=t$$로 단순하게 생각.
같은 위치에 있는 단어끼리 연관이 클 것이란 아이디어
$${a}_{t}$$는 global attention 때와 동일한 방법으로 생성
2. Predictive alignment

$${ p }_{ t }=S\cdot sigmoid({ v }_{ p }^{ T } \ tanh({ W }_{ p }{ h }_{ t }))$$

$${ W }_{ p }, { v }_{ p }$$ 는 학습되는 변수. S는 문장의 길이
이에 따라, $${ p }_{ t }\in [0,S]$$ 가 도출된다.
더불어, 해당 $${ p }_{ t }$$를 기준으로 gaussian적으로, 주변단어들이 의미를 가질 것이라 생각하여
$${ a }_{ t }(s)=align({ h }_{ t },{ \bar { h } }_{ s })exp(-\frac { { (s- }{ p }_{ t })^{ 2 } }{ 2{ \sigma }^{ 2 } } )$$을 이용한다.


### Input-feeding Approach

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Luong-EMNLP2015/4.png){:width="400px"}

이 논문의 모델에서는, atttentional decision이 독립적으로 이뤄진다.
하지만, 일반적인 machine training에서는 어느 단어가 번역이 완료되었는지 지속적으로 체크한다.
따라서 과거의 alignment information이 지금의 alignment decision에 고려되게(jointly) 만들어야한다.

이를 위하여 attentional vector $${ \widetilde { h } }_{ t }$$
를 다음 시점의 input과 concat시켜서 넣어준다.

이것의 목적은 다음 두가지이다.
1. 이전의 alignment choice를 알게 하고 싶다.
2. 수평&수직적으로 deep한 network를 만들고자한다.




