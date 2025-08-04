---
comments: true
title: 모바일로 Claude Code 사용하는 법
key: 202507300
picture_frame: shadow
tags:
  - AI
  - 생산성
---

바이브코더가 되는 방법...

<!--more-->

# 1: vibetunnel + cloudflared

![vibetunnel](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/vibetunnel/0.png)

간단하게 말하면 컴퓨터의 터미널을 웹으로 컨트롤 할 수 있도록 로컬에 띄우고, cloudflared를 통해 외부 접근을 열어서 폰으로 접근하는 방식입니다.

SSH와 근본적으로 같지만 웹뷰에 맞춘 줄바꿈과 세션 관리 메뉴가 있어서 사용성이 좋습니다.

## 설치

1. [vibetunnel](https://vibetunnel.sh/) 툴을 설치합니다.
2. vibetunnel 실행 후 설명에 따라 사용할 터미널 앱을 선택합니다.

## 설정

1. vibetunnel 설정창의 **Remote 탭**에서 cloudflared를 설치하고 자동 연동 버튼을 클릭합니다.
2. 연동하면 Public URL이 생성됩니다.
3. vibetunnel 앱에서 세션을 생성합니다.
4. 모바일에서 해당 URL로 접근하여 컴퓨터 비밀번호를 입력합니다.

> ⚠️ **주의**: 최근 업데이트 이후 vibetunnel의 사용성이 매우 안 좋아졌습니다.

# 2: tailscale + termius

![terminus](https://raw.githubusercontent.com/rokrokss/blog/master/assets/images/vibetunnel/1.jpeg)

vibetunnel 방식에서 웹뷰 품질 이슈가 심각해서 더 나은 방법을 찾았습니다.

웹뷰 품질 이슈 없이 네이티브 SSH UX를 그대로 사용하고, 모바일 특유의 끊김에도 작업이 안 날아가도록 tmux로 세션을 붙잡는 조합입니다. 

- **Tailscale**: 아이폰↔맥 사이에 안전한 P2P 경로만 제공 (VPN 역할)
- **실제 로그인**: 맥의 OpenSSH로 이루어집니다
- **Tailscale SSH** 같은 부가 기능 없이도 동작합니다

## 준비물

| 도구 | 플랫폼 | 용도 | 비용 |
|------|--------|------|------|
| **Tailscale** | 맥·아이폰 | VPN 연결 (같은 계정으로 로그인) | 무료 |
| **Termius** | iOS | SSH 클라이언트 (Starter) | 무료 |
| **tmux** | 맥 | 세션 유지용 | 무료 (오픈소스) |

## 설치 및 설정

### 1) 맥: SSH 서버 및 tmux 설정

#### 원격 로그인(SSH) 켜기
- **GUI 방법**: 시스템 설정 → 일반 → 공유 → 원격 로그인 On
- **CLI 방법**:
```bash
sudo systemsetup -setremotelogin on
```

#### tmux 설치
```bash
brew install tmux
```

#### (권장) 공개키 인증만 허용
`/etc/ssh/sshd_config`에 아래 설정 확인 후 재시작:

```bash
PubkeyAuthentication yes
PasswordAuthentication no
```

재시작 명령:
```bash
sudo launchctl kickstart -k system/com.openssh.sshd
```
### 2) Tailscale 연결

1. 맥·아이폰에서 Tailscale 로그인
2. Connected 상태 유지

맥에서 Tailscale IP 확인:
```bash
tailscale ip -4    # 예: 100.86.12.34
```

> 💡 **팁**: MagicDNS를 켜면 `맥이름.tailnet.ts.net` 같은 이름으로도 접속 가능합니다.

### 3) Termius(iOS) 세팅

#### SSH 키 생성
1. **Keychain → + → Generate key (ED25519)**로 키 생성
2. **Public key** 복사

#### 맥에 공개키 등록
```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys   # 공개키 한 줄 붙여넣기
chmod 600 ~/.ssh/authorized_keys
```

#### Host 프로필 생성
- **Hostname**: 맥의 Tailscale IP (예: `100.86.12.34`) 또는 MagicDNS 호스트
- **Port**: `22`
- **User**: 맥 계정명
- **Auth**: 방금 만든 Private key

#### (강추) Startup Command 설정
아래 명령을 Startup Command에 입력:
```bash
tmux attach -t main || tmux new -s main
```
→ 접속할 때마다 기존 세션에 자동 접속하거나 없으면 새로 생성

### 4) tmux 미니 설정 (모바일 친화적)

`~/.tmux.conf` 파일 생성:

```tmux
set -g mouse on
set -g history-limit 50000
set -g escape-time 0
setw -g mode-keys vi

# iOS에서 Ctrl 조작 편의
set -g prefix C-a
unbind C-b
bind C-a send-prefix

# 창 분할 단축키 단순화
unbind '"'
unbind %
bind - split-window -v
bind | split-window -h

# 256color/Truecolor
set -g default-terminal "tmux-256color"
set -ga terminal-overrides ",xterm-256color:RGB"
```

설정 적용:
```bash
tmux source-file ~/.tmux.conf
```
또는 세션 재생성

## 사용 흐름

1. 아이폰에서 **Tailscale ON**
2. **Termius**로 Host 접속
3. (Startup Command로) **tmux 자동 attach/new**

> 💡 **핵심**: iOS가 백그라운드로 내려가거나 네트워크가 바뀌어도 tmux 세션은 맥에서 유지됩니다. 재접속 시 즉시 이어서 작업 가능!

## 문제 해결 체크리스트

연결이 안 될 때 확인할 사항들:

- [ ] 아이폰 Tailscale이 **ON** 상태인지 (꺼져 있으면 100.x 대역 라우팅 불가)
- [ ] `tailscale status` (맥)에서 아이폰이 보이는지 확인
- [ ] 맥 자체 테스트: `ssh localhost` 또는 `ssh user@100.x.x.x`
- [ ] `sshd_config` 수정 후 `kickstart`로 재시작했는지
- [ ] 방화벽에서 SSH 허용 팝업을 승인했는지

## 비용 정보

| 서비스 | 플랜 | 비용 | 제한사항 |
|--------|------|------|----------|
| **Tailscale** | Personal | 무료 | 개인 사용 충분, 계정별 기기/사용자 한도 존재 |
| **Termius** | Starter | 무료 | 개인·상업적 사용 가능, Pro/Team/Business는 유료 |
| **tmux** | - | 무료 | 오픈소스 |

> 🎯 **요약**: **Tailscale Personal + Termius Starter + tmux = 0원** 조합으로 안정적인 모바일 원격 터미널 환경을 구축할 수 있습니다. 필요시 Termius Pro(동기화·스니펫 등)만 선택적으로 추가하면 됩니다.

## 사용

이제 터미널을 모바일로 제어할 수 있어 혼밥하면서 클로드코드에게 일시키는 바이브코더가 됩니다.
