---
layout: default
title: "1-5: `/plan`과 `/tasks` 활용법 - 명세를 실행 가능한 계획과 작업으로 변환하기"
description: "에이전틱 SaaS 조직 가이드"
order: 7
---

# 1-5: `/plan`과 `/tasks` 활용법 - 명세를 실행 가능한 계획과 작업으로 변환하기

## 📋 개요

명세서(spec.md)를 바탕으로 실행 가능한 계획(plan.md)과 구체적인 작업(tasks.md)으로 변환하는 것은 SDD의 핵심입니다. 이 가이드에서는 AI가 명세를 효과적으로 계획과 작업으로 분해하는 방법을 학습합니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

1. **명세를 계획으로 변환하는 원리 이해**
2. **계획을 구체적인 작업으로 분해하는 기법 습득**
3. **작업 의존성과 우선순위 오케스트레이션 방법 파악**
4. **실제 프로젝트에 적용 가능한 실습 경험**

## 🔄 명세 → 계획 → 작업 변환 프로세스

### 전체 워크플로우

```mermaid
graph TD
    A[spec.md<br/>명세서] --> B[plan.md<br/>실행 계획]
    B --> C[tasks.md<br/>작업 분해]
    C --> D[구현<br/>Implementation]
    
    A1[사용자 요구사항] --> A
    A2[기능 요구사항] --> A
    A3[기술 요구사항] --> A
    
    B1[아키텍처 설계] --> B
    B2[기술 스택 선택] --> B
    B3[데이터 모델 설계] --> B
    
    C1[작업 분해] --> C
    C2[의존성 분석] --> C
    C3[우선순위 설정] --> C
```markdown

## 📋 1단계: 명세를 계획으로 변환

### 계획 생성의 핵심 원리

#### 1. 아키텍처 중심 사고
명세의 기능 요구사항을 기술적 아키텍처로 변환:

```markdown
# 명세서에서 계획으로 변환 예시

## 명세서 (spec.md)
"사용자가 상품을 장바구니에 추가할 수 있어야 함"

## 계획서 (plan.md)
### 아키텍처 설계
- **프론트엔드**: React 컴포넌트로 장바구니 UI 구현
- **상태 오케스트레이션**: Context API로 장바구니 상태 전역 오케스트레이션
- **데이터 저장**: localStorage로 클라이언트 사이드 영속화
- **API 설계**: RESTful 엔드포인트로 장바구니 CRUD 제공

### 컴포넌트 구조
```
CartProvider (상태 오케스트레이션)
├── CartItem (개별 상품)
├── CartSummary (총 금액)
└── AddToCartButton (상품 추가)
```
```markdown

#### 2. 기술 스택 선택 원칙
```markdown
### 기술 스택 선택 기준

#### 프론트엔드 프레임워크
- **React**: 컴포넌트 기반, 풍부한 생태계
- **Vue**: 학습 곡선이 낮음, 빠른 개발
- **Angular**: 엔터프라이즈급, 타입 안정성

#### 상태 오케스트레이션
- **Context API**: 간단한 상태, React 내장
- **Redux**: 복잡한 상태, 예측 가능한 업데이트
- **Zustand**: 가벼움, TypeScript 친화적

#### 데이터 저장
- **localStorage**: 클라이언트 사이드, 간단함
- **IndexedDB**: 복잡한 데이터, 오프라인 지원
- **서버 API**: 실시간 동기화, 다중 디바이스
```markdown

### 계획서 작성 템플릿

```markdown
# [프로젝트명] 실행 계획

## 📋 계획 개요
- **프로젝트명**: [프로젝트 이름]
- **계획 버전**: 1.0.0
- **생성일**: [YYYY-MM-DD]
- **생성자**: AI Planning Agent
- **상태**: [Draft/Review/Approved]

## 🎯 목표 요약
[프로젝트의 핵심 목표를 2-3문장으로 요약]

## 📊 작업 분해 구조 (WBS)
### Phase 1: 기초 구축
```markdown
1. 프로젝트 설정
   ├── 1.1 개발 환경 구성
   ├── 1.2 저장소 초기화
   ├── 1.3 CI/CD 파이프라인 설정
   └── 1.4 기본 문서 작성

2. 핵심 기능 개발
   ├── 2.1 데이터 모델 설계
   ├── 2.2 API 엔드포인트 구현
   ├── 2.3 프론트엔드 컴포넌트 개발
   └── 2.4 기본 테스트 작성
```markdown

### Phase 2: 고급 기능
```markdown
3. 고급 기능 구현
   ├── 3.1 [기능 1] 구현
   ├── 3.2 [기능 2] 구현
   └── 3.3 [기능 3] 구현

4. 통합 및 최적화
   ├── 4.1 시스템 통합
   ├── 4.2 성능 최적화
   └── 4.3 보안 강화
```markdown

### Phase 3: 배포 및 운영
```
5. 배포 준비
   ├── 5.1 프로덕션 환경 구성
   ├── 5.2 모니터링 설정
   └── 5.3 문서화 완료

6. 배포 및 검증
   ├── 6.1 스테이징 배포
   ├── 6.2 사용자 테스트
   └── 6.3 프로덕션 배포
```markdown

## ⏰ 일정 계획
### 전체 일정 (6주)
```
Week 1-2: Phase 1 (기초 구축)
Week 3-4: Phase 2 (고급 기능)
Week 5-6: Phase 3 (배포 및 운영)
```markdown

### 상세 일정
| 작업 | 담당자 | 시작일 | 완료일 | 소요시간 | 의존성 |
|------|--------|--------|--------|----------|--------|
| 1.1 개발 환경 구성 | DevOps | Day 1 | Day 2 | 8h | - |
| 1.2 저장소 초기화 | DevOps | Day 1 | Day 1 | 2h | - |
| 2.1 데이터 모델 설계 | Developer | Day 3 | Day 4 | 16h | 1.1 |
| 2.2 API 구현 | Developer | Day 5 | Day 8 | 32h | 2.1 |
| 2.3 프론트엔드 개발 | Developer | Day 7 | Day 10 | 32h | 2.1 |

## 👥 리소스 할당
### AI 에이전트 팀
- **제품 전략가**: 요구사항 분석, 명세 검증
- **개발자 A**: 백엔드 API 개발
- **개발자 B**: 프론트엔드 개발
- **QA 엔지니어**: 테스트 케이스 작성 및 실행
- **DevOps 엔지니어**: 인프라 및 배포 오케스트레이션

### 외부 리소스
- **클라우드 인프라**: AWS/GCP/Azure
- **외부 API**: [필요한 외부 서비스]
- **디자인 에셋**: [디자인 시스템]

## 🔄 의존성 오케스트레이션
### 크리티컬 패스
```
개발 환경 구성 → 데이터 모델 설계 → API 구현 → 프론트엔드 개발 → 통합 테스트 → 배포
```markdown

### 주요 의존성
- **API 구현** → **프론트엔드 개발** (데이터 인터페이스)
- **데이터 모델** → **API 구현** (스키마 정의)
- **통합 테스트** → **배포** (품질 보증)

## 📊 품질 보증 계획
### 테스트 전략
1. **단위 테스트**: 각 컴포넌트별 테스트
2. **통합 테스트**: API와 프론트엔드 연동 테스트
3. **E2E 테스트**: 전체 사용자 시나리오 테스트
4. **성능 테스트**: 부하 및 응답 시간 테스트

### 코드 품질 기준
- **테스트 커버리지**: 80% 이상
- **코드 리뷰**: 모든 PR에 대해 필수
- **정적 분석**: SonarQube 점수 A등급 이상
- **보안 검사**: OWASP Top 10 준수

## 🚨 위험 오케스트레이션
### 식별된 위험
1. **기술적 위험**
   - 위험: [위험 설명]
   - 확률: [High/Medium/Low]
   - 영향: [High/Medium/Low]
   - 대응 방안: [대응 전략]

2. **일정 위험**
   - 위험: [위험 설명]
   - 확률: [High/Medium/Low]
   - 영향: [High/Medium/Low]
   - 대응 방안: [대응 전략]

## 📈 성과 측정
### 주요 지표 (KPIs)
- **일정 준수율**: 계획 대비 실제 완료율
- **품질 지표**: 버그 밀도, 테스트 커버리지
- **생산성**: 개발자당 기능 처리량
- **비용 효율성**: 예산 대비 산출물

### 보고 주기
- **일일**: 진행 상황 업데이트
- **주간**: 마일스톤 달성 현황
- **월간**: 전체 프로젝트 성과 검토

## 🔄 변경 오케스트레이션
### 변경 요청 프로세스
1. **요청 제출**: 변경 사항 문서화
2. **영향 분석**: 일정, 비용, 품질 영향 평가
3. **승인**: 이해관계자 검토 및 승인
4. **실행**: 승인된 변경 사항 적용
5. **문서화**: 변경 사항 기록 및 공유

## 📚 커뮤니케이션 계획
### 보고 구조
- **일일 스탠드업**: 팀 내 진행 상황 공유
- **주간 리뷰**: 이해관계자 진행 상황 보고
- **마일스톤 데모**: 주요 기능 시연

### 커뮤니케이션 도구
- **프로젝트 오케스트레이션**: Jira/Asana
- **문서 공유**: Confluence/Notion
- **실시간 소통**: Slack/Teams
- **코드 협업**: GitHub/GitLab

## ✅ 완료 기준
### Phase 1 완료 기준
- [ ] 개발 환경 구축 완료
- [ ] 기본 CI/CD 파이프라인 동작
- [ ] 핵심 기능 프로토타입 완성

### Phase 2 완료 기준
- [ ] 모든 기능 구현 완료
- [ ] 테스트 커버리지 80% 달성
- [ ] 성능 요구사항 충족

### Phase 3 완료 기준
- [ ] 프로덕션 배포 완료
- [ ] 사용자 테스트 통과
- [ ] 운영 문서 완성

---

**이 계획은 AI 에이전트 팀이 프로젝트를 체계적으로 실행하기 위한 로드맵입니다.**
```markdown

## 📋 2단계: 계획을 작업으로 분해

### 작업 분해의 핵심 원칙

#### 1. 작은 단위 (Small Units)
각 작업은 2-4시간 내에 완료 가능해야 함:

```markdown
# 작업 크기 가이드라인

## 적절한 작업 크기
- **2시간 이하**: 너무 작음, 오버헤드 발생
- **2-4시간**: 적절함, 집중력 유지 가능
- **4-8시간**: 약간 큼, 분할 고려
- **8시간 이상**: 너무 큼, 반드시 분할 필요

## 작업 분할 예시
### 나쁜 예: 너무 큰 작업
"장바구니 전체 기능 구현" (예상 16시간)

### 좋은 예: 적절한 크기로 분할
- "장바구니 데이터 모델 설계" (2시간)
- "장바구니 Context API 구현" (3시간)
- "장바구니 아이템 컴포넌트 구현" (4시간)
- "장바구니 총 금액 계산 로직" (2시간)
- "장바구니 localStorage 연동" (3시간)
```markdown

#### 2. 독립성 (Independence)
작업 간 의존성을 최소화:

```markdown
# 의존성 최소화 전략

## 순차적 의존성 (Sequential)
작업 A가 완료되어야 작업 B 시작 가능
- 예: 데이터베이스 스키마 설계 → API 구현

## 병렬 실행 가능 (Parallel)
동시에 실행 가능한 작업들
- 예: 프론트엔드 컴포넌트 A, B, C 구현

## 선택적 의존성 (Optional)
선택적으로 의존하는 작업들
- 예: 기본 기능 구현 → 고급 기능 구현
```markdown

#### 3. 테스트 가능성 (Testability)
각 작업은 명확한 완료 기준을 가져야 함:

```markdown
# 테스트 가능한 작업 정의

## 나쁜 예: 모호한 완료 기준
"사용자 인증 기능 구현"

## 좋은 예: 명확한 완료 기준
"사용자 인증 기능 구현"
- [ ] 로그인 API 엔드포인트 구현
- [ ] JWT 토큰 생성 및 검증 로직
- [ ] 비밀번호 해싱 (bcrypt) 적용
- [ ] 로그인 폼 컴포넌트 구현
- [ ] 인증 상태 오케스트레이션 (Context API)
- [ ] 단위 테스트 작성 (커버리지 80% 이상)
- [ ] 통합 테스트 작성
- [ ] API 문서화 완료
```markdown

### 작업 분해 템플릿

```markdown
# [프로젝트명] 작업 분해

## 📋 작업 개요
- **프로젝트명**: [프로젝트 이름]
- **작업 분해 버전**: 1.0.0
- **생성일**: [YYYY-MM-DD]
- **생성자**: AI Task Decomposition Agent
- **상태**: [Draft/Review/Approved]

## 🎯 작업 목표
[이 작업 분해의 목표와 범위를 명확히 기술]

## 📊 작업 분해 구조
### Level 1: 주요 단계
```markdown
1. 프로젝트 초기화
2. 핵심 기능 개발
3. 통합 및 테스트
4. 배포 및 운영
```markdown

### Level 2: 세부 작업
```markdown
1. 프로젝트 초기화
   ├── 1.1 환경 설정
   ├── 1.2 저장소 구성
   ├── 1.3 기본 구조 생성
   └── 1.4 문서화

2. 핵심 기능 개발
   ├── 2.1 데이터 레이어
   ├── 2.2 비즈니스 로직
   ├── 2.3 API 레이어
   └── 2.4 프레젠테이션 레이어
```markdown

## 📝 상세 작업 목록
### 1. 프로젝트 초기화

#### 1.1 환경 설정
| 작업 ID | 작업명 | 설명 | 담당자 | 예상 시간 | 우선순위 | 의존성 |
|---------|--------|------|--------|-----------|----------|--------|
| T001 | 개발 도구 설치 | Node.js, Python, Docker 등 설치 | DevOps | 2h | High | - |
| T002 | 의존성 오케스트레이션 설정 | package.json, requirements.txt 설정 | DevOps | 1h | High | T001 |
| T003 | IDE 구성 | VS Code 확장, 설정 파일 구성 | DevOps | 1h | Medium | T001 |
| T004 | 디버깅 환경 설정 | 디버거 설정, 로그 구성 | DevOps | 2h | Medium | T002 |

#### 1.2 저장소 구성
| 작업 ID | 작업명 | 설명 | 담당자 | 예상 시간 | 우선순위 | 의존성 |
|---------|--------|------|--------|-----------|----------|--------|
| T005 | Git 저장소 초기화 | .gitignore, README.md 생성 | DevOps | 1h | High | - |
| T006 | 브랜치 전략 설정 | main, develop, feature 브랜치 구성 | DevOps | 1h | High | T005 |
| T007 | CI/CD 파이프라인 설정 | GitHub Actions 워크플로우 구성 | DevOps | 4h | High | T005 |
| T008 | 코드 품질 도구 설정 | ESLint, Prettier, SonarQube 설정 | DevOps | 2h | Medium | T005 |

### 2. 핵심 기능 개발

#### 2.1 데이터 레이어
| 작업 ID | 작업명 | 설명 | 담당자 | 예상 시간 | 우선순위 | 의존성 |
|---------|--------|------|--------|-----------|----------|--------|
| T009 | 데이터베이스 스키마 설계 | ERD 작성, 테이블 구조 정의 | Developer | 4h | High | T002 |
| T010 | ORM 설정 | Sequelize/TypeORM 설정 | Developer | 2h | High | T009 |
| T011 | 마이그레이션 스크립트 | 데이터베이스 변경 오케스트레이션 | Developer | 3h | High | T010 |
| T012 | 시드 데이터 생성 | 테스트용 초기 데이터 | Developer | 2h | Medium | T011 |

#### 2.2 비즈니스 로직
| 작업 ID | 작업명 | 설명 | 담당자 | 예상 시간 | 우선순위 | 의존성 |
|---------|--------|------|--------|-----------|----------|--------|
| T013 | 도메인 모델 구현 | 비즈니스 엔티티 클래스 | Developer | 6h | High | T010 |
| T014 | 서비스 레이어 구현 | 비즈니스 로직 서비스 | Developer | 8h | High | T013 |
| T015 | 유효성 검사 구현 | 입력 데이터 검증 로직 | Developer | 4h | High | T014 |
| T016 | 에러 처리 구현 | 예외 처리 및 에러 응답 | Developer | 3h | Medium | T014 |

## ⏰ 일정 계획
### 전체 일정 (6주)
```
Week 1: 프로젝트 초기화 및 기본 CRUD 기능 (T001-T036)
Week 2: 데이터 레이어 개발 (T009-T012)
Week 3: 비즈니스 로직 개발 (T013-T016)
Week 4: API 및 프론트엔드 개발 (T017-T024)
Week 5: 테스트 및 통합 (T025-T032)
Week 6: 배포 및 운영 (T033-T040)
```markdown

### 크리티컬 패스
```
T001 → T002 → T009 → T010 → T013 → T014 → T017 → T018 → T021 → T022 → T025 → T029 → T033 → T037 → T039
```markdown

## 👥 리소스 할당
### 담당자별 작업 분배
- **DevOps (8개 작업)**: 환경 설정, 인프라, 배포
- **Developer (20개 작업)**: 핵심 기능 개발
- **QA (12개 작업)**: 테스트 및 품질 보증

### 작업 우선순위
- **High (24개)**: 핵심 기능 및 필수 작업
- **Medium (16개)**: 부가 기능 및 개선 작업

## 🔄 의존성 오케스트레이션
### 주요 의존성 체인
1. **환경 설정** → **데이터베이스** → **비즈니스 로직** → **API** → **프론트엔드**
2. **개발 완료** → **테스트** → **배포**
3. **API 완료** → **프론트엔드** → **통합 테스트**

### 병렬 실행 가능 작업
- T003, T004 (IDE 구성, 디버깅 환경)
- T021, T022 (UI 컴포넌트, 페이지 구현)
- T025, T026, T027 (다양한 단위 테스트)

## 📊 품질 기준
### 각 작업별 완료 기준
- **코드 작업**: 단위 테스트 작성, 코드 리뷰 통과
- **테스트 작업**: 테스트 케이스 작성, 실행 성공
- **배포 작업**: 환경 검증, 서비스 정상 동작 확인

### 전체 품질 지표
- **테스트 커버리지**: 80% 이상
- **코드 품질**: SonarQube A등급
- **성능**: 응답 시간 2초 이내
- **가용성**: 99.9% 이상

## 🚨 위험 요소
### 기술적 위험
- **의존성 충돌**: 패키지 버전 호환성 문제
- **성능 이슈**: 데이터베이스 쿼리 최적화 필요
- **보안 취약점**: 입력 검증 및 인증 강화 필요

### 일정 위험
- **복잡한 기능**: 예상보다 개발 시간 초과
- **통합 이슈**: 컴포넌트 간 연동 문제
- **테스트 이슈**: 테스트 환경 구성 지연

## 📈 진행 상황 추적
### 일일 체크포인트
- [ ] 오늘 완료할 작업 목표
- [ ] 진행 중인 작업 상태
- [ ] 발생한 이슈 및 해결 방안
- [ ] 내일 작업 계획

### 주간 리뷰
- [ ] 주간 목표 달성 현황
- [ ] 지연된 작업 및 대응 방안
- [ ] 다음 주 우선순위 조정
- [ ] 리소스 재할당 필요성

## ✅ 완료 체크리스트
### 작업 완료 시 확인 사항
- [ ] 코드 작성 완료
- [ ] 단위 테스트 작성 및 통과
- [ ] 코드 리뷰 완료
- [ ] 문서 업데이트
- [ ] 다음 작업 준비

### 마일스톤 완료 시 확인 사항
- [ ] 모든 하위 작업 완료
- [ ] 통합 테스트 통과
- [ ] 품질 기준 충족
- [ ] 이해관계자 승인
- [ ] 다음 단계 준비

---

**이 작업 분해는 AI 에이전트 팀이 프로젝트를 체계적으로 실행하기 위한 상세 가이드입니다.**
```markdown

## 🛠️ 실습: 온라인 쇼핑몰 장바구니 기능

### 1단계: 명세서 분석

```markdown
# 명세서에서 핵심 요구사항 추출

## 기능 요구사항
1. 상품을 장바구니에 추가
2. 장바구니 상품 수량 조절
3. 장바구니 상품 삭제
4. 장바구니 총 금액 계산
5. 장바구니 내용 영속화

## 기술 요구사항
- React 18 + TypeScript
- Context API + useReducer
- localStorage
- 반응형 디자인
- WCAG 2.1 AA 접근성
```markdown

### 2단계: 계획 생성

```bash
# Spec Kit으로 계획 생성
spec plan --input spec.md --output plan.md
```markdown

### 3단계: 작업 분해

```bash
# 계획을 바탕으로 작업 분해
spec tasks --input plan.md --output tasks.md
```markdown

### 4단계: 작업 실행

```bash
# 작업 실행 시작
spec implement --tasks tasks.md
```markdown

## 📊 작업 분해 품질 측정

### 품질 지표
- **작업 크기 적절성**: 2-4시간 작업 비율
- **독립성**: 의존성 없는 작업 비율
- **테스트 가능성**: 명확한 완료 기준 비율
- **우선순위 정확성**: 비즈니스 가치 반영도

### 개선 지표
- **작업 완료율**: 계획 대비 실제 완료율
- **재작업 비율**: 작업 수정 필요 비율
- **병렬 실행율**: 동시 실행 가능 작업 비율
- **의존성 복잡도**: 작업 간 의존성 복잡도

## 🔧 고급 기법

### 1. 동적 작업 분해
```python
# 작업 크기 자동 조정
class TaskSizer:
    def adjust_task_size(self, task, complexity_score):
        if complexity_score > 0.8:
            return self.split_large_task(task)
        elif complexity_score < 0.3:
            return self.merge_small_tasks(task)
        return task
    
    def split_large_task(self, task):
        # 복잡한 작업을 작은 단위로 분할
        subtasks = []
        for component in task.components:
            subtask = Task(
                name=f"{task.name} - {component}",
                duration=task.duration / len(task.components),
                dependencies=task.dependencies
            )
            subtasks.append(subtask)
        return subtasks
```markdown

### 2. 의존성 최적화
```python
# 의존성 그래프 최적화
class DependencyOptimizer:
    def optimize_dependencies(self, tasks):
        # 의존성 체인 분석
        chains = self.find_dependency_chains(tasks)
        
        # 병렬 실행 가능한 작업 식별
        parallel_groups = self.group_parallel_tasks(chains)
        
        # 크리티컬 패스 계산
        critical_path = self.calculate_critical_path(tasks)
        
        return {
            "optimized_tasks": tasks,
            "parallel_groups": parallel_groups,
            "critical_path": critical_path
        }
```markdown

### 3. 실시간 작업 조정
```python
# 실시간 작업 상태 모니터링
class TaskMonitor:
    def __init__(self):
        self.task_status = {}
        self.performance_metrics = {}
    
    def update_task_status(self, task_id, status, progress):
        self.task_status[task_id] = {
            "status": status,
            "progress": progress,
            "updated_at": datetime.now()
        }
        
        # 성능 지표 업데이트
        self.update_performance_metrics(task_id, progress)
    
    def suggest_adjustments(self):
        # 지연된 작업 식별
        delayed_tasks = self.identify_delayed_tasks()
        
        # 리소스 재할당 제안
        resource_suggestions = self.suggest_resource_reallocation()
        
        # 일정 조정 제안
        schedule_suggestions = self.suggest_schedule_adjustments()
        
        return {
            "delayed_tasks": delayed_tasks,
            "resource_suggestions": resource_suggestions,
            "schedule_suggestions": schedule_suggestions
        }
```

## 🚀 다음 단계

이 가이드를 완료한 후에는 다음 단계로 진행하세요:

1. **[1-6: 이중 LLM 인지 아키텍처 구축](1-6-dual-llm-architecture.html)**
2. **[1-7: 검증 루프 구현](1-7-verification-loop.html)**

## 📚 추가 리소스

- [작업 분해 기법](https://work-breakdown.dev/)
- [프로젝트 오케스트레이션 도구](https://project-management.dev/)
- [의존성 오케스트레이션](https://dependency-management.dev/)

---

**"명확한 계획이 성공적인 실행의 열쇠"** - 계획과 작업 분해의 핵심
