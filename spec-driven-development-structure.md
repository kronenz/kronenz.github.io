# Spec Driven Development (SDD) 레포지토리 구조

## 📁 전체 디렉토리 구조

```
spec/
├── README.md                           # 프로젝트 개요 및 시작 가이드
├── contents.md                         # 전체 가이드 시리즈 목차
├── constitution.md                     # AI 에이전트를 위한 핵심 원칙
├── CONTRIBUTING.md                     # 기여 가이드라인
├── LICENSE                             # 라이선스 정보
│
├── series-1/                          # 시리즈 1: 에이전틱 조직의 기초
│   ├── 1-1-agentic-ai-start.md
│   ├── 1-2-spec-driven-development.md
│   ├── 1-3-principle-based-engineering.md
│   ├── 1-4-spec-writing-techniques.md
│   ├── 1-5-plan-tasks-utilization.md
│   ├── 1-6-dual-llm-architecture.md
│   ├── 1-7-verification-loop.md
│   ├── 1-8-orchestration-framework.md
│   ├── 1-9-crewai-team-building.md
│   └── 1-10-constitution-writing.md
│
├── series-2/                          # 시리즈 2: 자동화된 SaaS 팩토리
│   ├── 2-1-github-actions-101.md
│   ├── 2-2-automation-triggers.md
│   ├── 2-3-front-office-setup.md
│   ├── 2-4-factory-floor-construction.md
│   ├── 2-5-autonomous-commits-prs.md
│   ├── 2-6-quality-control-setup.md
│   ├── 2-7-autonomous-qa-team.md
│   ├── 2-8-test-automation.md
│   ├── 2-9-self-healing-tests.md
│   ├── 2-10-shipping-dock-setup.md
│   └── 2-11-end-to-end-project.md
│
├── series-3/                          # 시리즈 3: 디지털 인력 관리
│   ├── 3-1-gendd-model.md
│   ├── 3-2-ai-team-roles.md
│   ├── 3-3-agent-persona-creation.md
│   ├── 3-4-agent-collaboration-models.md
│   ├── 3-5-conflict-resolution.md
│   ├── 3-6-coder-to-conductor.md
│   ├── 3-7-future-core-skills.md
│   ├── 3-8-strategic-validation.md
│   └── 3-9-digital-employee-onboarding.md
│
├── series-4/                          # 시리즈 4: Devin 아키텍처 분석
│   ├── 4-1-devin-architecture-analysis.md
│   ├── 4-2-devin-brain-replication.md
│   ├── 4-3-self-correction-mechanisms.md
│   ├── 4-4-multidevin-model.md
│   ├── 4-5-devin-playbook-application.md
│   └── 4-6-known-limitations-reality.md
│
├── series-5/                          # 시리즈 5: 자율성의 경제학
│   ├── 5-1-100x-productivity-quantification.md
│   ├── 5-2-ai-finops-introduction.md
│   ├── 5-3-finops-agent-construction.md
│   ├── 5-4-automated-resource-management.md
│   ├── 5-5-spot-instance-mastery.md
│   ├── 5-6-autonomous-growth-hacking.md
│   ├── 5-7-rl-ui-ux-optimization.md
│   ├── 5-8-reward-function-design.md
│   └── 5-9-real-time-ux-optimization.md
│
├── templates/                         # 가이드 작성 템플릿
│   ├── guide-template.md              # 기본 가이드 템플릿
│   ├── series-overview-template.md    # 시리즈 개요 템플릿
│   ├── code-example-template.py       # 코드 예제 템플릿
│   └── checklist-template.md          # 체크리스트 템플릿
│
├── examples/                          # 실습 예제 및 샘플 코드
│   ├── basic-agent/                   # 기본 에이전트 예제
│   ├── crewai-team/                   # CrewAI 팀 예제
│   ├── sdd-workflow/                  # SDD 워크플로우 예제
│   ├── github-actions/                # GitHub Actions 예제
│   └── finops-optimization/           # FinOps 최적화 예제
│
├── tools/                            # SDD 도구 및 스크립트
│   ├── spec-validator.py             # 명세서 검증 도구
│   ├── guide-generator.py            # 가이드 생성 도구
│   ├── continuity-checker.py         # 연속성 검사 도구
│   └── template-processor.py         # 템플릿 처리 도구
│
├── docs/                             # 추가 문서
│   ├── architecture/                 # 아키텍처 문서
│   ├── best-practices/               # 모범 사례
│   ├── troubleshooting/              # 문제 해결 가이드
│   └── glossary.md                   # 용어 사전
│
└── scripts/                          # 유틸리티 스크립트
    ├── setup.sh                      # 환경 설정 스크립트
    ├── validate-guides.py            # 가이드 검증 스크립트
    ├── generate-index.py             # 인덱스 생성 스크립트
    └── update-links.py               # 링크 업데이트 스크립트
```

## 🎯 SDD 핵심 원칙

### 1. 명세 우선 (Specification First)
- 모든 개발은 명확한 명세서(`spec.md`)로 시작
- 기능적 요구사항과 비기능적 요구사항을 명확히 정의
- AI 에이전트가 이해할 수 있는 구조화된 형식 사용

### 2. 단계적 정제 (Progressive Refinement)
- 고수준 명세 → 상세 계획 → 구체적 작업으로 단계적 정제
- 각 단계에서 검증 및 피드백 루프 구현
- 모호함을 점진적으로 제거

### 3. 검증 중심 (Verification-Driven)
- 각 단계마다 명확한 검증 기준 설정
- 자동화된 테스트와 수동 검토의 균형
- 지속적인 품질 보장

### 4. 문서화 중심 (Documentation-Centric)
- 모든 과정과 결정사항을 문서화
- 재사용 가능한 템플릿과 패턴 활용
- 지식의 체계적 축적

## 📋 가이드 작성 표준

### 문서 구조
1. **개요 (Overview)**: 가이드의 목적과 범위
2. **학습 목표 (Learning Objectives)**: 달성할 수 있는 구체적 목표
3. **핵심 개념 (Core Concepts)**: 이론적 배경
4. **실습 (Hands-on Practice)**: 단계별 실습 가이드
5. **고급 기능 (Advanced Features)**: 심화 내용
6. **다음 단계 (Next Steps)**: 연관 가이드 연결
7. **추가 리소스 (Additional Resources)**: 참고 자료

### 코드 예제 표준
- 모든 코드는 실행 가능해야 함
- 주석과 설명을 충분히 포함
- 에러 처리 및 예외 상황 고려
- 실제 프로덕션 환경을 고려한 구조

### 링크 및 참조 표준
- 상대 경로 사용 (`../series-1/1-2-spec-driven-development.md`)
- 절대 URL은 최소화
- 깨진 링크 자동 검증
- 크로스 레퍼런스 일관성 유지

## 🔄 연속성 보장 메커니즘

### 1. 템플릿 기반 작성
- 표준화된 템플릿 사용
- 일관된 구조와 스타일 유지
- 빠른 가이드 생성 가능

### 2. 자동화된 검증
- 링크 유효성 검사
- 코드 예제 실행 테스트
- 문서 구조 일관성 검증

### 3. 점진적 구축
- 각 시리즈를 독립적으로 완성
- 시리즈 간 의존성 최소화
- 병렬 개발 가능

### 4. 피드백 루프
- 사용자 피드백 수집
- 지속적인 개선
- 버전 관리 및 업데이트

## 🛠️ 도구 및 자동화

### Spec Kit 통합
- `/specify` 명령어로 명세서 생성
- `/plan` 명령어로 계획 수립
- `/tasks` 명령어로 작업 분할

### GitHub Actions 워크플로우
- 문서 변경 시 자동 검증
- 링크 및 코드 예제 테스트
- 자동 인덱스 업데이트

### AI 에이전트 활용
- 가이드 생성 자동화
- 일관성 검사 및 수정
- 번역 및 현지화 지원

이 구조는 방대한 가이드 시리즈의 체계적이고 지속 가능한 구축을 위한 기반을 제공합니다.
