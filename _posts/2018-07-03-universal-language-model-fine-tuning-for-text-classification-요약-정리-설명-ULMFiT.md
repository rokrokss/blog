---
comments: true
title: 논문 요약&#58; Universal Language Model Fine-tuning for Text Classification
key: 201807031
tags:
  - AI
  - NLP
  - 논문
  - ACL
---

> ACL 2018

사수님이 보라고 주셨다. NLP를 위한 fine-tuning.

<!--more-->


[논문 링크](https://arxiv.org/abs/1801.06146)

## Introduction

transfer learning은 computer vision 연구에 큰 영향을 끼쳤다. object detection, classification, segmentation 등등
fine-tuned model을 안 쓰는게 거의 없다.

NLP task에서는 지금까지 transfer learning이 CV에서만큼 성공적이지 못했는데, 그 이유를 보자면.

- CV에 비하면 NLP 모델들은 얕고 task마다 1차적인 word embedding을 제외하면 공통적으로 사용될만한게 별로 없다.
- 우리가 해결방법을 잘 알지 못했다.

그래서 이분들이 등장했다. Universal Language Model Fine-tuning (ULMFiT) 으로 정복하고 구원.



## Contribution

1. Universal Language Model Fine-tuning (ULMFiT) 방법을 제시하여 Vision 쪽에서의 transfer learning과
같은 효과를 NLP task에서 보일 수 있게 했다.
2. fine-tuning을 위한 discriminative fine-tuning, slanted triangular learning rates, gradual unfreezing,
세 가지 새로운 효율적인 technique을 제시했다.
3. text classification에서 state-of-the-art
4. sample-efficient transfer learning과 extensive ablation analysis
5. pretrained model들이 다른 곳에도 잘 쓰일 수 있게 했다.

## Related work

### Transfer learning in CV

general to task-specific transition으로 말할 수 있다.
단순히 더 설명하자면, 주어진 task에 대하여 잘 학습된 모델이 필요할 때, 현재 task보다 더 general한 목적 하에 학습된 모델을 가지고 학습을 시작하는 것이다.
여러 NLP task에서도 pre-trained word2vec을 사용하는 경우들과 같다. 다만 이 경우는 1st layer만 transfer된다고 볼 수 있다.
원래는 CV에서도 모델의 1st layer만 학습된 feature들을 갖다 썼는데 요즘에는 여러 개를 fine-tuning하여 갖다 쓰거나 뒤쪽 layer들도 학습된 걸로 가져다가 쓴다.

### Hypercolumns

다른 종류에 task에서 pre-trained된 embedding을 사용하는 것.
CV 쪽에서는 hypercolumn이 end-to-end fine-tuning한테 져서 거의 안 쓴다.

### Multi-task learning

main task model에 다른 language modeling objective를 결합해서 학습시키는 것. (ex. 기계번역 model에 syntactic parsing 기능을 넣어 놓고 objective function을 잘 짜기)
얘네는 pre-trained된 걸 쓰는 건 아니고 매번 scratch부터 다시 학습된다.
objective function을 디자인할 때 좀 힘듬.

### Fine-tuning

pre-trained된 모델을 가져다가 쓸 때 목적이 다르다해도, 비슷해서 약간 변화시켜서 현재 task를 위해 사용할 수 있을 때, 그 모델을 변화시키고 필요한 부분은 (정교하게) training 시키는 것을 말한다.
예를 들어, (개, 고양이) 두 개의 카테고리로 사진을 분류해야 한다고 치자. VGG16 모델이 사진을 1000개의 카테고리로 분류하게 학습되어 있다면 그걸 가지고 와서 bottleneck feature가 나오는 부분에서 짤라서 거기다가 affine layer 하나 장착시켜서 그 부분만 학습시키면 목적에 맞는 모델을 만들 수 있다.

NLP에서도 [QA에 이용한다던가,](https://arxiv.org/pdf/1702.02171.pdf) [distantly supervised sentiment analysis에 이용한다던가](http://www.aclweb.org/anthology/S15-2079) 해봤지만 관계가 직접적으로 없는 모델에서는 실패하며,
language model을 fine-tuning하여 좋은 성능을 내려면 수백만 개 이상의 document가 필요하다.
하지만 본 논문의 ULMFiT은 다 해결하고 small dataset으로 state-of-the-art 달성함.

## Universal Language Model Fine-tuning (ULMFiT)

Language modeling은 NLP task의 가장 기본적은 source task이다. 본 논문에서는 pre-trained된 language model을 classification에 맞춰 fine-tuning한다.
language modeling을 학습시키면서 특정한 또 다른 task, syntactic dependency처럼 특정 feature에 sensitive하게 모델을 짤 수도 있겠지만 그 부분은 future work로 열어두었다.

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/1.png)

모델은 위와 같다. 3-layer LSTM으로 되어 있고, 1) 먼저 general-domain corpus에 맞추어 pre-train되고, 2) 전체 language model이 target task를 위해 주어진 data에 맞추어 discriminative fine-tuning과 slanted triangular learning rates를 이용하여 fine-tuning되고, 3) classifier가 gradual unfreezing, discriminative fine-tuning, slanted triangular learning rates를 이용하며 fine-tuning된다.

여기서 language modeling을 위해서는 기본적으로 당시 state-of-the-art인 [AWD-LSTM](https://arxiv.org/pdf/1708.02182.pdf)을 사용한다.

### General-domain LM pretraining

[Wikitext-103](https://einstein.ai/research/the-wikitext-long-term-dependency-language-modeling-dataset) 데이터 위에서 pre-train한다.
가장 오래 걸리지만 한 번하면 다시 안 해도 된다.

### Target task LM fine-tuning

이제 pretrained general-domain LM이 주어진 상태이다.
그대로 가져다가 target task의 data에서 학습시키는데,
여기서 discriminative fine-tuning, slanted triangular learning rates 두 가지 새로운 테크닉이 있다.

#### Discriminative fine-tuning

[Yosinski et al., 2014](https://pdfs.semanticscholar.org/a981/0fc4c6baacc3d262e73dd44bdcbbb0db034e.pdf)에 의하면 각각의 layer가 서로 다른 type의 정보를 가진다고 한다.

그러므로 각 layer마다 서로 다른 learning rate를 적용한다.
저자는 실험적으로 마지막 layer의 learning rate를 정하고 1칸씩 앞으로 갈수록 learning rate가 2.6으로 나눈 값으로 설정하는 것이 성능이 좋다고 했다.

#### Slanted triangular learning rates

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/2.png){:width="450px"}

빠르고 효율적으로 gradient descent가 이루어지려면 learning rate의 in-train 조절이 필요한데,
여기서는 위 그래프와 같이 변화시킨다. 이것이 slanted triangular learning rates (STLR)이다.

### Target task classifier fine-tuning

이제 classifier에 맞추어 fine-tuning을 해야 한다.

linear layer 두 개를 더 붙이고 마지막 softmax로 target class들에 해당하는 확률이 나오도록 한다.

#### Concat pooling

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/3.png){:width="350px"}

hidden state를 뽑아 올 때 중요 정보를 잃을 수 있다. 그러므로 위 계산처럼 각 time step의 hidden state를 concatenate한 H를 max-pool한 값과 min-pool한 값을 h와 concatenate하여 보내 준다.

#### Gradual unfreezing

모든 layer를 함께 fine-tuning하기보다, 다 얼려놓고 last layer부터 천천히 unfreeze한다.

#### BPTT for Text Classification (BPT3C)

Language model 학습에는 large input sequence에 유리한 Backpropagation through time (BPTT)을 이용한다.

large document에 대해 classifier를 잘 fine-tuning하기 위서는 BPTT for Text Classification (BPT3C)을 이용한다.
batch 사이즈를 정해두고, 각 batch의 시작마다 model의 hidden state를 이전 batch의 final state로 초기화해둔다.
variable length backpropagation sequences도 사용한다. [(Merity et al., 2017a)](https://arxiv.org/pdf/1708.02182.pdf)

#### Bidirectional language model

모든 실험에서 forward LM, backward LM 둘 다 학습시키고 fine-tuning에서도 각 LM에서 BPT3C을 따로 쓰고 classifier prediction도 따로 구해 평균낸다.

## Results and Analysis

### Results

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/4.png)

CoVe [(McCann et al., 2017)](https://arxiv.org/pdf/1708.00107.pdf) 얘가 당시 state-of-the-art transfer learning method 였단다.

### Analysis

#### Low-shot learning

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/5.png)

IMDb와 AG 데이터셋이서는 supervised ULMFiT가 example 100개만 가지고서도 10배 20배의 데이터로 scratch부터 학습된 모델만큼의 성능을 낸다.

general-domain LM pretraining이 빛을 발하는 순간이다. 작은 데이터셋으로도 좋은 성능을 얻을 수 있다.
여기에 unlabeled example (50k for IMDb, 100k for AG)를 semi-supervised learning에 사용할 수 있다면 50배 100배 많은 데이터셋을 가진 scratch부터의 모델의 성능을 낼 수 있다.

#### Impact of pretraining

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/6.png){:width="400px"}

pretraining이 작은 데이터셋에서 강점을 가졌지만 Table 4를 보면 큰 데이터셋에서도 성능 향상을 가진다.

#### Impact of LM quality

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/7.png){:width="400px"}

LM을 좋은 걸 쓰면 이만큼 성능이 향상된다. 특히 데이터셋 크기가 작을 때는 더 중요하다.

#### Impact of classifier fine-tuning

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/8.png){:width="400px"}

어떤 환경에서 뭐가 더 좋았고 어떻고 하는데 좀 길어서 본문 보는게 좋다.

#### Classifier fine-tuning behavior

![text](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/paper-summary/Howard-ACL2018/9.png){:width="400px"}

아까 Target task classifier fine-tuning 에서 이것저것 테크닉을 써줬는데 그런거 안하고 그냥 다 한꺼번에 학습시키면 저렇게 성능이 안 좋다.

#### Impact of bidirectionality

bidirectionality를 이용해서 forward LM, backward LM의 결과를 평균내는 편이 성능을 0.5-0.7은 상향시킨다.


## Discussion

- 영어가 아니면 데이터셋이 상당히 부족한데 이 연구가 많이 도움될 것이다.
- labeled data가 별로 없는 경우도 연구가 많이 도움될 것이다.
- language modeling이 multi-task learning이나 다른 feature를 직접적으로 포착하게 하면 도움이 될 수 있다.
- classification이 아닌 다른 task에 적용시켜볼 수 있다.

## Conclusion


We have proposed ULMFiT, an effective and extremely sample-efficient transfer learning method that can be applied to any NLP task. We have also proposed several novel fine-tuning techniques that in conjunction prevent catastrophic forgetting and enable robust learning across a diverse range of tasks. Our method significantly outperformed existing transfer learning techniques and the state-of-the-art on six representative text classification tasks. We hope that our results will catalyze new developments in transfer learning for NLP.

<br>

*힘들다... Conclusion은 원문으로...*

<br>

**끝!**




































