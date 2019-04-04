---
comments: true
title: 머신러닝을 이용한 토렌트 해시 함수 개선
key: 201904041
picture_frame: shadow
tags:
  - Network
  - ML
---

Hash 값을 통한 Key 검색이 가능한 P2P 구조 개발!

<!--more-->

<br>

본 프로젝트의 아이디어는 [박세형님](https://github.com/justin-labry)에게 안내받았으며 저는 개발을 맡았습니다.

[Evaluation](https://nbviewer.jupyter.org/gist/q0115643/d5e2aee3089cca8f64791285eda23ba7),
[코드](https://github.com/q0115643/arithmetic-hash)


## 배경 SHA-1

```
A good hash function should map the expected inputs as evenly as possible over its output range. - Wikipedia/Hash_Function
```

토렌트에 사용되는 해시 알고리즘 SHA-1은 본 파일의 key 값을 인코딩하여 네트워크 공간에 어느 한 쪽 치우치지 않게 균등 분포시킨다고 합니다.
SHA-1 알고리즘을 통해 20바이트의 info_hash를 만들어 내고 이것이 트래커로 사용됩니다. 이렇게 key를 균등하게 배포해서 트래픽 과부하를 막아주는데,
이 특성은 해당 알고리즘의 디코딩이 불가능하다는 점을 감수하면서 얻어집니다.
(이 프로젝트에서는 SHA-1이 가진 '보안성'은 다루지 않습니다.)

<br>

## 개선 방향

만약 우리가 토렌트의 해시값을 디코딩하여 원래의 key값을 구할 수 있다면, 우리는 단순 검색으로 우리가 원하는 토렌트를 콕 집어 찾아낼 수 있을 것입니다.
그렇게 하기 위해서 제안되는 것이 바로 Arithmetic Hashing입니다. 인코딩(해싱)된 값이 균등 분포를 위해 어느 노드에 위치해야 하는지 디코딩이 가능한 계산 방법을 이용하는 것입니다.

<br>

기본적인 방법은 문자마다 확률을 구하여 그만큼의 영역을 할당하는 것입니다. 예를 들어 ``apple``을 해싱한다고 했을 때, 전체 key들을 보아 ``첫 문자``가 ``a``일 확률이 20%라면
apple은 ``[0, 0.1]`` 만큼의 공간이 배당되고, ``(beginning) a``((beginning)는 a가 첫 문자임을 인식하기 위해 토큰) 다음에 p가 올 확률이 5%라면 배정될 구간이 어딘지는 p까지의
다른 문자들의 확률을 알아야 하겠지만 0.1에 5%만큼의 길이를 가진 구간, ``[x, x+0.005]`` 공간이 배당됩니다. 이런 식으로 마지막 문자까지 계산을하면 ``(beginning)apple(end)``이
인코딩되는 위치를 특정할 수 있습니다. **반대로도** 문자간의 확률 분포를 알 수 있으므로 해시값(위치)를 안다면 key값을 구하는 디코딩(역추적)이 가능해집니다.

<br>

## 선행 연구

이 부분의 선행논문으로 3-order Markov Chain을 이용하여 접근한 논문이 있었습니다. 하지만 Markov Chain은 order가 한정되어 key가 길어질수록 
성능이 떨어지게 됩니다. 그래서 본 연구에서는 RNN(LSTM)을 이용해 문제를 해결합니다. brown corpus, 그리고 key가 길 때를 위한 2gram corpus를 이용해 Markov Chain과 RNN을 이용한
Arithmetic Hashing 구조를 각각 만들고 성능을 비교했습니다.

## 결과

[Evaluation](https://nbviewer.jupyter.org/gist/q0115643/d5e2aee3089cca8f64791285eda23ba7)

<br>

Evaluation 방법은, 500개의 node가 있다고 가정하여 각 key마다 위치를 계산해 어떤 node로 배정되는지 구해 각 노드의 key 갯수를 구하고, 그 표준편차를 비교했습니다.



