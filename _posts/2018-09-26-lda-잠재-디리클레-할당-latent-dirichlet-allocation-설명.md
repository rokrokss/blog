---
comments: true
title: LDA(Latent Dirichlet Allocation)가 무엇이냐
key: 201809260
picture_frame: shadow
tags:
  - ML
  - NLP
---

인용 수 20,000 이상의 '그 LDA'

<!--more-->

[논문도 있다.](http://delivery.acm.org/10.1145/950000/944937/3-993-blei.pdf?ip=143.248.242.199&id=944937&acc=OPEN&key=0EC22F8658578FE1%2E7500FBAD1E9579D9%2E4D4702B0C3E38B35%2E6D218144511F3437&__acm__=1533546683_ec4e0e5c9ea38aaacf7b8d563467672f)

<br>

## Beta distribution (베타 분포)

베타 분포는 $$\alpha$$, $$\beta$$ 두 매개 변수에 대해 $$[0, 1]$$ 구간의 값을 가집니다.

좀 더 보시면 알겠지만 베타 분포는 $$K=2$$인 디리클레 분포입니다.

$$\text{Beta}(x; \alpha, \beta), \;\; 0 \leq x \leq 1$$

베타 분포의 확률 밀도 함수는 다음과 같습니다.

$$
\begin{align}
\text{Beta}(x; \alpha, \beta) 
& = \frac{\Gamma(\alpha + \beta)}{\Gamma(\alpha)\Gamma(\beta)}\, x^{\alpha - 1}(1 - x)^{\beta - 1} 
\end{align}
$$

이 식의 감마 함수 $$\Gamma$$는 다음과 같이 정의된 특수 함수입니다.

$$
\Gamma(\alpha) = \int_0^\infty  x^{\alpha - 1} e^{-x}\, dx
$$


## Dirichlet distribution (디리클레 분포)

디리클레 분포는 베타 분포의 확장판으로, 0과 1사이의 사이의 값을 가지는 다변수(multivariate) 확률 변수의 베이지안 모형에 사용됩니다.

변수가 $$K$$개일 경우, 각 변수가 확률을 나타내므로 $$\sum_{i=1}^{K} x_i = 1$$ 를 만족해야 합니다.

디리클레 분포의 확률 밀도 함수는 다음과 같다.

$$
\text{Dir}(x_1, x_2, \cdots, x_K; \alpha_1, \alpha_2, \cdots, \alpha_K) 
= 
\frac{1}{\mathrm{B}(\alpha_1, \alpha_2, \cdots, \alpha_K)} \prod_{i=1}^K x_i^{\alpha_i - 1}
$$

이 식에서의 베타 함수 $$\mathrm{B}$$는 다음과 같습니다.

$$
\mathrm{B}(\alpha_1, \alpha_2, \cdots, \alpha_K) = \frac{\prod_{i=1}^K \Gamma(\alpha_i)} {\Gamma\bigl(\sum_{i=1}^K \alpha_i\bigr)}
$$

## Latent Dirichlet Allocation (LDA, 잠재 디리클레 할당)

<br>

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/LDA/1.png){:width="700px"}

<br>

LDA는 Topic Modeling의 한 기법으로, 토픽별 단어의 분포와 문서별 토픽의 분포를 모두 추정해 냅니다.

<br>

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/assets/images/LDA/2.png){:width="700px"}

<br>

전체적으로 위와 같은 구조를 가집니다.

$$D$$ : 문서 총 갯수

$$K$$ : 토픽의 총 갯수

$$N$$ : $$d$$번째 문서의 총 단어 갯수

$$w_{d,n}$$ : $$d$$번째 문서의 $$n$$번째 단어

$$\alpha, \beta$$ : hyperparameters

$$\Phi$$ : 토픽당 단어 분포

$$\Theta$$ : 문서당 토픽 분포

$$z_{d,n}$$ : 해당 단어의 토픽 분포

<br>





