---
comments: true
title: "“메이플스토리 만들어줘”: Astra, Fable, Meshy AI"
description: "Astra와 Fable에 같은 프롬프트로 메이플스토리풍 게임을 만들어 달라고 요청했습니다. 제작 시간·플레이 경험을 비교하고 Meshy AI로 3D를 구현한 과정을 기록합니다."
key: 202609090
permalink: /post/2026/09/09/make-maplestory-with-ai.html
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

1~4번은 모두 xhigh로, **각각 새 빈 프로젝트에서 한 번의 프롬프트로 실행했다(one-shot).** 공식 에셋 조건은 기본 프롬프트 끝에 “공식 에셋을 가져다 써”를 덧붙여 함께 입력했다. 5번은 2번 결과를 바탕으로 진행했다.

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

이번 비교에서 Astra를 더 높게 평가한 이유는 게임 경험이다. 내가 중요하게 본 것은 만들어놓은 양보다 그 안에서 플레이를 이어갈 수 있는지였다. 그 기준에서 Astra는 축소된 형태라도 **get shit done**했다.

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

## 만들어보고 남은 생각

“게임을 만들어줘”라는 요청의 결과는 결국 직접 플레이해봐야 알 수 있었다. 3D까지 확장해보니, 에이전트가 도구를 다루는 능력과 원하는 외형을 만들어내는 능력도 따로 살펴볼 필요가 있었다.

<details markdown="1" style="margin:1.5rem 0;">
<summary style="cursor:pointer;font-weight:600;">참고 자료 · 2026년 9월 9일 확인</summary>

- [GameXpert-Bench](https://arxiv.org/html/2608.21833v1#S4.SS3) — 2026년 8월 22일 공개본. 시각적 품질과 플레이 경험의 분리, 실행 기반 기능 평가.
- [OpenAI Image generation tool](https://developers.openai.com/api/docs/guides/tools-image-generation) — 메인 모델과 이미지 생성 도구의 역할.
- [Architectural visualization with Astra](https://developers.openai.com/blog/architectural-visualization-with-astra) — Blender 장면 생성, 외부 에셋 활용, 렌더링을 통한 수정과 Unreal 통합.
- [Meshy Image-to-3D](https://docs.meshy.ai/en/api/image-to-3d), [Rigging](https://docs.meshy.ai/en/api/rigging) — 메시 출력 형식과 비인간형 모델의 리깅 제약.
- [Introducing Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) — 2026년 7월 31일. Clay render와 이미지 참조를 결합하는 영상 생성 방식.
- [ComfyUI: Seedance 2.5 Reference to Video](https://comfy.org/workflows/cd0c4f9f61a4-cd0c4f9f61a4/) — Comfy 팀의 공식 참조 기반 영상 생성 워크플로우.
- [Higgsfield Genjutsu](https://higgsfield.ai/genjutsu), [Higgsfield for Blender](https://higgsfield.ai/blog/higgsfield-blender-plugin) — Motion Transfer와 Blender 뷰포트에서의 Seedance 연동.

</details>

*2026년 9월 9일의 개인 실험이며 반복 측정한 벤치마크는 아니다. Astra는 ChatGPT Pro 20x, Fable은 Claude Max 20x 구독으로 사용했다. 5번은 기존 2D 결과에서 재개발한 시간이며 fal.ai를 통한 3D 생성 비용은 주간 한도 사용량에 포함되지 않는다.*
