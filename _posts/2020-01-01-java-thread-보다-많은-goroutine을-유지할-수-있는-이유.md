---
comments: true
title: Java thread보다 많은 Goroutine을 유지할 수 있는 이유
key: 202001010
picture_frame: shadow
tags:
  - Go
---

Java thread의 갯수는 아무리 많아도 수만을 넘지 못하지만, Goroutine은 수백만을 유지할 수 있다.

<!--more-->

어떻게 가능할까? 결론부터 말하자면, 유저 스페이스에서 작동하는 M:N 스케줄러와 가변 스택 덕이다.

# Go Scheduling

# Contiguous Stack
