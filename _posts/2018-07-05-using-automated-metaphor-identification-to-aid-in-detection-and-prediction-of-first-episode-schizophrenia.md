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

그리고 sentiment coherence 또한 계산하는데,

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Gutierrez-EMNLP2017/1.png){:width="160px"}

요렇게 한다. s를 token별, phrase별 sentiment score로 해주면 token별, phrase별 sentiment coherence를 구할 수 있다.

이제 SentTok, SentPhr, CohTok, CohPhr 이렇게 4개의 feature를 가진다.

## Classification Algorithms

[Bedi et al. (2015)](https://www.nature.com/articles/npjschz201530.pdf)가 사용한 convex-hall classifier를 이용한다고 한다. ~~네이쳐...~~
뒤에도 읽어 보니까 이 논문이 핵심 base paper인 것 같다.

## Results

metaphorical token은 조현병 있는 사람들이 6.3%, 없는 사람들이 5.2%로 갯수 차이가 좀 있다.
남녀 차이는 별로 없었다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Gutierrez-EMNLP2017/2.png){:width="500px"}

아까 구한 Met, SentTok, SentPhr, CohTok, CohPhr 다섯가지 feature말고도 여기서 이것저것 해놨는데 각 feature 1개씩만 classification에 사용했을 때 결과가 위 표와 같다.

## 소감

내용이 많은 논문은 아니었다. 사실 EMNLP에 뽑할만한가 잘 모르겠다.

내가 불만족스러웠던 건 조현병은 metphor를 이상하게 쓴다고 할 수도 있겠지 원래 심한 조현병 환자는 사용하는 단어의 배열이 지리멸렬하여 의사소통이 힘들다.
현재 metaphor detection의 기본적인 원리가 단어들이 원래 쓰여야 할 장소가 아닌 곳에서 관련이 크지 않은 다른 단어와 쓰이는 것을 포착하여 metaphorical phrase라 하는 것이기 때문에 위의 문제가 덩달아 해결된게 아닐까 싶다.

<br>

**끝!**
















