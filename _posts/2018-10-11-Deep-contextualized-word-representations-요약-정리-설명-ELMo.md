---
comments: true
title: 논문 요약&#58; Deep Contextualized Word Representations
key: 201810110
tags:
  - ML
  - NLP
  - 논문
  - ICLR
---

> ICLR 2018
 
동일 단어 동일 벡터 OUT! deep-BiLM의 layer마다 state를 꺼내서 합치기.

<!--more-->
 
[논문 링크](http://aclweb.org/anthology/N18-1202)
 
# 요약

## BiLM

**BiLM (Bidirectional Language Model)**

우리가 많이 쓰는 Language model은 대표적으로 Word2Vec이 있습니다.
그 Word2Vec에서는 기본적으로 Fully connected layer를 이용하여 단어의 등장을 예측하게 학습시킵니다.
그리고 그 학습된 단어벡터는 여러 모델에 초석으로 사용됩니다.
RNN을 이용하는 모델(예를 들어 sequential tagging에 사용되는 BiRNN-CRF)에도 RNN에 학습된 Word2Vec이 들어가는 경우가 있습니다.
헌데, 이런 식으로 Language model을 RNN에 input으로 넣는 경우가 아닌, RNN을 Language Model만을 위하여 사용할 수도 있습니다.

BiRNN에 Softmax를 붙여서 이용하여 한 스텝마다 다음 단어를 예측하는 모델을 학습시키면 그 자체로 Language Model이 됩니다.
(각 스텝에 뱉는 hidden state을 embedding으로 사용합니다)

이 모델이 바로 **BiLM(Bidirectional Language Model)**입니다.

하지만 이 Language Model과 Word2Vec같은 기존의 Language Model은 큰 차이점을 가지고 있는데,
Word2Vec은 학습 당시에는 context-dependent하여 주위 단어에 영향을 받지만 사용할 때는 context와 상관없이 그 단어가 어디 있든 같은 벡터가 사용되지만,
**BiLM은 inference 단계에서도 context-dependent**하다는 것입니다. 학습된 BiLM을 이용하여 텍스트 인풋을 벡터화 시키려면 문장 단위,
혹은 문서 단위로 BiLM에 집어 넣어야 합니다.
혹은 사용할 모델 앞부분에 아예 붙여서 사용합니다.

이런 방식으로 인해 개선되는 점이 있습니다.
예를 들어 다의어(polysemy)의 경우 Word2Vec을 사용할 경우 이용해야 하는 벡터가 모든 의미를 표현하고 있어야 하지만,
BiLM의 경우 context를 지니고 inference되는 벡터를 사용하므로 좀 더 효과적으로 해당 context-dependent한 정보를 얻을 수 있습니다.
 
## ELMo

**ELMo (Embeddings from Language Model)**

기본적으로 모델의 structure는 deep-BiLM을 학습시키지만,
본 논문에서의 키포인트는, 마지막 레이어의 hidden state만 사용하는 것이 아닌,
**여러 레이어의 hidden state를 모두 weighted-sum하고 사용하는 것입니다.**

$$
{ELMo}_k^{task} = E(R_k ; \Theta^{task})=\gamma^{task} \sum_{j=0}^L {s_j^{task} h_{k, j}^{LM}}
$$

핵심 표현은 요렇게 정리됩니다.
<br>

|---
| 표기 | 값
|-|:-
| $$task$$ | 걍 우리가 이후에 하려는 task
| $$k$$ | time-step
| $$\gamma^{task}$$ | hyper-parameter, 왜 존재하는지는 바로 뒤에 설명.
| $$s_j^{task}$$ | softmax-normalized weight입니다. 레이어마다의 weight.
| $$h_{k,j}^{LM}$$ | 우리 모델의 j번째 레이어, k번째 단어에서 나온 hidden state.
|---

<br>
일단 저 $$\gamma$$가 왜 필요한 지 알려면 이 모델이 다른 task에 어떻게 적용되었는지 봐야합니다.

[요 논문](https://arxiv.org/pdf/1808.09653.pdf)에서 보시면 metaphor detection에 본 LM이 사용되었는데,
GloVe 단어벡터와 ELMo를 concatenate해서 사용합니다. 본 논문에서도 저런 식으로 사용하라고 하긴 합니다.
그 때 ELMo의 weight이라고 보시면 됩니다.

~~$$s_j^{task}$$는 레이어마다 정해지는 weight이긴 한데 softmax-normalized라는 말이 이해가 안가서 지금 저자 매튜한테 메일 보내놨습니다. 제가 이해하게 되면 수정하겠습니다.~~

레이어마다 나온 hidden state를 linear combination하는 과정은 Task 모델에 포함시켜 학습되게 합니다!


# 코멘트

BiLM의 기본 구조가 context-dependent함으로 생기는 이점과, 타 모델에 적용할 때 기존 단어벡터와 합치라는 방식이 좋은 결과를 만들 수밖에 없는 것은 이해가 갑니다.

하지만 결국 이 논문에서 제일 Novel한 부분은 레이어마다 hidden state를 떼 내어 합쳐서 사용하는 모습인데, 이걸 보면 굳이 저런 식으로 해야 하나, 왜 마지막 레이어의 아웃풋만 사용하는 것이 완전할 수가 없는가.
라는 생각이 계속 들었습니다.

그래서 기억이 났는데 [Yosinski et al., 2014](https://pdfs.semanticscholar.org/a981/0fc4c6baacc3d262e73dd44bdcbbb0db034e.pdf)에
의하면 각각의 layer가 서로 다른 type의 정보를 가진다고 합니다.

우리는 단어벡터를 빈칸 채우기 방식으로만 학습합니다. 어떤 position의 단어가 무엇인지 예측하는 방식으로요.
근데 실상 그 단어벡터들을 이용한 task는 그렇지 않죠.
classification, tagging, NMT 등 아주 다양하고 word inference에 국한되지 않습니다. 이 부분에 괴리가 있다고 생각합니다.
BiLM을 그냥 사용하면 맨 위 레이어의 정보만을 갖는 것인데,
어짜피 BiLM이 학습된 목적과 적용될 Task가 다르기 때문에 BiLM이 학습되면서 만든 정보들을 모두 가져다가 쓰는 것이 더 좋게 되는 것 같습니다.

<br>

그래도 본 논문에서 가장 강력한 점은 context-dependent LM pre-training이 된다는 점입니다.
