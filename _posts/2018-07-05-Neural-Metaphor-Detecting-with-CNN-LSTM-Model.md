---
comments: true
title: 논문 요약&#58; Neural Metaphor Detecting with CNN-LSTM Model
key: 201807052
tags:
  - AI
  - NLP
  - 논문
  - NAACL
---

> Figurative Language Processing, NAACL 2018

CNN-LSTM 모델로 Metaphor Detection, 해당 workshop의 보고에 의하면 state-of-the-art 모델이다.

<!--more-->

[논문 링크](http://aclweb.org/anthology/W18-0913)

## Model

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Wu-NAACL2018/1.png){:width="450px"}

사실 별거없다. CNN 뒤로는 NER이나 token별 tagging할 때 써주는 Bi-LSTM-CRF 모델이랑 똑같다.
눈여겨볼 만한 것은 CNN으로 들어가는 embedding에 Word Cluster가 one-hot encoding으로 들어간다는 것이다.
이 word cluster feature는 word embedding vector에 k-means를 적용시켜서 얻는다.

## Results

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Wu-NAACL2018/2.png){:width="730px"}

저기 보이는 ensemble은 한 모델을 여러가지 hyper-parameter 환경에서 학습시켜 봤을 때 inference time에는 각 모델에서의 output을 모두 가지고 평균내거나 하는 방식으로 합쳐서 final output을 내는 것이다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Wu-NAACL2018/3.png){:width="400px"}

위 그래프는 additional feature의 영향을 보여준다.


## 소감

개인적으로 저 word cluster feature에 좀 더 의미가 있을 것 같다.
metaphorical phrase라는 것이 domain이 일치하지 않는 두 단어가 동시에 등장하면서 source domain에서 target domain으로 해석을 변화시키는 것이므로 저 feature가 이것과 연관되지 않을까.
예를 들어 “the turning wheels of a political regime”, “rebuilding the campaign machinery”, “mending foreign policy”와
같은 표현을 쓰면 mechanism domain의 knowledge와 imagery가 political systems에서 표현되도록 metaphor가 일어나는 것과 같다.

<br>

**끝!**




















