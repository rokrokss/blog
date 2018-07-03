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






































