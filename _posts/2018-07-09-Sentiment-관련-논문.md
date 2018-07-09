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

Sentiment 관련 연구를 파보자!

<!--more-->

### ACL 2018


##### Identifying Transferable Information Across Domains for Cross-domain Sentiment Classification

[논문 링크](https://www.cse.iitb.ac.in/~pb/papers/acl18-cross-domain-sentiment.pdf)

Cross-domain sentiment analysis, target domain이 unlabeled일 때 label된 source domain을 갖다가 어찌저찌 이용하는 것.
domain이 변할 때 word의 opinion이 바뀌는 경우가 많은데 (positive or negative 기준으로), 여기서 중요하게 여긴 것은, 원래 opinion을 유지하는 word는 cross-domain analysis로 사용할 수 있다는 점이다.
예를 들어 *unpredictable*은 movie domain에서는 positive지만 automobile domain에서는 negative다.

요러니 labeled domain에 학습된 supervised algorithm들은 unlabeled domain을 위한 일반화된 feature를 제공해주기 힘들고, cross-domain performance가 나빠진다.



##### Learning Domain-Sensitive and Sentiment-Aware Word Embeddings

[논문 링크](https://arxiv.org/pdf/1805.03801.pdf)

##### Unpaired Sentiment-to-Sentiment Translation: A Cycled Reinforcement Learning Approach

[논문 링크](https://arxiv.org/pdf/1805.05181.pdf)

##### Cross-Domain Sentiment Classification with Target Domain Specific Information

[논문 링크](http://jkx.fudan.edu.cn/~qzhang/paper/acl2018.pdf)

##### Domain Adapted Word Embeddings for Improved Sentiment Classification

[논문 링크](https://arxiv.org/pdf/1805.04576.pdf)

##### Exploiting Document Knowledge for Aspect-level Sentiment Classification

[논문 링크](https://arxiv.org/pdf/1806.04346.pdf)


### EMNLP 2017

##### Sentiment Intensity Ranking among Adjectives Using Sentiment Bearing Word Embeddings

[논문 링크](http://aclweb.org/anthology/D17-1058)

##### Refining Word Embeddings for Sentiment Analysis

[논문 링크](http://aclweb.org/anthology/D17-1056)

##### A Cognition Based Attention Model for Sentiment Analysis

[논문 링크](https://pdfs.semanticscholar.org/3fe4/fde24fab5795f01fea7dffa9dc42cabced60.pdf)


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




















