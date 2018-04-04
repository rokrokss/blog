---
layout: post
comments: true
title: Pintos&#58; Alarm Clock & Priority Scheduling
key: 201804041
modify_date: 2018-04-04
picture_frame: shadow
tags:
  - OS
  - Pintos
---

OS수업에서 Pintos 프로젝트를 진행 중이다.
Alarm Clock과 Priority Scheduling 관련 test case를 통과하기 위한 내 implementation을 정리해 보겠다.
이해를 위해 다시 적기보다는 그냥 결과 기록용이니 설명은 조금씩만 적겠다.(원리 설명은 구글링하면 잘 나옴)

먼저 결과창

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-result.png)
<!--more-->

# Alarm Clock

Busy waiting -> wake up when time comes
thread가 언제 일어나야 하는지 wakeup_tick에 저장하고 thread_block()
sleep_list 만들어서 timer_interrupt 때마다 wake_up_threads()를 호출하여 sleep_list 확인하면서 thread_unblock()

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-01.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-02.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-03.png)

# Priority Scheduling

## Scheduling 관련 함수

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-04.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-05.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-06.png)

ready_list에 우선도 순으로 insert한다.
thread_create()과 thread_set_priority(int new_priority)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-07.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-08.png)

이거 추가해서 priority 체크 후 preemption해야 하면 바로 thread_yield()

## Synchronization 관련 함수

### semaphore 관련 부분

sema->waiters 리스트를 우선도 정렬된 상태로 만들어야 하는데, 나는 insert 해주는 sema->value가 0일 때 sema_down() 함수는 그대로 두고, 원래는 pop_front를 해주던 sema_up에서 list_max로 max_elem을 뽑고, list_remove 한 후에 해당 스레드를 unblock 해줬다.
그리고, 이 경우에도 unblock으로 ready_list에 추가 되므로 thread_yield()가 따로 필요하다.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-09.png)

### condition 관련 부분

cond_wait에서 cond->waiters에 push_back 하고 cond_signal에서 뽑아주는데, 여기서도 cond_signal에서 뽑아줄 때 list_max로 뽑아줌.

**이 부분 내가 잘못 알았는데 cond->waiters의 element 1개에 해당되는 semaphore의 waiters(thread list)에는 thread가 1개씩만 있어서 마지막에 뽑는 부분을 list_front로 해도 된다고 함**

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-10.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-11.png)

### lock 관련 부분

lock_acquire(lock) 에서 lock 요구.
lock->holder의 priority가 자신보다 낮을 경우 holder의 priority를 자신의 priority로 바꿔줌.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-12.png)

그리고 바꾸는 동안
enum intr_level old_level;
old_level = intr_disable();
~
intr_set_level(old_level);
을 통해 interrupt 막아야함

thread->lock_wanted, lock->big_priority 추가하고
중간에서 lock_donation(lock)을 불러 일련의 과정을 따로 쓰자

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-13.png)

해당 lock의 holder가 없다면 donation 필요 없음.
lock->big_priority 보다 현재 priority가 크다면 덮어쓰기.
holder->priority가 lock->priority보다 작으면
holder->priority랑 original_priority 조정
그리고 holder가 대기 중인 다른 lock이 존재한다면, holder의 priority가 바뀌었으므로 그 lock에서도 donation을 recursive하게 부름.
lock->big_priority는 해당 lock을 원하는/갖는 모든 thread 중 가장 큰 priority


이제 lock_release(lock)로
holder가 사라지고 lock->semaphore를 sema_up 해줘야함
그리고 lock_donation_payback()으로 바뀐 priority를 원래대로 돌려줌.
lock_list가 thread가 가진 lock의 리스트이므로 일단 제거 후 lock_donation_payback()으로 들어가자

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-14.png)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-15.png)

lock_donation_payback()에서는
curr->original_priority가 존재하지 않는 경우 donation 받지 않았으므로 패스.
받았을 경우, 만약 lock_list가 없으면 다른 lock에서 priority를 받았을 리 없으니 curr->priority를 original_priority로 바꾸고 패스.
아니면, lock_list의 lock이 가진 가장 큰 big_priority와 현재 priority를 비교하여 original_priority보다 더 크면 그걸로 바꿈.
그 이후 lock_release()로 돌아와 lock의 big_priority 수정.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj1-16.png)

original_priority가 생겼으니 thread_set_priority 함수도 조정 필요.

**끝!**

그리고 내 pintos 코드는 Github에 올려 놓긴 했는데 아직 비공개고 수업 끝나면 공개로 전환할 예정.
