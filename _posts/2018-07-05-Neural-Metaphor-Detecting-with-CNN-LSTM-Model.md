---
comments: true
title: "논문 요약: Neural Metaphor Detecting with CNN-LSTM Model"
image: "/assets/images/paper-summary/Wu-NAACL2018/1.png"
description: "CNN과 LSTM을 결합한 은유 탐지 논문을 정리합니다. 단어·문자 표현, CRF·softmax 출력과 POS·클러스터 특징의 조합이 분류 성능에 미치는 영향을 살펴봅니다."
key: 201807052
tags:
  - AI
  - NLP
  - 논문
  - NAACL
image_alt: "단어·문자 임베딩과 BiLSTM·CRF를 결합한 은유 탐지 모델"
---

> Figurative Language Processing, NAACL 2018

CNN-LSTM 모델로 Metaphor Detection, 해당 workshop의 보고에 의하면 state-of-the-art 모델이다.

<!--more-->

[논문 링크](http://aclweb.org/anthology/W18-0913)

## Model

![단어·문자 임베딩과 BiLSTM·CRF를 결합한 은유 탐지 모델](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Wu-NAACL2018/1.png){:width="450px"}

사실 별거없다. CNN 뒤로는 NER이나 token별 tagging할 때 써주는 Bi-LSTM-CRF 모델이랑 똑같다.
눈여겨볼 만한 것은 CNN으로 들어가는 embedding에 Word Cluster가 one-hot encoding으로 들어간다는 것이다.
이 word cluster feature는 word embedding vector에 k-means를 적용시켜서 얻는다.

## Results

![CNN·LSTM·CRF 조합별 은유 탐지 정밀도·재현율·F1 비교](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Wu-NAACL2018/2.png){:width="730px"}

저기 보이는 ensemble은 한 모델을 여러가지 hyper-parameter 환경에서 학습시켜 봤을 때 inference time에는 각 모델에서의 output을 모두 가지고 평균내거나 하는 방식으로 합쳐서 final output을 내는 것이다.

![품사와 단어 클러스터 특징 추가에 따른 은유 탐지 성능 비교](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Wu-NAACL2018/3.png){:width="400px"}

위 그래프는 additional feature의 영향을 보여준다.


## 소감

개인적으로 저 word cluster feature에 좀 더 의미가 있을 것 같다.
metaphorical phrase라는 것이 domain이 일치하지 않는 두 단어가 동시에 등장하면서 source domain에서 target domain으로 해석을 변화시키는 것이므로 저 feature가 이것과 연관되지 않을까.
예를 들어 “the turning wheels of a political regime”, “rebuilding the campaign machinery”, “mending foreign policy”와
같은 표현을 쓰면 mechanism domain의 knowledge와 imagery가 political systems에서 표현되도록 metaphor가 일어나는 것과 같다.

<br>

**끝!**




















