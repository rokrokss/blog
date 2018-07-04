---
layout: post
comments: true
title: 논문 요약&#58; Universal Language Model Fine-tuning for Text Classification
key: 201807031
tags:
  - ML
  - NLP
  - 논문
  - ACL
---

> ACL 2018

사수님이 보라고 주셨다.

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
3. text classification에서 state-of-the-art 발라 버렸다.
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

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Howard-ACL2018/1.png)

모델은 위와 같다. 3-layer LSTM으로 되어 있고, 1) 먼저 general-domain corpus에 맞추어 pre-train되고, 2) 전체 language model이 target task를 위해 주어진 data에 맞추어 discriminative fine-tuning과 slanted triangular learning rates를 이용하여 fine-tuning되고, 3) classifier가 gradual unfreezing, discriminative fine-tuning, slanted triangular learning rates를 이용하며 fine-tuning된다.

여기서 language modeling을 위해서는 기본적으로 당시 state-of-the-art인 [AWD-LSTM](https://arxiv.org/pdf/1708.02182.pdf)을 사용한다.

### General-domain LM pretraining

[Wikitext-103](https://einstein.ai/research/the-wikitext-long-term-dependency-language-modeling-dataset) 데이터 위에서 pre-train한다.
가장 오래 걸리지만 한 번하면 다신 안 해도 된다.

### Target task LM fine-tuning

이제 pretrained general-domain LM이 주어진 상태이다.
그대로 가져다가 target task의 data에서 학습시키는데,
여기서 discriminative fine-tuning, slanted triangular learning rates 두 가지 새로운 테크닉이 있다.

#### Discriminative fine-tuning

[Yosinski et al., 2014](https://pdfs.semanticscholar.org/a981/0fc4c6baacc3d262e73dd44bdcbbb0db034e.pdf)에 의하면 각각의 layer가 서로 다른 type의 정보를 가진다고 한다.

그러므로 각 layer마다 서로 다른 learning rate를 적용한다.
저자는 실험적으로 마지막 layer의 learning rate를 정하고 1칸씩 앞으로 갈수록 learning rate가 2.6으로 나눈 값으로 설정하는 것이 성능이 좋다고 했다.

#### Slanted triangular learning rates

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/paper-summary/Howard-ACL2018/2.png)


### Target task classifier fine-tuning


























































