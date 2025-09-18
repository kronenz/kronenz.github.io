---
layout: default
title: "1-2: 명세 기반 개발(명세 기반 개발) 마스터하기 - Spec Kit으로 첫 프로젝트 시작하기"
description: "에이전틱 SaaS 조직 가이드"
series: "series-1"
order: 4
---

# 1-2: 명세 기반 개발(명세 기반 개발) 마스터하기 - Spec Kit으로 첫 프로젝트 시작하기

## 📋 개요

명세 기반 개발(Spec-Driven Development, 명세 기반 개발)은 "감성 코딩"의 한계를 극복하고 체계적이고 신뢰할 수 있는 소프트웨어 개발을 가능하게 하는 혁신적인 방법론입니다. 이 가이드에서는 Spec Kit을 활용하여 명세 기반 개발 워크플로우를 완전히 마스터하는 방법을 학습합니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

1. **SDD의 핵심 원리와 4단계 프로세스 이해**
2. **Spec Kit 도구 활용법 완전 마스터**
3. **명확하고 실행 가능한 명세서 작성 능력**
4. **실제 프로젝트에 명세 기반 개발 적용 실습**

## 🔄 SDD의 4단계 워크플로우

### 1단계: 명세(Specify) - "무엇을" 정의하기

SDD의 첫 번째 단계는 기술적 구현이 아닌 **사용자 여정과 성공 기준**에 초점을 맞춘 명확한 명세를 작성하는 것입니다.

#### 명세서의 핵심 구성 요소

```markdown
# 프로젝트 명세서 (spec.md)

## 🎯 프로젝트 개요
- **목적**: 명확한 비즈니스 목표
- **배경**: 문제 상황과 해결 필요성
- **성공 기준**: 측정 가능한 성과 지표

## 👥 사용자 관점
- **주요 사용자**: 타겟 사용자 그룹
- **사용자 시나리오**: 핵심 사용자 여정
- **사용자 가치**: 사용자가 얻는 구체적 가치

## 📝 기능 요구사항
- **핵심 기능**: 반드시 구현해야 할 기능
- **부가 기능**: 있으면 좋은 기능
- **제외 기능**: 명시적으로 제외할 기능

## 🔧 비기능 요구사항
- **성능**: 응답 시간, 처리량, 동시 사용자
- **보안**: 인증, 인가, 데이터 보호
- **확장성**: 사용자 증가에 대한 대응
- **호환성**: 지원할 플랫폼과 브라우저
```markdown

#### Spec Kit을 사용한 명세 생성

```bash
# Spec Kit 설치
npm install -g @spec-kit/cli

# 프로젝트 초기화
spec init my-project
cd my-project

# 명세 생성 시작
spec specify "온라인 쇼핑몰의 장바구니 기능을 구현해주세요"
```markdown

### 2단계: 계획(Plan) - "어떻게" 설계하기

명세가 완성되면 AI 에이전트가 기술적 구현 계획을 생성합니다.

#### 계획서의 핵심 요소

```markdown
# 기술 구현 계획 (plan.md)

## 🏗️ 아키텍처 설계
- **시스템 구조**: 전체 아키텍처 다이어그램
- **기술 스택**: 사용할 기술과 도구
- **데이터 모델**: 데이터베이스 설계
- **API 설계**: RESTful API 엔드포인트

## 📊 데이터베이스 설계
- **엔티티 관계도**: 주요 테이블과 관계
- **인덱스 전략**: 성능 최적화를 위한 인덱스
- **마이그레이션 계획**: 데이터베이스 변경 오케스트레이션

## 🔌 통합 계획
- **외부 서비스**: 결제, 배송, 알림 서비스
- **기존 시스템**: 레거시 시스템과의 연동
- **보안 통합**: 인증 및 권한 오케스트레이션
```markdown

#### Spec Kit으로 계획 생성

```bash
# 명세를 바탕으로 계획 생성
spec plan

# 생성된 계획 검토 및 수정
spec edit plan.md
```markdown

### 3단계: 작업(Tasks) - "단계별" 분해하기

계획을 작고, 독립적이며, 테스트 가능한 작업 단위로 분할합니다.

#### 작업 분해의 원칙

```markdown
# 작업 분해 (tasks.md)

## 📋 작업 분해 원칙
- **작은 단위**: 각 작업은 2-4시간 내 완료 가능
- **독립성**: 다른 작업에 의존하지 않음
- **테스트 가능**: 명확한 완료 기준 존재
- **우선순위**: 중요도와 의존성에 따른 순서

## 🎯 작업 목록
| ID | 작업명 | 설명 | 예상시간 | 우선순위 | 의존성 |
|----|--------|------|----------|----------|--------|
| T001 | 데이터베이스 스키마 설계 | 장바구니 관련 테이블 설계 | 2h | High | - |
| T002 | API 엔드포인트 구현 | 장바구니 CRUD API | 4h | High | T001 |
| T003 | 프론트엔드 컴포넌트 | 장바구니 UI 컴포넌트 | 3h | High | T002 |
| T004 | 테스트 작성 | 단위 및 통합 테스트 | 2h | Medium | T003 |
```markdown

#### Spec Kit으로 작업 분해

```bash
# 계획을 바탕으로 작업 분해
spec tasks

# 작업 우선순위 조정
spec prioritize tasks.md
```markdown

### 4단계: 구현(Implement) - "실행"하기

개발자 에이전트가 작업을 실행하고, 인간은 검증과 방향 수정에 집중합니다.

#### 구현 프로세스

```bash
# 작업 실행 시작
spec implement

# 진행 상황 모니터링
spec status

# 특정 작업 재실행
spec retry T003
```markdown

## 🛠️ Spec Kit 완전 활용 가이드

### 설치 및 초기 설정

```bash
# Spec Kit 설치
npm install -g @spec-kit/cli

# 버전 확인
spec --version

# 도움말 확인
spec --help
```markdown

### 프로젝트 초기화

```bash
# 새 프로젝트 생성
spec init my-sdd-project

# 프로젝트 구조 확인
tree my-sdd-project
```

생성되는 프로젝트 구조:
```
my-sdd-project/
├── spec.md              # 명세서
├── plan.md              # 실행 계획
├── tasks.md             # 작업 분해
├── .spec/               # Spec Kit 설정
│   ├── config.json      # 설정 파일
│   └── templates/       # 템플릿
├── src/                 # 소스 코드
├── tests/               # 테스트 파일
└── docs/                # 문서
```markdown

### 명세 작성 명령어

```bash
# 대화형 명세 작성
spec specify

# 특정 주제로 명세 시작
spec specify "사용자 인증 시스템"

# 명세 검증
spec validate spec.md

# 명세 템플릿 사용
spec template spec.md --type web-app
```markdown

### 계획 생성 명령어

```bash
# 명세를 바탕으로 계획 생성
spec plan

# 특정 기술 스택으로 계획 생성
spec plan --stack "React, Node.js, PostgreSQL"

# 계획 검증
spec validate plan.md

# 계획 템플릿 사용
spec template plan.md --type microservice
```markdown

### 작업 분해 명령어

```bash
# 계획을 바탕으로 작업 분해
spec tasks

# 작업 우선순위 설정
spec prioritize

# 작업 의존성 분석
spec analyze-dependencies

# 작업 템플릿 사용
spec template tasks.md --type frontend
```markdown

### 구현 실행 명령어

```bash
# 모든 작업 실행
spec implement

# 특정 작업만 실행
spec implement T001 T002

# 병렬 실행
spec implement --parallel

# 실행 상태 확인
spec status

# 로그 확인
spec logs
```markdown

## 📝 실습: 온라인 쇼핑몰 장바구니 기능

### 1단계: 명세 작성

```bash
# 프로젝트 초기화
spec init shopping-cart
cd shopping-cart

# 명세 작성 시작
spec specify
```

명세 작성 시 입력할 내용:
```
온라인 쇼핑몰의 장바구니 기능을 구현해주세요.

주요 요구사항:
- 사용자가 상품을 장바구니에 추가/제거할 수 있어야 함
- 장바구니에 담긴 상품의 수량을 조절할 수 있어야 함
- 장바구니 총 금액을 실시간으로 계산해야 함
- 장바구니 내용을 로컬에 저장해야 함
- 반응형 디자인으로 모바일에서도 사용 가능해야 함

기술 스택: React, TypeScript, CSS Modules
```markdown

### 2단계: 계획 생성

```bash
# 명세를 바탕으로 계획 생성
spec plan
```

생성된 계획 예시:
```markdown
# 장바구니 기능 구현 계획

## 🏗️ 아키텍처 설계
- **프론트엔드**: React 18 + TypeScript
- **상태 오케스트레이션**: Context API + useReducer
- **스타일링**: CSS Modules
- **데이터 저장**: localStorage

## 📊 컴포넌트 구조
- CartProvider: 장바구니 상태 오케스트레이션
- CartItem: 개별 상품 컴포넌트
- CartSummary: 총 금액 및 요약
- AddToCartButton: 상품 추가 버튼

## 🔌 API 설계
- addItem(productId, quantity)
- removeItem(productId)
- updateQuantity(productId, quantity)
- clearCart()
- getCartItems()
```markdown

### 3단계: 작업 분해

```bash
# 계획을 바탕으로 작업 분해
spec tasks
```

생성된 작업 예시:
```markdown
# 장바구니 기능 작업 분해

## 📋 작업 목록
| ID | 작업명 | 설명 | 예상시간 | 우선순위 |
|----|--------|------|----------|----------|
| T001 | 프로젝트 설정 | React + TypeScript 프로젝트 초기화 | 1h | High |
| T002 | 타입 정의 | 장바구니 관련 TypeScript 타입 정의 | 1h | High |
| T003 | Context 구현 | 장바구니 상태 오케스트레이션 Context | 2h | High |
| T004 | CartItem 컴포넌트 | 개별 상품 표시 컴포넌트 | 2h | High |
| T005 | CartSummary 컴포넌트 | 총 금액 계산 컴포넌트 | 1h | High |
| T006 | AddToCartButton 컴포넌트 | 상품 추가 버튼 컴포넌트 | 1h | High |
| T007 | localStorage 연동 | 장바구니 데이터 영속화 | 1h | Medium |
| T008 | 반응형 스타일링 | 모바일 대응 CSS | 2h | Medium |
| T009 | 테스트 작성 | 단위 테스트 작성 | 2h | Low |
```markdown

### 4단계: 구현 실행

```bash
# 모든 작업 실행
spec implement

# 특정 작업만 실행
spec implement T001 T002

# 실행 상태 확인
spec status
```markdown

## 🔍 명세 품질 검증

### 자동 검증 도구

```bash
# 명세 완성도 검사
spec validate spec.md

# 계획 일관성 검사
spec validate plan.md

# 작업 분해 적절성 검사
spec validate tasks.md
```markdown

### 수동 검증 체크리스트

#### 명세서 검증
- [ ] 비즈니스 목표가 명확한가?
- [ ] 사용자 시나리오가 구체적인가?
- [ ] 성공 기준이 측정 가능한가?
- [ ] 기술적 제약사항이 명시되었는가?

#### 계획서 검증
- [ ] 아키텍처가 명세와 일치하는가?
- [ ] 기술 스택이 적절한가?
- [ ] 데이터 모델이 완전한가?
- [ ] 보안 고려사항이 포함되었는가?

#### 작업 분해 검증
- [ ] 작업 크기가 적절한가? (2-4시간)
- [ ] 작업 간 의존성이 명확한가?
- [ ] 우선순위가 합리적인가?
- [ ] 완료 기준이 명확한가?

## 🚀 고급 명세 기반 개발 기법

### 템플릿 활용

```bash
# 웹 애플리케이션 템플릿 사용
spec template spec.md --type web-app

# 마이크로서비스 템플릿 사용
spec template spec.md --type microservice

# 모바일 앱 템플릿 사용
spec template spec.md --type mobile-app
```markdown

### 커스텀 템플릿 생성

```bash
# 템플릿 생성
spec create-template my-template

# 템플릿 편집
spec edit-template my-template

# 템플릿 사용
spec template spec.md --template my-template
```markdown

### 협업 워크플로우

```bash
# 명세 공유
spec share spec.md

# 피드백 수집
spec feedback spec.md

# 버전 오케스트레이션
spec version spec.md
```markdown

## 📊 명세 기반 개발 성과 측정

### 품질 지표
- **명세 완성도**: 명세서의 완전성 점수
- **계획 정확도**: 계획 대비 실제 구현 일치도
- **작업 효율성**: 작업 분해의 적절성

### 생산성 지표
- **개발 속도**: 명세 작성부터 배포까지 소요 시간
- **재작업 비율**: 명세 변경으로 인한 재작업 비율
- **품질 향상**: 버그 발생률 감소 정도

## 🔧 문제 해결

### 일반적인 문제와 해결책

#### 1. 명세가 모호한 경우
```bash
# 명세 명확화 도구 사용
spec clarify spec.md

# 질문 기반 명세 보완
spec enhance spec.md --interactive
```markdown

#### 2. 계획이 현실적이지 않은 경우
```bash
# 계획 검증 및 수정
spec validate plan.md --fix

# 기술적 제약사항 재검토
spec review-constraints plan.md
```markdown

#### 3. 작업 분해가 부적절한 경우
```bash
# 작업 크기 재조정
spec resize-tasks tasks.md

# 의존성 재분석
spec analyze-dependencies tasks.md --fix
```

## 🚀 다음 단계

이 가이드를 완료한 후에는 다음 단계로 진행하세요:

1. **[1-3: "감성 코딩"을 넘어서](1-3-principle-based-engineering.md)**
2. **[1-4: `spec.md` 작성의 기술](1-4-spec-writing-techniques.md)**

## 📚 추가 리소스

- [Spec Kit 공식 문서](https://spec-kit.dev/)
- [명세 기반 개발 방법론 가이드](https://spec-driven.dev/)
- [명세서 작성 모범 사례](https://spec-best-practices.dev/)

---

**"명확한 명세가 완벽한 구현의 시작"** - SDD의 핵심 철학
