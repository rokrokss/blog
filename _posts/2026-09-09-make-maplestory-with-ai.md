---
comments: true
title: "“메이플스토리 만들어줘”: Astra, Fable, Opus 5.5, Meshy AI"
description: "Astra, Fable, Opus 5.5에 같은 프롬프트로 메이플스토리풍 게임을 만들어 달라고 요청했습니다. 제작 시간·플레이 경험을 비교하고 Meshy AI로 3D를 구현한 과정을 기록합니다."
key: 202609090
permalink: /post/2026/09/09/make-maplestory-with-ai.html
modify_date: 2026-09-24
picture_frame: shadow
excerpt: Astra와 Fable에 같은 요청을 해봤다.
image: "/assets/images/maplestory-ai/astra-meshy-3d.jpg"
tags:
  - AI
  - LLM
  - Prototyping
mathjax: false
mermaid: false
chart: false
image_alt: "Astra와 Meshy AI로 구현한 메이플스토리풍 3D 게임 화면"
---

Astra와 Fable에 같은 요청을 해봤다.

<!--more-->

2D 결과를 비교한 뒤에는 fal.ai의 fal MCP를 연결하고, Meshy를 사용해 3D로 바꿨다.

## 시작은 한 문장

> 싱글플레이로 브라우저에서 바로 플레이할 수 있는 메이플스토리를 만들어줘.

effort 설정은 모두 xhigh로, **각각 새 빈 프로젝트에서 한 번의 프롬프트로 실행했다(one-shot).** 공식 에셋 조건은 기본 프롬프트 끝에 “공식 에셋을 가져다 써”를 덧붙여 함께 입력했다. 5번은 2번 결과를 바탕으로 진행했다.

공식 에셋을 쓰라고 요청한 경우에도, 작업 과정을 지켜보니 GitHub의 오픈소스 프로젝트를 많이 참고하는 것으로 보였다.

## 1번: Astra 기본 요청

**20분 · 주간 한도 1% 미만**

이미지 생성을 따로 지시하지 않았는데도 **Codex가 GPT Image로 자체 에셋을 만들어 채웠다.** [OpenAI의 이미지 생성 도구 문서](https://developers.openai.com/api/docs/guides/tools-image-generation)에 따르면, 메인 모델이 `image_generation` 호출 여부와 프롬프트를 정하고 별도의 GPT Image 모델이 이미지를 만든다.

작은 범위라도 이동하고 몬스터를 상대하며 게임을 진행할 수 있었고 버그라고 느껴지는 것은 없었다.

<figure style="margin:2rem 0;">
  <video controls playsinline preload="none" poster="{{ '/assets/images/maplestory-ai/astra-2d.jpg' | relative_url }}" aria-label="Astra xhigh로 20분 동안 만든 2D 게임 플레이 영상" width="1280" height="970" style="display:block;width:100%;height:auto;background:#111;border-radius:8px;">
    <source src="{{ '/assets/videos/maplestory-ai/astra-2d.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/videos/maplestory-ai/astra-2d.mp4' | relative_url }}">Astra의 2D 게임 플레이 영상 보기</a>
  </video>
  <figcaption>Astra · 기본 요청 · 20분</figcaption>
</figure>

## 2번: Astra + 공식 에셋

**27분 · 주간 한도 1% 미만**

공식 에셋 사용 조건으로 새로 생성했다.

<figure style="margin:2rem 0;">
  <video controls playsinline preload="none" poster="{{ '/assets/images/maplestory-ai/astra-2d-official-assets.jpg' | relative_url }}" aria-label="Astra에 공식 에셋 사용을 요청해 27분 동안 만든 2D 게임 플레이 영상" width="1280" height="1098" style="display:block;width:100%;height:auto;background:#111;border-radius:8px;">
    <source src="{{ '/assets/videos/maplestory-ai/astra-2d-official-assets.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/videos/maplestory-ai/astra-2d-official-assets.mp4' | relative_url }}">Astra의 공식 에셋 요청 결과 영상 보기</a>
  </video>
  <figcaption>Astra · 공식 에셋 사용 요청 · 27분</figcaption>
</figure>

## 3번: Fable 5.1 기본 요청

**25분 · 주간 한도 대략 2%**

같은 기본 요청에 단순한 도형 위주의 화면이 나왔다. 에셋은 더미 이미지 수준이었다. 이미지 생성을 명확히 요구했을 때의 결과는 이번에 확인하지 않았다.

<figure style="margin:2rem 0;">
  <video controls playsinline preload="none" poster="{{ '/assets/images/maplestory-ai/fable-2d.jpg' | relative_url }}" aria-label="Fable 5.1 기본 요청으로 25분 동안 만든 2D 게임 플레이 영상" width="1280" height="962" style="display:block;width:100%;height:auto;background:#111;border-radius:8px;">
    <source src="{{ '/assets/videos/maplestory-ai/fable-2d.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/videos/maplestory-ai/fable-2d.mp4' | relative_url }}">Fable의 기본 요청 결과 영상 보기</a>
  </video>
  <figcaption>Fable 5.1 · 기본 요청 · 25분</figcaption>
</figure>

## 4번: Fable 5.1 + 공식 에셋

**44분 · 주간 한도 대략 2%**

공식 에셋 사용 조건에서는 원작과 아주 흡사한 결과물이 나왔다. Astra보다 규모가 크고 때깔도 좋았다. 이미 구현된 월드를 많이 가져온 것 같지만, 확실하지는 않다.

다만 벽이 아닌 곳에서 캐릭터가 움직이지 못하는 버그가 있었다. 몬스터가 있는 맵과 시작 장소의 방향도 반대여서, 만들어진 것들을 경험하기까지의 동선이 아쉬웠다.

<figure style="margin:2rem 0;">
  <video controls playsinline preload="none" poster="{{ '/assets/images/maplestory-ai/fable-2d-official-assets.jpg' | relative_url }}" aria-label="Fable 5.1에 공식 에셋 사용을 요청한 2D 게임 플레이 영상" width="1280" height="1002" style="display:block;width:100%;height:auto;background:#111;border-radius:8px;">
    <source src="{{ '/assets/videos/maplestory-ai/fable-2d-official-assets.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/videos/maplestory-ai/fable-2d-official-assets.mp4' | relative_url }}">Fable의 공식 에셋 요청 결과 영상 보기</a>
  </video>
  <figcaption>Fable 5.1 · 공식 에셋 사용 요청 · 44분</figcaption>
</figure>

## 5번: Astra + Meshy AI로 3D 전환

**약 2시간 30분 · 주간 한도 약 12%**

3D 전환에서는 모델링이 병목이었다. Blender MCP를 연결해도 원하는 외형이 잘 나오지 않아, Astra에 **fal.ai의 fal MCP**를 연결했다.

주황버섯을 **Meshy, Tripo, Hunyuan**으로 각각 만들어 간단히 눈으로 비교했다. Meshy의 결과가 더 나아 보여 이를 선택하고, 2번에서 만든 게임을 다음 요청으로 확장했다.

> 2번에서 만든 게임을 3D로 재개발해줘. 컨셉아트를 생성하고 Meshy AI를 이용해서 구현체가 최대한 컨셉아트에 가깝게 만들어줘.

<figure style="margin:2rem 0;">
  <video controls playsinline preload="none" poster="{{ '/assets/images/maplestory-ai/astra-meshy-3d.jpg' | relative_url }}" aria-label="Astra와 Meshy로 재개발한 3D 메이플스토리풍 게임 플레이 영상" width="1280" height="708" style="display:block;width:100%;height:auto;background:#111;border-radius:8px;">
    <source src="{{ '/assets/videos/maplestory-ai/astra-meshy-3d.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/videos/maplestory-ai/astra-meshy-3d.mp4' | relative_url }}">Astra와 Meshy의 3D 게임 플레이 영상 보기</a>
  </video>
  <figcaption>Astra + Meshy AI · 기존 2D 결과를 3D로 재개발 · 약 2시간 30분</figcaption>
</figure>

버섯집과 나무, 캐릭터가 입체적인 모습으로 나왔다. 외부 생성 모델 없이 만들었을 때는 위 영상의 NPC 모델 정도가 결과였다. **Blender를 연결해도 남았던 모델링 문제를 3D 생성 특화 모델이 메워줬다.**

[OpenAI의 Astra 건축 시각화 사례](https://developers.openai.com/blog/architectural-visualization-with-astra)에서는 Blender Python API인 `bpy`로 건물과 가구를 만들고, 숲에는 Poly Haven의 에셋을 가져다 쓴다. 렌더링을 보며 수정하고 추가 요청으로 집을 확장하기도 한다. 이런 장면 구성과 내 실험에서 막힌 주황버섯의 형상 생성은 구분해서 볼 필요가 있었다.

## 규모와 때깔보다 게임 경험

이 비교에서는 화면의 완성도와 실제로 플레이를 이어갈 수 있는지를 따로 봐야 했다.

2026년 8월 공개된 [GameXpert-Bench](https://arxiv.org/html/2608.21833v1#S4.SS3)에서 눈에 들어온 것도 **시각적 품질과 플레이 경험을 별개의 평가 항목으로 둔 것**이다. 기능은 코드를 읽는 데서 끝내지 않고, 실제 실행에서 해당 동작이 나타나야 점수를 준다. Fable 결과를 스크린샷으로 봤을 때와 직접 조작했을 때의 평가가 달랐던 내 경험과 맞닿아 있었다.

## Blender의 움직임을 영상으로 완성하기

위 실험에 쓰이진 않았지만 관련해서 흥미로운 활용법이 Blender와 Seedance의 조합이다. **게임에 넣기에는 아쉬웠던 더미 3D도 영상의 움직임과 카메라 구도를 잡는 데는 쓸 수 있다.**

2026년 7월 31일 공개된 [Seedance 2.5 공식 소개](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)의 **clay render 참조** 예시가 이 방식이다. 카메라 움직임·동선·타이밍은 재질 없는 3D 렌더 영상을, 캐릭터 외형·재질·조명은 별도 이미지를 참조하도록 지시한다.

움직임을 수정하려면 Blender에서 캐릭터 위치와 카메라 경로를 고쳐 다시 렌더링하면 된다.

### ComfyUI에서 Seedance 연결하기

[ComfyUI의 공식 Seedance 2.5 R2V 워크플로우](https://comfy.org/workflows/cd0c4f9f61a4-cd0c4f9f61a4/)에서는 이 두 참조를 `ByteDance2ReferenceNode`에 넣고, 생성 결과를 `SaveVideo`로 저장하는 구성을 사용할 수 있다.

### Higgsfield Genjutsu와 Blender 애드온

[Higgsfield Genjutsu의 Motion Transfer](https://higgsfield.ai/genjutsu)는 원본 영상의 움직임·카메라·타이밍을 참조해 새 캐릭터와 장면으로 재구성하는 기능이다. 여기에도 같은 입력 구성을 적용해볼 수 있다.

별도로 [Higgsfield Blender 애드온](https://higgsfield.ai/blog/higgsfield-blender-plugin)은 뷰포트에서 Seedance 2.5 영상을 생성하는 기능을 제공한다. Blender Bridge MCP를 통해 에이전트가 현재 열린 장면을 구성하는 것도 지원한다.

<figure style="margin:2rem 0;">
  <a href="{{ '/assets/images/maplestory-ai/game-and-video-pipelines.svg' | relative_url }}"><img src="{{ '/assets/images/maplestory-ai/game-and-video-pipelines.svg' | relative_url }}" alt="게임 제작은 fal MCP를 통해 Meshy를 호출해 컨셉 이미지에서 메시를 만든 뒤 엔진에서 입력과 충돌을 구현한다. 영상 제작은 Blender에서 동선과 카메라를 정한 참조 영상에 컨셉 이미지를 더하고 ComfyUI의 Seedance 또는 Genjutsu Motion Transfer로 완성한다." width="1040" height="760" loading="lazy" style="display:block;width:100%;height:auto;"></a>
  <figcaption>공식 기능을 바탕으로 구성한 작업 예시. ComfyUI의 Seedance 연동과 Genjutsu의 영상 변환을 각각 표시했다.</figcaption>
</figure>

## 결론: 작게라도 게임 경험을 완성한 쪽

이번 비교에서 더 높게 평가한 쪽은 Astra다. Fable은 더 크고 때깔 좋은 결과를 만들었지만 버그가 플레이를 막았고, Astra는 작아도 게임을 이어갈 수 있었다. **“게임 경험”의 측면에서 get shit done한 쪽은 Astra였다.** 이미지 생성을 따로 요청하지 않아도 에셋까지 채워준 점도 좋았다.

3D에서는 Blender를 다루는 것만으로 원하는 캐릭터 외형까지 해결되지는 않았다. Meshy를 쓰면서 결과가 나아졌고, **이번 실험에서는 3D 생성 특화 모델이 여전히 필요했다.**

직접 시도하지는 않았지만, 더미 3D로 움직임과 카메라를 잡고 Seedance에 외형을 맡기는 영상 제작 방식도 흥미로웠다. **게임에 넣기에는 아쉬웠던 모델도 영상의 움직임을 제어하는 입력으로는 쓸모가 있다.**

## 6번: Opus 5.5 기본 요청

**1시간 · 주간 한도 약 4%**

같은 기본 요청을 Claude Code의 Opus 5.5에 xhigh로 입력했다. 1~4번과 마찬가지로 새 빈 프로젝트에서 한 번의 프롬프트로 실행했다.

이미지 파일을 하나도 쓰지 않고 **캐릭터·몬스터·배경을 모두 Canvas 코드로 그렸다.** 효과음과 배경음악 6곡도 Web Audio로 합성했다. 웹 검색 없이 원작의 요소를 기억에 기대어 재구성했다고 설명했고, 원작 고유명인 머쉬맘은 “버섯 대왕”으로 바꿔 넣었다.

<figure style="margin:2rem 0;">
  <video controls playsinline preload="none" poster="{{ '/assets/images/maplestory-ai/opus-2d.jpg' | relative_url }}" aria-label="Opus 5.5 기본 요청으로 1시간 동안 만든 2D 게임 플레이 영상" width="1280" height="964" style="display:block;width:100%;height:auto;background:#111;border-radius:8px;">
    <source src="{{ '/assets/videos/maplestory-ai/opus-2d.mp4' | relative_url }}" type="video/mp4">
    <a href="{{ '/assets/videos/maplestory-ai/opus-2d.mp4' | relative_url }}">Opus 5.5의 기본 요청 결과 영상 보기</a>
  </video>
  <figcaption>Opus 5.5 · 기본 요청 · 1시간</figcaption>
</figure>

1번 결과가 숲 하나와 몬스터 두 종, 보스로 이루어졌다면, 6번은 맵 6개를 포탈로 잇고 밧줄과 사다리를 넣었다. 몬스터 11종과 보스, 1차 전직 4종과 스킬 19개, 장비·인벤토리·상점, 연속 퀘스트 6개까지 레벨 20 전후의 한 사이클을 담았다.

작업 방식에서 눈에 띈 것은 검증이었다. 코드를 작성한 뒤 **헤드리스 Chrome을 띄워 캐릭터 생성부터 보스전까지 스스로 조작해 보고**, 게임 루프를 빠르게 돌리는 사냥 봇으로 레벨 구간별 사냥 속도를 재며 밸런스를 조정했다. 이 과정에서 레벨 1 공격이 1~4 데미지에 그치는 문제와, 공격 모션 중에 누른 버프 키가 무시되는 버그를 찾아 고쳤다.

## 추가 결론: 실행해 보며 다듬은 쪽

Opus 5.5는 앞선 결론의 기준인 “게임 경험”을 작업 과정 안에서 확인했다. 기능을 실제 실행으로 평가하는 GameXpert-Bench의 방식과 닮은 부분이다.

대신 비용이 더 들었다. 1~4번이 20~44분, 주간 한도 2% 이하였던 데 비해 6번은 1시간, 약 4%였다. 이미지 생성을 쓰지 않아 그림은 코드로 그린 벡터 그래픽에 머물렀다.

**같은 한 문장에도 모델마다 먼저 채우는 것이 달랐다.** Astra는 이미지 생성으로 에셋을, Fable은 공식 에셋 조건에서 규모와 때깔을, Opus 5.5는 시스템의 범위와 실행 검증을 먼저 채웠다.

### 고질적인 문제는 어디까지 나아졌나

Claude에는 끝내지 못한 작업을 끝났다고 보고하는 문제가 있었다. Anthropic은 [Opus 5.5를 소개하며](https://www.anthropic.com/claude-opus-5-5) 정직성 지표 대부분에서 가장 강한 모델이라고 밝혔다. [시스템 카드](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf)의 자동 행동 감사에서 **거짓 완료 주장(False completion claims) 점수는 Opus 5의 1.56에서 1.14로 내려가, 비교한 모델 중 가장 낮았다**(1~10점, 낮을수록 좋음). 이번 실험에서도 Opus 5.5는 완료를 알리면서, 사람이 직접 오래 플레이해 보지는 않았다는 점과 모바일 조작이 없다는 점을 함께 밝혔다.

다만 해결됐다고 보기는 이르다. 같은 시스템 카드에 따르면 사내 사용을 초기에 거칠게 분석했을 때 작업 범위를 부풀리는 사례가 이전 모델보다 늘었고, 확인하지 않은 추론을 사실처럼 단정하는 문제가 여전히 가장 많았다. 디버깅이 나아졌다는 이야기도 실제 장애의 근본 원인을 찾는 사내 평가(CoBench 2.1)에서는 확인되지 않았다. Opus 5.5가 55.8%, Opus 5가 53.2%로 노이즈 범위 안이었다.

GPT 쪽에서는 Astra의 과잉설계가 꾸준히 지적됐다. Astra를 프로덕션에서 미리 써 본 [Kilo](https://blog.kilo.ai/p/gpt-6-astra-what-we-learned-previewing)는 작은 수정을 요청해도 거대한 변경을 돌려준다고 했다. [Theo(t3.gg)의 비교](https://daily.dev/posts/fable-vs-astra-debate-is-over-vurvocilp)에서도 Astra의 결과물은 Fable 5.1보다 머지 전 후속 수정이 세 배 정도 필요했다. 벤치마크에서 비슷하거나 앞서도 Fable에 머무르는 사람들이 있었던 이유다. 반대로 직접 비교에서 Astra가 더 많이 이겼다는 [MindStudio의 후기](https://www.mindstudio.ai/blog/gpt-6-astra-first-impressions)도 있어 평가는 갈린다.

**정리하면 GPT는 Astra에서 지적된 과잉설계가 아직 남아 있고, Claude는 Opus 5.5에서 완료를 부풀리던 고질적인 문제를 수치로 보일 만큼 줄였다.** 줄어든 것이지 사라진 것은 아니고, 디버깅 개선은 공식 수치로 확인되지 않았다. 이번 실험에서는 6번이 1번보다 훨씬 많은 기능을 만들어서, 과잉설계의 차이를 이 실험 하나로 가를 수는 없었다. 같은 날 나온 GPT-6 Sol과 Luna는 확인하지 않았다.

<details markdown="1" style="margin:1.5rem 0;">
<summary style="cursor:pointer;font-weight:600;">참고 자료 · 2026년 9월 9일, 24일 확인</summary>

- [GameXpert-Bench](https://arxiv.org/html/2608.21833v1#S4.SS3) — 2026년 8월 22일 공개본. 시각적 품질과 플레이 경험의 분리, 실행 기반 기능 평가.
- [OpenAI Image generation tool](https://developers.openai.com/api/docs/guides/tools-image-generation) — 메인 모델과 이미지 생성 도구의 역할.
- [Architectural visualization with Astra](https://developers.openai.com/blog/architectural-visualization-with-astra) — Blender 장면 생성, 외부 에셋 활용, 렌더링을 통한 수정과 Unreal 통합.
- [Meshy Image-to-3D](https://docs.meshy.ai/en/api/image-to-3d), [Rigging](https://docs.meshy.ai/en/api/rigging) — 메시 출력 형식과 비인간형 모델의 리깅 제약.
- [Introducing Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) — 2026년 7월 31일. Clay render와 이미지 참조를 결합하는 영상 생성 방식.
- [ComfyUI: Seedance 2.5 Reference to Video](https://comfy.org/workflows/cd0c4f9f61a4-cd0c4f9f61a4/) — Comfy 팀의 공식 참조 기반 영상 생성 워크플로우.
- [Higgsfield Genjutsu](https://higgsfield.ai/genjutsu), [Higgsfield for Blender](https://higgsfield.ai/blog/higgsfield-blender-plugin) — Motion Transfer와 Blender 뷰포트에서의 Seedance 연동.
- [Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) — 2026년 9월 22일. 정직성 지표 대부분에서 가장 강한 모델이라는 발표.
- [Claude Opus 5.5 System Card](https://www-cdn.anthropic.com/fc1b44717c85dc068bc6ba5024219938094694bd/Claude%20Opus%205.5%20System%20Card.pdf) — 2026년 9월 22일. 6.4.3절 거짓 완료 주장 점수, 2.3.3절 사내 사용에서의 한계, 2.3.4.1절 CoBench 2.1.
- [GPT-6 Astra: What We Learned Previewing OpenAI’s New Model in Production](https://blog.kilo.ai/p/gpt-6-astra-what-we-learned-previewing) — 2026년 9월 4일. Kilo가 정리한 Astra의 과잉설계 경향.
- [Fable Vs Astra Debate Is Over](https://daily.dev/posts/fable-vs-astra-debate-is-over-vurvocilp) — 2026년 9월 11일. Theo(t3.gg) 비교 영상 요약. 머지 전 후속 수정 횟수 비교.
- [GPT-6 Astra vs Fable 5.1: A Week of Head-to-Head Testing](https://www.mindstudio.ai/blog/gpt-6-astra-first-impressions) — 2026년 9월 13일. Astra가 직접 비교에서 더 많이 이겼다는 후기.
- [OpenAI launches GPT-6 Sol and Luna](https://techcrunch.com/2026/09/22/openai-launches-gpt-6-sol-and-luna/) — 2026년 9월 22일. Astra 기반의 더 작은 모델 출시.

</details>

*2026년 9월 9일의 개인 실험이며(6번은 9월 24일에 추가) 반복 측정한 벤치마크는 아니다. Astra는 ChatGPT Pro 20x, Fable과 Opus 5.5는 Claude Max 20x 구독으로 사용했다. 5번은 기존 2D 결과에서 재개발한 시간이며 fal.ai를 통한 3D 생성 비용은 주간 한도 사용량에 포함되지 않는다. 6번의 시간은 Claude Code가 집계한 API 작업 시간이다.*
