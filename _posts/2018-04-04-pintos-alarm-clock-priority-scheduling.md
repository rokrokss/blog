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

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-04.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-05.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-06.png)

ready_list에 우선도 순으로 insert한다.
thread_create()과 thread_set_priority(int new_priority)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-07.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-08.png)

이거 추가해서 priority 체크 후 preemption해야 하면 바로 thread_yield()

### Synchronization 관련 함수

#### semaphore 관련 부분

sema->waiters 리스트를 우선도 정렬된 상태로 만들어야 하는데, 나는 insert 해주는 sema->value가 0일 때 sema_down() 함수는 그대로 두고, 원래는 pop_front를 해주던 sema_up에서 list_max로 max_elem을 뽑고, list_remove 한 후에 해당 스레드를 unblock 해줬다.
그리고, 이 경우에도 unblock으로 ready_list에 추가 되므로 thread_yield()가 따로 필요하다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-09.png)

#### condition 관련 부분



