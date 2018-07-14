---
layout: post
comments: true
title: 논문 요약&#58; Learning Domain-Sensitive and Sentiment-Aware Word Embeddings
key: 201807121
tags:
  - ML
  - NLP
  - 논문
  - ACL
---

> ACL 2018

Sentiment Analysis를 위한 Domain adaptation

<!--more-->

[논문 링크](https://arxiv.org/pdf/1805.03801.pdf)

## Introduction

본 논문에서는, word embedding을 domain-sensitive, sentiment-aware하게 학습시키고, words의 domain 파악과 함께 sentiment analysis를 목적으로 한다.

## Related Work

결국에는 18년도 ACL에 쏟아져 나온 논문들과 함께 domain 관련 문제점을 해결하려는 시도다. word embedding이 target domain에서 (혹은 general domain에서) 학습되었을 경우 단어의 의미가 domain-dependent하여 sentiment analysis가 원활하지 못하다.
많은 단어들이 domain에 따라 단어의 opinion이 바뀌는 경우가 많기 때문이다. 예를 들어 unpredictable은 movie domain에서는 positive지만 automobile domain에서는 negative다.

이전의 시도들에서는 domain 간 common feature를 찾아 이용했었지만 본 논문에서는 domain-common & domain-specific embedding을 모두 사용한다.

본 논문과 같이 multiple domain을 고려한 word embedding을 학습하는 논문들도 있는데, 대부분은 여러 domain에서 분리된 embedding을 학습시킨다.
그 이후 frequency-based statistical measure로 pivot words를 골라서 각 embedding space를 연결해 준다.
본 논문에서는 domain-common words는 sentiment information과 context words를 이용하여 결정된다.

## Model, DSE

DSE (**D**omain-sensitive and **S**entiment-aware word **E**mbeddings) 라고 부른단다.

multiple domain 환경에서 가능한데 논문에서는 일단 2개의 domain 위에서 설명하였고 그 이상의 경우에서 어떻게 적용하는지 소개해 놓았다.

### Design of Embeddings

각 word $$w$$에 대해 latent variable $$z_w$$를 부여, $${z_w}=1$$이면 $$w$$는 common, 아니면 $$w$$는 domain p나 q에 specific.

원하는 모델을 얻기 위해 word2vec에 변형을 시키는데 먼저 skip-gram의 단어 $$w$$일 때 주변 단어 $$w_t$$의 확률 식이 아래와 같다.

$$p({w_t}|w)=\sum_{k \in \{0,1\}} p({w_t}|w, {z_w}=k)p({z_w}=k)$$

원래는 $$z_w$$ 관련 항 없이 $$w$$에 대한 $$w_t$$가 되어야 하는데 $$z_w$$ dependent하게 만들었다.

그렇다면 $$z_w=1$$, 즉 $$w$$가 domain-common word일 경우, 아래와 같은 식을 얻을 수 있다.

$$p({w_t}|w, z_w=1)= \frac{exp(U_w^c \cdot V_{w_t})}{\sum_{w^ \prime \in \Lambda} exp(U_w^c \cdot V_{w_ \prime })}$$

## Results

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Shi-ACL2018/1.png){:width="800px"}













































