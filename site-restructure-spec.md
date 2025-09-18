# 사이트 구조 재설계 스펙

## 📋 프로젝트 개요

GitHub Pages 사이트를 AI 자동화 중심의 구조로 재설계하고, Medium/Apple 스타일의 모던한 디자인으로 변경합니다.

## 🎯 목표

1. **AI 자동화 중심 구조**: 상단 메뉴를 AI 자동화 워크플로우 기반으로 재구성
2. **직관적 네비게이션**: 대표 제목으로 챕터 구분하여 사용자 경험 개선
3. **모던 디자인**: Medium 기술 칼럼 + Apple 홈페이지 스타일 적용
4. **반응형 레이아웃**: 모든 디바이스에서 최적화된 사용자 경험

## 🏗️ 새로운 사이트 구조

### 1. 상단 메뉴 구조 (AI 자동화 워크플로우 기반)

```
홈 | AI 기반 개발 | 자동화 팩토리 | 팀 관리 | 고급 아키텍처 | 비즈니스 성장 | 리소스
```

**메뉴 설명:**
- **홈**: 메인 랜딩 페이지
- **AI 기반 개발**: 기존 시리즈 1 (에이전틱 조직의 기초)
- **자동화 팩토리**: 기존 시리즈 2 (자동화된 SaaS 팩토리)
- **팀 관리**: 기존 시리즈 3 (디지털 인력 관리)
- **고급 아키텍처**: 기존 시리즈 4 (Devin 아키텍처 분석)
- **비즈니스 성장**: 기존 시리즈 5 (자율성의 경제학)
- **리소스**: 도구, 템플릿, 추가 자료

### 2. 챕터 제목 변경

| 기존 시리즈 | 새로운 대표 제목 | 설명 |
|------------|-----------------|------|
| 시리즈 1 | AI 기반 개발 | AI 에이전트와 협업하는 기본 원리 |
| 시리즈 2 | 자동화 팩토리 | 완전 자동화된 개발 파이프라인 |
| 시리즈 3 | 팀 관리 | AI 에이전트 팀 운영 및 관리 |
| 시리즈 4 | 고급 아키텍처 | 고급 AI 에이전트 아키텍처 |
| 시리즈 5 | 비즈니스 성장 | AI 기반 비즈니스 성장 전략 |

### 3. 디자인 시스템

#### 3.1 컬러 팔레트
```css
/* Primary Colors */
--primary-blue: #007AFF;
--primary-dark: #1D1D1F;
--primary-light: #F5F5F7;

/* Secondary Colors */
--secondary-gray: #8E8E93;
--secondary-light: #F2F2F7;
--accent-green: #30D158;
--accent-orange: #FF9500;

/* Text Colors */
--text-primary: #1D1D1F;
--text-secondary: #8E8E93;
--text-tertiary: #C7C7CC;
```

#### 3.2 타이포그래피
```css
/* Font Stack */
font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif;

/* Heading Styles */
h1: 48px, 600, -0.02em line-height
h2: 32px, 600, -0.01em line-height
h3: 24px, 500, normal line-height
h4: 20px, 500, normal line-height

/* Body Text */
body: 17px, 400, 1.47 line-height
small: 15px, 400, 1.33 line-height
```

#### 3.3 레이아웃 시스템
```css
/* Container */
max-width: 1200px
padding: 0 20px
margin: 0 auto

/* Grid System */
display: grid
grid-template-columns: repeat(12, 1fr)
gap: 24px

/* Spacing Scale */
--space-xs: 8px
--space-sm: 16px
--space-md: 24px
--space-lg: 32px
--space-xl: 48px
--space-2xl: 64px
```

## 📁 파일 구조 변경

### 1. 디렉토리 구조
```
/
├── index.md (메인 랜딩)
├── ai-development/ (시리즈 1)
├── automation-factory/ (시리즈 2)
├── team-management/ (시리즈 3)
├── advanced-architecture/ (시리즈 4)
├── business-growth/ (시리즈 5)
├── resources/ (리소스 섹션)
├── _layouts/
│   ├── default.html
│   ├── home.html
│   ├── chapter.html
│   └── guide.html
├── _sass/
│   ├── _variables.scss
│   ├── _typography.scss
│   ├── _layout.scss
│   └── _components.scss
└── assets/
    ├── css/
    │   └── main.scss
    └── js/
        └── main.js
```

### 2. Jekyll 설정 변경

#### 2.1 _config.yml 업데이트
```yaml
# Navigation
navigation:
  - title: "홈"
    url: "/"
  - title: "AI 기반 개발"
    url: "/ai-development/"
  - title: "자동화 팩토리"
    url: "/automation-factory/"
  - title: "팀 관리"
    url: "/team-management/"
  - title: "고급 아키텍처"
    url: "/advanced-architecture/"
  - title: "비즈니스 성장"
    url: "/business-growth/"
  - title: "리소스"
    url: "/resources/"

# Collections
collections:
  chapters:
    output: true
    permalink: /:name/
  guides:
    output: true
    permalink: /:name/
```

## 🎨 디자인 컴포넌트

### 1. 헤더 컴포넌트
```html
<header class="site-header">
  <nav class="main-nav">
    <div class="nav-brand">
      <a href="/">에이전틱 SaaS 조직</a>
    </div>
    <ul class="nav-menu">
      <!-- Navigation items -->
    </ul>
  </nav>
</header>
```

### 2. 히어로 섹션
```html
<section class="hero">
  <div class="hero-content">
    <h1>AI 자동화로 100배 생산성 달성</h1>
    <p>에이전틱 SaaS 조직 구축을 위한 체계적인 가이드</p>
    <div class="hero-actions">
      <a href="/ai-development/" class="btn-primary">시작하기</a>
      <a href="/resources/" class="btn-secondary">리소스 보기</a>
    </div>
  </div>
</section>
```

### 3. 카드 컴포넌트
```html
<div class="card">
  <div class="card-header">
    <h3>AI 기반 개발</h3>
    <span class="card-badge">기초</span>
  </div>
  <div class="card-content">
    <p>AI 에이전트와 협업하는 기본 원리와 방법을 학습합니다.</p>
    <ul class="card-features">
      <li>에이전틱 AI 이해</li>
      <li>명세 기반 개발</li>
      <li>이중 LLM 아키텍처</li>
    </ul>
  </div>
  <div class="card-footer">
    <a href="/ai-development/" class="card-link">자세히 보기 →</a>
  </div>
</div>
```

## 📝 콘텐츠 변경사항

### 1. 이모지 제거
- 모든 이모지 제거
- 텍스트 기반 아이콘 사용
- 깔끔한 텍스트 중심 디자인

### 2. Medium 스타일 적용
- 읽기 쉬운 타이포그래피
- 충분한 여백과 줄 간격
- 코드 블록 스타일링
- 인용구 디자인

### 3. Apple 스타일 적용
- 미니멀한 디자인
- 부드러운 애니메이션
- 고품질 이미지
- 직관적인 인터랙션

## 🔧 구현 단계

### Phase 1: 구조 변경
1. 디렉토리 구조 변경
2. 파일 이동 및 링크 업데이트
3. Jekyll 설정 수정

### Phase 2: 디자인 시스템
1. SCSS 파일 구조 생성
2. 컴포넌트 스타일링
3. 반응형 레이아웃 구현

### Phase 3: 콘텐츠 업데이트
1. 이모지 제거
2. 텍스트 스타일 통일
3. 링크 검증 및 수정

### Phase 4: 최적화
1. 성능 최적화
2. SEO 개선
3. 접근성 향상

## 📊 성공 지표

- **사용자 경험**: 페이지 로딩 시간 < 2초
- **반응성**: 모든 디바이스에서 완벽한 레이아웃
- **접근성**: WCAG 2.1 AA 준수
- **SEO**: 모든 페이지 메타데이터 완성

## 🚀 예상 결과

1. **직관적 네비게이션**: AI 자동화 워크플로우 기반 메뉴로 사용자 이해도 향상
2. **모던한 디자인**: Medium/Apple 스타일로 전문성과 신뢰성 증대
3. **향상된 사용성**: 깔끔한 디자인과 명확한 구조로 사용자 경험 개선
4. **확장성**: 새로운 콘텐츠 추가 시 일관된 디자인 시스템 활용 가능

---

**"AI 자동화의 미래를 위한 모던한 학습 플랫폼"** - 사용자 중심의 직관적이고 아름다운 사이트로 전환합니다.
