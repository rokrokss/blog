---
comments: true
title: Claude Squad 사용법
key: 202507292
picture_frame: shadow
tags:
  - AI
  - 생산성
---

멀티 클로드코드 툴 [클로드스쿼드](https://github.com/smtg-ai/claude-squad)의 사용법 정리글입니다.

<!--more-->

# Claude Squad: AI 어시스턴트 병렬 관리 시스템

## 빠른 시작

### 실행
```bash
cs
```

### 주요 단축키
| 키 | 기능 |
|---|---|
| `n` | 새 세션 생성 |
| `N` | 프롬프트와 함께 새 세션 생성 |
| `↵` | 세션 연결 |
| `ctrl-q` | 세션 분리 |
| `s` | 커밋 및 푸시 |
| `c` | 체크아웃 |
| `tab` | Preview/Diff 전환 |
| `D` | 세션 종료 |
| `↑/j`, `↓/k` | 세션 간 이동 |
| `shift-↑/↓` | Diff 뷰 스크롤 |
| `q` | 애플리케이션 종료 |

### 워크플로우 예시

**병렬 작업 시나리오:**

1. 기능 개발 세션 시작
   ```
   cs
   N → "Add user authentication API"
   ```

2. 긴급 버그 수정 필요 시
   ```
   ctrl-q  # 현재 세션 백그라운드 전환
   N → "Fix critical payment bug"
   ```

3. 버그 수정 완료 후
   ```
   s  # 변경사항 푸시
   ↑  # 이전 세션으로 이동
   ↵  # 기능 개발 재개
   ```

## 개요

Claude Squad는 다수의 AI 코딩 어시스턴트를 동시에 관리하고 조율하는 터미널 기반 애플리케이션입니다. 각 AI 세션을 독립된 작업 공간에서 실행하여 병렬 개발 워크플로우를 지원합니다.

### 지원 AI 어시스턴트
- Claude Code (기본값)
- OpenAI Codex
- Google Gemini
- Aider
- CLI 기반 AI 도구

## 설치

### 시스템 요구사항
- tmux
- gh (GitHub CLI)

### 설치 방법

**Homebrew:**
```bash
brew install claude-squad
ln -s "$(brew --prefix)/bin/claude-squad" "$(brew --prefix)/bin/cs"
```

**수동 설치:**
```bash
curl -fsSL https://raw.githubusercontent.com/smtg-ai/claude-squad/main/install.sh | bash
```

## 핵심 기능

### 1. 멀티 세션 관리
최대 10개의 AI 세션을 동시 실행 및 관리. 각 세션은 독립적으로 작동하며 실시간 전환 가능.

### 2. Git 워크트리 격리
각 세션은 별도의 git 브랜치에서 작업. 코드 충돌 없이 병렬 개발 가능.

```
main
├── feature/api-endpoint (세션 1)
├── refactor/ui-components (세션 2)
└── hotfix/production-bug (세션 3)
```

### 3. 실시간 변경사항 추적
Preview/Diff 탭을 통한 코드 변경 실시간 모니터링. 즉각적인 커밋 또는 수정 가능.

## 고급 활용

### Auto-Accept 모드
```bash
cs -y  # 자동 승인 모드로 실행
```

### 다중 AI 모델 활용
```bash
cs -p "claude"  # Claude 세션
cs -p "aider --model gpt-4"  # GPT-4 세션
```

### 설정 관리
```bash
cs debug  # 설정 파일 경로 확인
```

## 제약사항

- 최대 10개 세션 동시 실행
- 각 세션은 독립 프로세스로 실행 (메모리 고려 필요)
- 다중 AI 사용 시 API 비용 증가

## 기술 아키텍처

- **터미널 UI**: Bubble Tea 프레임워크
- **세션 관리**: tmux 기반 격리
- **버전 관리**: git 워크트리를 활용한 브랜치 격리
- **상태 관리**: 각 세션의 독립적 상태 유지

## 결론

Claude Squad는 AI 어시스턴트의 병렬 활용을 통해 개발 생산성을 극대화하는 도구입니다. 컨텍스트 스위칭 없이 여러 작업을 동시에 진행하고, 각 작업에 최적화된 AI 모델을 선택하여 효율적인 개발 워크플로우를 구현할 수 있습니다.

---

**참고 자료**
- [GitHub 저장소](https://github.com/smtg-ai/claude-squad)
- [공식 문서](https://smtg-ai.github.io/claude-squad/)
