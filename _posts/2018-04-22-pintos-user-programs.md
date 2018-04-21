---
layout: post
comments: true
title: Pintos Project 2&#58; Alarm Clock & Priority Scheduling
key: 201804041
modify_date: 2018-04-04
picture_frame: shadow
tags:
  - OS
  - Pintos
---

OS수업에서 Pintos 프로젝트를 진행 중이다.
User Programs 관련 test case를 통과하기 위한 내 implementation을 정리해 보겠다.

이번 과제는 좀 복잡해서 작동원리를 이해하기 위한 순서로 code를 설명하면 답이 없으므로, 그냥 code만 가지고 보여주겠다.

process.c와 syscall.c를 중심으로 수정하면 되는데, 먼저 process.c

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1/pintos-pj1-result.png)
<!--more-->