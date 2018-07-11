---
layout: post
comments: true
title: Sentiment 관련 논문 리스트업
key: 201807091
picture_frame: shadow
tags:
  - ML
  - NLP
  - 논문
---

Sentiment 관련 연구를 파보자, 지금 Sentiment Analysis에 Metaphor 관련 연구를 응용하는 목표로 공부하고 있어서 Sentiment 아니어도 내가 보고 싶은 논문들이다.

<!--more-->

### ACL 2018


##### Identifying Transferable Information Across Domains for Cross-domain Sentiment Classification

[논문 링크](https://www.cse.iitb.ac.in/~pb/papers/acl18-cross-domain-sentiment.pdf)

Cross-domain sentiment analysis, target domain이 unlabeled일 때 label된 source domain을 갖다가 어찌저찌 이용하는 것.
domain이 변할 때 word의 opinion이 바뀌는 경우가 많은데 (positive or negative 기준으로), 여기서 중요하게 여긴 것은, 원래 opinion을 유지하는 word는 cross-domain analysis로 사용할 수 있다는 점이다.
예를 들어 *unpredictable*은 movie domain에서는 positive지만 automobile domain에서는 negative다.

요러니 labeled domain에 학습된 supervised algorithm들은 unlabeled domain을 위한 일반화된 feature를 제공해 주기 힘들고, cross-domain performance가 나빠진다.
$${\chi}^2$$ test는 annotated corpus에서 word의 significance와 polarity를 파악하는데 쓰인다.
본 논문에서는 words의 context vector의 $${\chi}^2$$ test와 cosine-similarity를 이용하여
domain들에서의 **Significant Consistent Polarity (SCP)**를 계산한다.
SCP 계산한 다음 Ensemble-based Cross-domain Adaptation Algorithm이란 걸 이용해서 분류한다.

##### Learning Domain-Sensitive and Sentiment-Aware Word Embeddings

[논문 링크](https://arxiv.org/pdf/1805.03801.pdf)

앞 논문과 같은 문제를 다룬다. words의 sentiment representation이 domain-sensitive하다는 것.
본 논문에서는 domain-sensitive와 sentiment-aware를 전부 학습하고 sentiment semantics와 domain specificity of words를 jointly modeling한다.
본 모델은 domain-common embedding과 domain-specific embedding을 동시에 만들어 낸다. word2vec의 변형이 사용됨.

##### Unpaired Sentiment-to-Sentiment Translation: A Cycled Reinforcement Learning Approach

[논문 링크](https://arxiv.org/pdf/1805.05181.pdf)

Sentiment-to-Sentiment Translation은 sentence의 내용을 유지한 채 sentiment를 바꾸는 것이다.
이거는 지금 내가 강화학습을 잘 몰라서... 일단 딴거부터...

##### Cross-Domain Sentiment Classification with Target Domain Specific Information

[논문 링크](http://jkx.fudan.edu.cn/~qzhang/paper/acl2018.pdf)

domain adaptation 관련 논문 많이도 쏟아져 나왔다. domain-invariant, domain-specific embedding 뽑고 classifier를 얘네 둘 각각에 대해 학습시키고 이리저리 한다.

##### Domain Adapted Word Embeddings for Improved Sentiment Classification

[논문 링크](https://arxiv.org/pdf/1805.04576.pdf)

generic embedding과 domain specific embedding을 합쳐 Domain Adapted Word Embedding 만듬.
Canonical Correlation Analysis (CCA)를 사용함.

##### Exploiting Document Knowledge for Aspect-level Sentiment Classification

[논문 링크](https://arxiv.org/pdf/1806.04346.pdf)

기본적인 LSTM+ATT sentiment classification에서 document-level과 aspect-level로 multi-task learning.

##### Efficient Large-Scale Neural Domain Classification with Personalized Attention

[논문 링크](https://arxiv.org/pdf/1804.08065.pdf)

classification에서 아주 큰 domain에서 personalized attention을 이용하는건데 (아마존에서 냈다.) 이건 패스.

##### Domain Adaptation with Adversarial Training and Graph Embeddings

[논문 링크](https://arxiv.org/pdf/1805.05151.pdf)

자연재해에 대한 sns post 데이터셋 두 개 (earthquake, flood)를 이용해서 하나는 labeled와 unlabeled data 전부, 하나는 unlabeled data만 이용한다.
adversarial training을 통한 후자의 dataset에서의 adaptation.

### EMNLP 2017

##### Sentiment Intensity Ranking among Adjectives Using Sentiment Bearing Word Embeddings

[논문 링크](http://aclweb.org/anthology/D17-1058)

##### Refining Word Embeddings for Sentiment Analysis

[논문 링크](http://aclweb.org/anthology/D17-1056)

word2vec 같은 pre-trained word vector를 가지고 sentiment를 기준으로 더 부합하도록 조정한다.

sentiment score의 사전인 sentiment lexicon을 이용하는데, target word에 대해 cosine similarity로 나온 word set을 sentiment score 기준으로 re-ranking한다.
높은 rank의 words는 더 큰 weight을 부여받는다. 요렇게 하면 words가 sentiment가 비슷한 것끼리 가깝게, 다른 것끼리 멀게 refine된다. 

##### A Cognition Based Attention Model for Sentiment Analysis

[논문 링크](https://pdfs.semanticscholar.org/3fe4/fde24fab5795f01fea7dffa9dc42cabced60.pdf)

eye-tracking data 썼음.

### ACL 2017

##### Active Sentiment Domain Adaptation

[논문 링크](http://www.aclweb.org/anthology/P17-1156)

##### Learning Cognitive Features from Gaze Data for Sentiment and Sarcasm Classification using Convolutional Neural Network

[논문 링크](https://www.cse.iitb.ac.in/~pb/papers/acl17-cogfeatures.pdf)

##### Linguistically Regularized LSTM for Sentiment Classification

[논문 링크](https://arxiv.org/pdf/1611.03949.pdf)

##### EmoNet: Fine-Grained Emotion Detection with Gated Recurrent Neural Networks

[논문 링크](http://www.aclweb.org/anthology/P17-1067)

##### Multilingual Connotation Frames: A Case Study on Social Media for Targeted Sentiment Analysis and Forecast

[논문 링크](https://homes.cs.washington.edu/~hrashkin/publications/mlconnframes_aclshort_2017.pdf)




















