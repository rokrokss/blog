---
comments: true
title: Go Scheduler
key: 202001010
picture_frame: shadow
tags:
  - Go
---

[Dmitry Vyukov의 발표 영상](https://youtu.be/-K11rY57K7k)을 요약했다.

<!--more-->

Java thread의 갯수는 아무리 많아도 수만을 넘지 못하지만, Goroutine은 수백만을 유지할 수 있다.
어떻게 가능할까? 결론부터 말하자면 이유는 크게 두 가지로, 유저 스페이스에서 작동하는 M:N 스케줄러와 가변 스택 덕이다.

# Go Scheduler

> [소스코드](https://github.com/golang/go/blob/master/src/runtime/proc.go)

run queue로 관리
channel이 런타임에 제어되고 channel마다 wait queue가 따로 있으므로 전체적인 wait queue는 필요없음
system call 실행한 고루틴은 스레드가 해제되고, 기다리다가 반환 값이 왔을 때 run queue로 들어감

scalable?
- run queue에 global mutex가 있으면 scalable하지 않음
lock-free?
- losing context, cache 등등 퍼포먼스 저하

Disributed Scheduler
- kerenl thread마다 local run queue
- global run queue와 mutex 역시 존재하지만 특정 목적에서만 참조

poll order
- what is the next goroutine to run
- local run queue 체크하고 없으면 global run queue 체크, invoke the network poller, work stealing
- work stealing: 다른 local run queue에서 가져옴
=> scalability 성립

threads in syscalls?
- threads >> cores, work stealing할 때 체크할 곳이 너무 많음
- M:P:N threading

distributed 3-level scheduler
- local run queue, cache를 thread가 아닌 processor object로 옮김
- work stealing이 체크할 run queue의 수가 core 수와 동일해짐
=> efficiency 성립

Fairness?
- if a goroutine is runnable, it will run eventually
why?
- bad tail latencies, livelocks, pathological behaviors

Fair Scheduling
- ex) FIFO Run Queue
Fairness/Performance Tradeoff
- single run queue does not scale
- fifo bad for locality
-> want a minimal amount of fairness at a minimal cost!

Go uses time slice based preemption (~10ms)
- preempted goroutines go into global run queue(FIFO)

local queue = FIFO queue + 1-element LIFO buffer
- buffer for locality
- goroutine 1이 goroutine 2를 생성했을 때 stealing 당하지 않고 processor state을 그대로 이용해서 2를 실행하는 것이 좋다(locality)
- restrict other thread from stealing thread 1's goroutine for 3ms

그럼에도 gorouting 생성 실행이 반복될 경우 starvation 발생
time slice inheritance!
- time slice 안에 buffer에서 꺼내는게 반복되면 막고 preempt 시킨다.

Global Run Queue Starvation
- local run queue만 계속 확인하고 global run queue polling이 일어나지 않음
- schedTick variable이 있어서, 61번의 polling마다 local이 아닌 global run queue를 먼저 확인함
- why 61? => not too small, not too large, prime
- why prime? => hashmap의 사이즈를 정할 때와 비슷한 이유. pointer size의 배수가 되면 어플리케이션 패턴과 충돌이 있음.

Network Poller Starvation
- time slice가지고 핸들링할수도 있겠지만 network poller involves systemcall
- Solution: background thread poll network occasionally

Fairness Hierarchy
- Goroutine - preemption
- local run queue - time slice inheritance
- global run queue - check once in a while
- network poller - background thread
= minimal fairness at minimal cost



# Contiguous Stack

일반적으로 stack은 1~8mb (but stack is cheap, rsp 값을 바꿀 뿐이다.)

where is stack overflow check?
- 1 protected guard page

paging-based infinite stacks?
- lazy page-in
- 64bit virtual address space
- 1GB is infinite enough

paging won't work
- not enough address space
- 48bits CPU address space
- 1bit for kernel = 47 bits = 128TB
- 1GB 짜리 스택은 128K개 밖에 못 들어감
- 32bit system(ARM)
- 훨씬 적어짐
- performance
- releasing pages -> system call

split stack
- 1KB짜리 stack segment를 차례차례 할당한다.
cost
- normal function call ~2ns
- stack split ~60ns
빠른 forloop안에 함수 호출이 있을 경우 stack split의 영향이 너무 크다.
stack split이 일어나냐 안 일어나냐에 따라 좌지우지됨. non-transparent performance

Growable Stack
- allocates new large stack, copy the old stack and releases
- shrink when gc cycle

split stack
- O(1) cost per function call
- repeated
- worst case: stack split in hot loop
growable stack
- O(N) cost per function call
- amortized
- worst case: grow stack for short goroutine
Penalizing cheap operation a bit < penalizing expensive operation significantly
