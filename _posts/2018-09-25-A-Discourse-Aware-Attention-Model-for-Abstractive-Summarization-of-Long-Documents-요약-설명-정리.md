---
comments: true
title: "논문 요약: A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents"
image: "/assets/images/paper-summary/Cohan-NAACL2018/1.png"
description: "긴 문서의 추상적 요약을 위한 담화 인식 attention 모델을 정리합니다. 단어·섹션 계층의 인코더와 디코더 구조, arXiv·PubMed 데이터셋 평가를 살펴봅니다."
key: 201809250
tags:
  - AI
  - NLP
  - 논문
  - NAACL
image_alt: "단어·섹션 attention을 결합한 긴 문서 요약 인코더·디코더"
---

> NAACL 2018
 
Word -> "Section" -> Document 순서로 계층에 따른 Attention Network
 
<!--more-->
 
[논문 링크](https://arxiv.org/pdf/1804.05685.pdf)
 
## Introduction
 
Attention Mechanism만 알고 있다면 별로 어렵지 않습니다. 먼저 [이 논문 설명](http://kimhyungrok.com/post/2018/09/24/Hierarchical-Attention-Networks-for-Document-Classification-요약-정리-설명.html)을
보면, 저 논문의 HAN 모델은 Word -> Sentence -> Document의 계층 구조를 가진 Attentive 모델이었습니다.
 
여기서는 Sentence 대신 "Section"을 가진, 예를 들어 Introduction, Experiment, Conclusion 등의 Section으로 나뉘는 일반적인 논문과 같은 Document에 적용한, Word -> Section -> Document의 계층 구조의 Attentive Model을 고안한 것입니다.
다만, 여기서는 Classification이 아닌 Summarization Task에 응용하였습니다.
 
## Model
 
![단어·섹션 attention을 결합한 긴 문서 요약 인코더·디코더](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Cohan-NAACL2018/1.png){:width="500px"}
 
## Result
 
![arXiv·PubMed 문서 요약에서 모델별 ROUGE 점수 비교](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Cohan-NAACL2018/2.png){:width="400px"}
 
빠진 수식들은 [본 논문](https://arxiv.org/pdf/1804.05685.pdf)을 보시기 바랍니닷.