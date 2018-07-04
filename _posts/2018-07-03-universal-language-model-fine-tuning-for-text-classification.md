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
하지만 본 논문의 ULMFiT은 다 해결함.

























































