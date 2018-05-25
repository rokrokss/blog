---
layout: post
comments: true
title: 논문 요약&#58; Design Challenges for Entity Linking
key: 201805241
tags:
  - ML
  - NLP
  - EL
  - 논문
  - TACL
---

> TACL 2015

~~VINCULUM이라는 새로운 system을 개발하여 Entity Linking의 state-of-the-art를 갱신한다.~~

당시 Entity Linking 연구들 간의 존재하는 Ambiguity를 언급하며 그 이유와 해결방안을 제시했다.

<!--more-->

Abstract랑 Introduction만 읽고 저자들이 개발했다는 VINCULUM이 대단하다는 줄 알았는데
결과랑 분석을 보고 나니 VINCULUM보다는 문제 제시와 aspects 분석이 더 중요한 것이였다.
그러므로 VINCULUM 관련 내용은 번역 안 함.

## Entity Linking (EL)


EL은 information extraction의 중심 분야이다. entity를 인식하여 Knowledge Base(KB)에 link하는 일. 여기서 KB는 보통 Wikipedia를 많이 쓴다.

예시: *JetBlue begins direct service between Barnstable Airport and JFK International.*

여기서 *“JetBlue”*는 *KB:JetBlue*로, *“Barnstable Airport”*는 *KB:Barnstable Municipal Airport*로, *“JFK International”*은 *KB:John F. Kennedy International Airport*로 link되어야 한다. 이 link들은 읽는 인간에게 semantic annotation을 줄 뿐만 아니라, machine에게도 마찬가지로 semantic knowledge를 습득시킬 수 있다.

EL은 distantly-supervised relation extraction과 같은 NLP 응용 분야에서 training data를 형성하거나, disambiguation 등에 도움이 된다. 이 논문이 나오기 전까지는, EL에 관한 연구가 많음에도 불구하고 어느 것이 The-State-of-the-Art가 무엇인지 판단하기가 힘든데 그 이유로는, (1)EL에 대한 standard definition이 없고, (2)system이 같은 data set을 사용하며 비교되는 경우가 드물어 approach간의 비교를 하기 힘들고, (3)approach의 무엇을 보고 비교할 지 정하지 못한 점들이 있다. 이 논문에서는 simple, modular, unsupervised EL system인 VINCULUM을 개발하였다.


### NIL entities


Wikipedia에 없는 entity들. AIDA data는 비슷한 annotation으로 NIL entity를 포함하는데 ACE랑 MSNBC는 안함.


## 당시 EL field의 문제점

- Problem의 standard definition이 없음
- Approach들이 dataset을 다 다르게 가지고 개발되었으므로 system간의 비교가 힘들다.
- System을 비교하려 해도 어떤 aspect를 기준으로 가질 것인지 확실하지 않다. 


## Datasets

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Ling-TACL2015/1.png)

당시 approach들이 사용하는 dataset의 sparsity를 보여 주는 표.

## Evaluation Metrics


### Bag-of-Concept F1 (ACE, MSNBC)

### Micro Accuracy (TAC09, TAC10, TAC10T)

### TAC-KBP B^3 + F1 (TAC11, TAC12)

### NER-style F1 (AIDA)

Guidelines

Entity Mention: Common or Named?

How Specific Should Linked Entities Be?

Metonymy

Named Entities, But of What Types?

Can Mention Boundaries Overlap

VINCULUM, A Simple & Modular Linking Method































