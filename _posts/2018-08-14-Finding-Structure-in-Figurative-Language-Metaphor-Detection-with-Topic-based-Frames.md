---
comments: true
title: "논문 요약: Finding Structure in Figurative Language: Metaphor Detection with Topic-based Frames"
image: "/assets/images/paper-summary/Jang-SIGDIAL2017/1.png"
description: "주제 기반 프레임을 이용한 은유 탐지 논문의 학습 메모입니다. 비라벨 말뭉치의 어휘·문법 패턴과 반지도 부트스트래핑으로 프레임을 구성하는 흐름을 살펴봅니다."
key: 201808141
picture_frame: shadow
tags:
  - AI
  - NLP
  - 논문
  - SIGDIAL
image_alt: "Seed 단어에서 어휘·문법 패턴과 프레임을 추출하는 은유 탐지 흐름"
---

> SIGDIAL 2017

정리는 나중에 ㄱㄱ

<!--more-->

[논문 링크](http://www.aclweb.org/anthology/W17-5538)

metaphor frame templates using a semi-supervised bootstrapping approach on an unlabeled corpus?

The goal of our work is to lay a computational foundation for detection of such switches
so that social strategies regarding metaphor use in interaction can be accomplished as follow-up work.

Lexico-grammatical pattern: the shortest path that passes through the ROOT in dependencies between the domain name and seed facet instances.

BookCorpus (Zhu et al., 2015)

The corpus contains 11,038 books in 16 different genres

https://www.smashwords.com

![Seed 단어에서 어휘·문법 패턴과 프레임을 추출하는 은유 탐지 흐름](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Jang-SIGDIAL2017/1.png){:width="600px"}

![문장 수집·구문 분석·군집화를 반복하는 프레임 부트스트래핑 절차](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Jang-SIGDIAL2017/2.png){:width="300px"}











