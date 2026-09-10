---
comments: true
title: "논문 요약: A Comparison of Feature-Based and Neural Scansion of Poetry"
image: "/assets/images/paper-summary/Agirrezabal-RANLP2017/1.png"
description: "시의 운율을 분석하는 feature 기반 모델과 신경망 모델을 비교한 논문 메모입니다. Scansion 모델의 구성과 영어·스페인어 시를 대상으로 한 평가 결과를 정리합니다."
key: 201805192
tags:
  - AI
  - NLP
  - 논문
  - RANLP
image_alt: "영어·스페인어 시 운율 분석에서 특징 기반 모델과 신경망의 오류율 비교"
---

> RANLP 2015

구현해야 하는데 시간이 없으니 일단 모델만 정리한다.

<!--more-->

[논문 링크](https://arxiv.org/abs/1711.00938)

## Model

저자는 Averaged Perceptron, HMM, CRFs, Bi-LSTMs+CRF, encoder-decoder model 실험했다.

잘 들어맞았던 건 character-based RNN with Bi-LSTM+CRF,
여기서 두 개의 character-based LSTM vector는 pre-trained word embedding과 concatenate한 것.

그 이후 이 embedding이 1개의 word를 가르킨다하고 word-level Bi-LSTM + CRF layer를 사용한다.

S2S(Syllable to Stress)

W2SP(Word to Stress Pattern)

pre-trained word embedding은 improvement를 살짝만 가져다 줌.

syllable이 space로 나뉘어 있으면 word structure를 잃으므로 WB(word boundary marker)를 만들어 놓고 실험한다.

## Results

![영어·스페인어 시 운율 분석에서 특징 기반 모델과 신경망의 오류율 비교](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Agirrezabal-RANLP2017/1.png)

4B4V dataset에서는 Bi-LSTM+CRF+WB (S2S)가 제일 잘 나옴.





