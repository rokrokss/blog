---
layout: post
comments: true
title: Pintos Project 2&#58; User Programs
key: 201804221
modify_date: 2018-04-22
picture_frame: shadow
tags:
  - OS
  - Pintos
---

OS수업에서 Pintos 프로젝트를 진행 중이다.
User Programs 관련 test case를 통과하기 위한 내 implementation을 정리해 보겠다.

이번 과제는 좀 복잡해서 작동원리를 이해하기 위한 순서로 code를 설명하면 답이 없으므로, 그냥 code만 가지고 보여주겠다.

일단 결과창(test 76개 통과하는 그거 맞다. make check 후 make grade? 하면 이런 식으로 나옴.)

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-result.png)

<!--more-->

# process.c

process.c와 syscall.c를 중심으로 수정하면 되는데, 먼저 process.c

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-01.png)

- fn_copy, fn_copy2를 만들어가며 file name을 token으로 뽑아내 thread_create으로 전달한다.
- token으로 file open해봐서 NULL이면 load error
- thread_create하고 나서 sema_up(load_sema)를 불러 load가 끝났다고 signal 하는데, 이건 syscall의 system_exec에서 기다리는 중.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-02.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-03.png)

- 전달받은 file_name_(앞의 thread_create에서 전달된 fn_copy)를 잘라서 file_name을 뽑아주고, load함수에 token_ptr을 추가로 전달해서 argument parsing할 준비.
- load 끝난 후 success에 따라서 load 상태 저장하고 load_sema signal

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-04.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-05.png)

- thread_child는 wait을 위한 새로운 구조체.
- process_exit에서 sema_up함.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-06.png)

- fd_list의 file 닫고.
- executable(load 때 추가해주는 해당 thread의 실행 파일)도 닫아줌.
- wait에서 기다리고 있는 sema_up

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-07.png)

중략

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-08.png)

- file 연 후에 deny_write 적용
- argument_setup이란 새로운 함수가 stack에 argument 넣어줌
- success 시에 t->executable에 달아준 file은 process exit에서 close해준다.
- success 아니면 file 닫아줌

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-09.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-10.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-11.png)

- load의 setup stack이후 요리조리 argument를 stack에 넣어줌


# syscall.c

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-12.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-13.png)

- file 관련 함수 쓸 때 사용할 lock 정의하고 syscall_init 때 lock_init함.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-14.png)

- syscall_handler에서 get_argument로 argument를 받아옴.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-15.png)

- 요로코롬 esp 주소 valid한 지 체크도 해주면서 함수마다 해당하는 argc만큼 가져다 넣음

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-16.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-17.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-18.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-19.png)
![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-20.png)

- 얘네는 너무 많아서 다 설명하긴 귀찮음.
- wait은 process.c의 wait이 다 처리해줌.
- exec에서 load_sema를 기다리며 제대로 load됐는지 확인함.
- create이나 read처럼 주소를 argument로 사용하는 경우 해당 주소가 valid한 지 체크해야함.

![text](https://raw.githubusercontent.com/q0115643/my_blog/master/images/pintos-pj2/pintos-pj2-21.png)

- thread.h에서 thread에 fd_list, fd_count 같은 것들 추가해 놓고 사용함.


**끝!**

그리고 내 pintos 코드는 Github에 올려 놓긴 했는데 아직 비공개고 수업 끝나면 공개로 전환할 예정.

[https://github.com/q0115643/CS330_OS_Pintos](https://github.com/q0115643/CS330_OS_Pintos)
