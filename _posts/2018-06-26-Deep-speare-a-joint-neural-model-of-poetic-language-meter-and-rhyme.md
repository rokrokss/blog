---
comments: true
title: 논문 요약&#58; Deep-speare&#58; a Joint Neural Model of Poetic Language, Meter and Rhyme
key: 201806261
modify_date: 2018-06-27
tags:
  - ML
  - NLP
  - 논문
  - ACL
---

> ACL 2018

애증의 poetry...poetry generation...

<!--more-->

지난 학기에 NLP 수업에서 텀프로젝트로 poetry classification을 위한 neural poetry scansion model을 만들었다...

아무튼 그건 됐고,


## Introduction

기본적으로 automatic poem generation이 main task이다. poem generation을 constrained language modelling task로 취급한다.
여기서 constraint는 rhythm 타입, stress pattern이 된다. 그리해서 전문가와 일반인에게 보여 주어 그 기준으로 좋은 성능을 보였다고 한다.

<br>

**poem generation 때문에 읽는 논문이 아니고 저 joint model이 궁금해서 읽고 있으므로 그쪽으로 휙휙 넘기겠다.**

<br>

## Dataset

여기서는 sonnet(셰익스피어가 유행시킨 시의 종류, iambic pentameter stress pattern을 따름)만 취급하고,
[Project Gutenberg](https://www.gutenberg.org/) 여기서 데이터셋을 추출했다. [GutenTag tool](https://pdfs.semanticscholar.org/487e/8b24427c2462b030fa4ab3095c360512c9fd.pdf)
요거의 rule-based structural classification 기능으로 poem의 분류를 나눴다.

## Architecture

1) language model, 2) pentameter model(iambic pentameter를 포착하기 위한),
3) rhyme model, 이 세 component로 이루어진 joint model이다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Lau-ACL2018/1.png)

요렇게 생겼다. 모든 component는 각자 sub-task를 수행하는 multitask learning으로 여기고 통째로 학습된다.

### Language Model

기본적으로 Bahdanau의 LSTM encoder-decoder with attention model을 사용한다.
selective mechanism [(Zhou et al., 2017)](https://arxiv.org/abs/1704.07073) 또한 사용한다.

### Pentameter Model



### Rhyme Model



### Generation Procedure


**좀 복잡한데 지금 급한 과제가 있어서 나중에 다시 돌아오겠다.**

























