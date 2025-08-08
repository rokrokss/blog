---
comments: true
title: Claude Code 텔레그램으로 알림 받기
key: 202508080
picture_frame: shadow
tags:
  - AI
  - 생산성
---

Claude Code가 작업할 때마다 실시간으로 텔레그램 알림을 받는 방법.

<!--more-->

## 배경

Claude Code는 강력하지만 장시간 작업 시 진행 상황을 파악하기 어려운 경우가 있습니다. 특히 대규모 리팩토링이나 복잡한 디버깅 작업 중에는 "지금 뭐하고 있는지", "멈춘 건 아닌지" 궁금할 때가 많습니다.

Claude Code Telegram Notification Hook은 이런 상황을 위한 간단한 솔루션입니다. Claude Code의 모든 작업을 텔레그램으로 실시간 알림받을 수 있습니다.

## 설치

### 준비물

| 도구 | 용도 | 비용 |
|------|------|------|
| **텔레그램** | 알림 수신 | 무료 |
| **Python 3** | Hook 스크립트 실행 | 무료 |
| **Claude Code** | AI 코딩 도구 | 구독 필요 |

### 1단계: 텔레그램 봇 생성

1. 텔레그램에서 [@BotFather](https://t.me/botfather) 검색
2. `/newbot` 명령어 입력
3. 봇 이름과 username 설정
4. 생성된 봇 토큰 저장 (형식: `1234567890:ABCdefGHI...`)

### 2단계: Chat ID 확인

#### 방법 1: UserInfoBot 사용
[@userinfobot](https://t.me/userinfobot)에게 메시지 전송 → ID 확인

#### 방법 2: API 직접 호출
1. 생성한 봇에게 아무 메시지 전송
2. 브라우저에서 접속:
   ```
   https://api.telegram.org/botYOUR_TOKEN/getUpdates
   ```
3. JSON 응답에서 `"chat":{"id":YOUR_ID}` 확인

### 3단계: Hook 설치

```bash
# 저장소 클론
git clone https://github.com/rokrokss/claude-code-telegram-notify-hook.git
cd claude-code-telegram-notify-hook

# 환경변수 설정
export CC_HOOK_TELEGRAM_BOT_TOKEN="your_bot_token"
export CC_HOOK_TELEGRAM_CHAT_ID="your_chat_id"

# Hook 파일 복사
cp -r .claude ~/.claude

# 실행 권한 부여
chmod +x ~/.claude/hooks/notification.py
```

### 4단계: 작동 확인

```bash
# 테스트 메시지 전송
curl -X POST "https://api.telegram.org/botYOUR_TOKEN/sendMessage" \
     -d "chat_id=YOUR_CHAT_ID" \
     -d "text=Hook 설치 완료!"
```

메시지가 도착하면 설정 완료입니다.

## 알림 형식

Claude Code가 작업할 때마다 다음과 같은 형식의 알림을 받습니다:

```
🤖 Project: my-awesome-project
⏰ 2025-01-08 15:30:45
✅ Event: File Edit
📁 Path: src/components/Header.tsx
📌 Stop Hook Active: false
```

## 주요 기능

### 지원 이벤트

| 이벤트 | 설명 | 활용 |
|--------|------|------|
| **Notification** | 일반 작업 알림 | 전체 작업 흐름 파악 |
| **Stop** | 작업 완료 | 작업 종료 시점 확인 |
| **SubagentStop** | 서브 에이전트 완료 | 병렬 작업 추적 |
| **File Operations** | 파일 편집/생성/삭제 | 코드 변경사항 추적 |
| **Terminal Commands** | 명령어 실행 | 빌드/테스트 상태 확인 |

### 활용 예시

#### 1. 장시간 리팩토링
대규모 코드베이스 리팩토링 시 진행 상황을 실시간으로 확인할 수 있습니다. 다른 작업을 하면서도 모바일로 진행도를 체크할 수 있어 효율적입니다.

#### 2. 디버깅 과정 추적
Claude Code가 어떤 파일을 분석하고 수정하는지 추적하여 디버깅 과정을 이해하고 학습할 수 있습니다.

#### 3. 팀 협업
팀 텔레그램 채널에 봇을 추가하면 Claude Code의 작업을 팀원들과 실시간으로 공유할 수 있습니다.

## 고급 설정

### 환경변수 영구 설정

`.bashrc` 또는 `.zshrc`에 추가:

```bash
export CC_HOOK_TELEGRAM_BOT_TOKEN="your_bot_token"
export CC_HOOK_TELEGRAM_CHAT_ID="your_chat_id"
```

### 그룹 채팅 연동

1. 봇을 그룹에 초대
2. 그룹 Chat ID 확인 (음수로 시작: `-1001234567890`)
3. 해당 ID로 환경변수 설정

### 필터링 커스터마이징

특정 이벤트만 알림받으려면 `notification.py` 수정:

```python
# 예: 파일 작업만 알림
if event_type in ['FileEdit', 'FileCreate', 'FileDelete']:
    send_telegram_message(message)
```

## 문제 해결

| 문제 | 해결 방법 |
|------|-----------|
| **알림이 오지 않음** | 토큰/ID 확인, 봇과 대화 시작 여부 확인 |
| **권한 오류** | `chmod +x ~/.claude/hooks/notification.py` 실행 |
| **토큰 오류** | 토큰을 정확히 복사했는지 확인 (대소문자 구분) |
| **그룹 채팅 실패** | 음수 Chat ID 사용, 봇 관리자 권한 확인 |

## 보안 주의사항

- 토큰을 절대 공개 저장소에 커밋하지 마세요
- `.env` 파일을 `.gitignore`에 추가하세요
- 토큰이 노출되면 BotFather의 `/revoke` 명령으로 즉시 재발급하세요

## 마무리

간단한 Hook 설정으로 Claude Code의 작업을 실시간으로 모니터링할 수 있습니다. 특히 모바일 환경에서 작업 진행 상황을 확인하고 싶을 때 유용한 도구입니다.

전체 소스 코드: [GitHub 저장소](https://github.com/rokrokss/claude-code-telegram-notify-hook)
