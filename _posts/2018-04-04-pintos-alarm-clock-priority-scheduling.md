---
layout: post
comments: true
title: <Pintos> Alarm Clock & Priority Scheduling
key: 201804041
modify_date: 2018-04-04
picture_frame: shadow
tags:
  - OS
  - Pintos
---

OS수업에서 Pintos 프로젝트를 진행 중이다.
Alarm Clock과 Priority Scheduling 관련 test case를 통과하기 위한 내 implementation을 정리해 보겠다.
이해를 위해 다시 적기 보다는 그냥 결과 기록용이니 설명은 조금씩만 적겠다.(원리 설명은 구글링하면 잘 나옴)

먼저 결과창

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-result.png)
<!--more-->

## Alarm Clock

Busy waiting -> wake up when time comes
thread가 언제 일어나야 하는지 wakeup_tick에 저장하고 thread_block()
sleep_list 만들어서 timer_interrupt 때마다 wake_up_threads()를 호출하여 sleep_list 확인하면서 thread_unblock()

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-01.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-02.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-03.png)

## Priority Scheduling

### Scheduling 관련 함수

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-01.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-01.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-01.png)




