---
layout: chapter
title: "자동화 팩토리"
description: "완전 자동화된 개발 파이프라인을 구축합니다"
chapter: "automation-factory"
order: 2
---

# 자동화 팩토리

## 개요

시리즈 2는 완전 자동화된 개발 파이프라인을 구축하는 방법을 다룹니다. GitHub 이슈 생성부터 배포까지, 거의 모든 과정을 AI 에이전트가 자율적으로 처리하는 "SaaS 팩토리"를 구축합니다.

## 학습 목표

이 시리즈를 완료하면 다음을 달성할 수 있습니다:

1. **CI/CD 자동화**: GitHub Actions를 활용한 완전 자동화된 워크플로우
2. **AI 워크플로우**: GitHub 이슈를 트리거로 하는 AI 기반 개발 프로세스
3. **프런트 오피스**: 자동화된 요구사항 분석 및 명세 생성
4. **공장 플로어**: AI 개발자 팀의 자율적 코드 생성 및 관리
5. **품질 관리**: 자동화된 코드 리뷰 및 테스트 시스템
6. **QA 자동화**: Gherkin 기반 테스트 자동 생성 및 실행
7. **자가 치유**: UI 변경에 자동 적응하는 테스트 시스템
8. **DevOps 자동화**: 완전 자동화된 배포 및 모니터링

## 📚 가이드 목록

### 2-1: GitHub Actions 101
**첫 번째 CI/CD 워크플로우 자동화**

[가이드 보기 →](/automation-factory/2-1-github-actions-101.html)

- GitHub Actions 기본 개념
- 워크플로우 작성 방법
- 자동화 트리거 설정
- 실제 프로젝트 적용

### 2-2: 자동화의 시작
**GitHub 이슈 생성을 트리거로 AI 워크플로우 실행하기**

[가이드 보기 →](/automation-factory/2-2-automation-triggers.html)

- 이슈 기반 워크플로우 설계
- AI 에이전트 연동
- 자동화 파이프라인 구축
- 모니터링 및 관리

### 2-3: 프런트 오피스 구축
**이슈를 분석하여 명세와 계획을 자동 생성하는 제품 전략가 에이전트**

[가이드 보기 →](/automation-factory/2-3-front-office-setup.html)

- 제품 전략가 에이전트 설계
- 이슈 분석 자동화
- 명세 및 계획 생성
- 품질 보장 메커니즘

### 2-4: 공장 플로어 구축
**CrewAI로 Claude Code 개발자 팀을 오케스트레이션하기**

[가이드 보기 →](/automation-factory/2-4-factory-floor-construction.html)

- 개발자 팀 구성
- CrewAI 오케스트레이션
- 코드 생성 자동화
- 협업 워크플로우

### 2-5: 자율적 코드 커밋 및 PR 생성
**AI 에이전트가 Git과 상호작용하는 방법**

[가이드 보기 →](/automation-factory/2-5-autonomous-commits-prs.html)

- Git 자동화 전략
- PR 생성 및 관리
- 코드 리뷰 자동화
- 브랜치 전략

### 2-6: 품질 관리 구축
**PR을 기반으로 자동 코드 리뷰를 수행하는 검증 에이전트**

[가이드 보기 →](/automation-factory/2-6-quality-control-setup.html)

- 검증 에이전트 설계
- 자동 코드 리뷰
- 품질 기준 설정
- 피드백 루프 구축

### 2-7: 자율적 QA 팀 구성
**명세서로부터 Gherkin 테스트 케이스를 생성하는 QA 에이전트**

[가이드 보기 →](/automation-factory/2-7-autonomous-qa-team.html)

- QA 에이전트 구축
- Gherkin 테스트 생성
- 자동화된 테스트 실행
- 결과 분석 및 보고

### 2-8: 테스트 자동화
**Gherkin 시나리오를 Selenium/Playwright 스크립트로 변환하고 실행하기**

[가이드 보기 →](/automation-factory/2-8-test-automation.html)

- 테스트 스크립트 생성
- Selenium/Playwright 활용
- 자동화된 실행 환경
- 결과 리포팅

### 2-9: 자가 치유 테스트의 구현
**UI 변경에 자동으로 적응하는 회복탄력성 있는 QA 시스템**

[가이드 보기 →](/automation-factory/2-9-self-healing-tests.html)

- 자가 치유 메커니즘
- UI 변경 감지
- 테스트 자동 수정
- 학습 기반 개선

### 2-10: 출하 부두 구축
**테스트 통과 후 자동으로 배포를 관리하는 DevOps 에이전트**

[가이드 보기 →](/automation-factory/2-10-shipping-dock-setup.html)

- DevOps 에이전트 구축
- 자동 배포 파이프라인
- 모니터링 및 알림
- 롤백 전략

### 2-11: 엔드-투-엔드 프로젝트
**단일 GitHub 이슈로 마이크로 SaaS 앱 전체 구축하기**

[가이드 보기 →](/automation-factory/2-11-end-to-end-project.html)

- 전체 파이프라인 통합
- 실제 프로젝트 실습
- 성능 최적화
- 운영 노하우

## 🚀 다음 단계

이 시리즈를 완료한 후에는 다음 단계로 진행하세요:

1. **[시리즈 3: 팀 관리](../team-management/)**: AI 에이전트 팀 운영 방법
2. **[시리즈 4: 고급 아키텍처](../advanced-architecture/)**: 고급 AI 에이전트 아키텍처

## 📋 학습 체크리스트

- [ ] 2-1: GitHub Actions 워크플로우 구축
- [ ] 2-2: AI 워크플로우 트리거 설정
- [ ] 2-3: 프런트 오피스 에이전트 구축
- [ ] 2-4: 개발자 팀 오케스트레이션
- [ ] 2-5: 자율적 Git 워크플로우
- [ ] 2-6: 품질 관리 시스템 구축
- [ ] 2-7: QA 팀 자동화
- [ ] 2-8: 테스트 자동화 구현
- [ ] 2-9: 자가 치유 테스트 시스템
- [ ] 2-10: DevOps 자동화
- [ ] 2-11: 엔드-투-엔드 프로젝트 완성

---

**"이슈에서 배포까지, 완전 자동화된 개발 공장"** - 자동화 팩토리의 혁신

© 2025 에이전틱 SaaS 조직. All rights reserved.