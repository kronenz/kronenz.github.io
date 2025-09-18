# 기여 가이드라인

이 프로젝트에 기여해주셔서 감사합니다! 이 문서는 에이전틱 SaaS 조직 가이드 시리즈에 기여하는 방법을 안내합니다.

## 🤝 기여 방법

### 1. 이슈 생성
- 버그 리포트, 기능 요청, 문서 개선 제안 등을 이슈로 생성해주세요
- 이슈 생성 시 명확한 제목과 상세한 설명을 포함해주세요

### 2. 포크 및 브랜치 생성
```bash
# 저장소 포크 후 클론
git clone https://github.com/your-username/agentic-saas-organization.git
cd agentic-saas-organization

# 새로운 브랜치 생성
git checkout -b feature/your-feature-name
```

### 3. 개발 환경 설정
```bash
# 가상환경 설정 (선택사항)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt
```

## 📝 가이드 작성 가이드라인

### 문서 구조
모든 가이드는 다음 구조를 따라야 합니다:

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

## 🔧 도구 사용법

### 가이드 생성
```bash
# 샘플 명세 파일 생성
python tools/guide-generator.py --create-sample

# 가이드 생성
python tools/guide-generator.py --spec examples/sample_guide_spec.json --output my-guide.md
```

### 연속성 검사
```bash
# 특정 시리즈 검사
python tools/continuity-checker.py --series-path series-1 --output continuity-report.json

# 전체 프로젝트 검사
python tools/continuity-checker.py --series-path . --output full-continuity-report.json
```

### 코드 블록 수정
```bash
# 코드 블록 언어 지정 자동 수정
python tools/fix-code-blocks.py --series-path series-1
```

## 📋 품질 기준

### 필수 검사 항목
- [ ] 모든 필수 섹션이 포함되어 있는가?
- [ ] 코드 블록에 언어가 지정되어 있는가?
- [ ] 링크가 유효한가?
- [ ] 용어 일관성이 유지되는가?
- [ ] 가이드 간 연결이 적절한가?

### 자동 검증
모든 변경사항은 다음 자동 검증을 통과해야 합니다:
- 연속성 검사 도구 실행
- 링크 유효성 검사
- 문서 구조 일관성 검증

## 🚀 풀 리퀘스트 프로세스

1. **변경사항 준비**
   - 명확한 커밋 메시지 작성
   - 관련 이슈 번호 포함
   - 변경사항에 대한 설명 추가

2. **PR 생성**
   - PR 제목에 변경사항 요약
   - 상세한 설명과 변경 이유 포함
   - 관련 이슈 링크 추가

3. **리뷰 프로세스**
   - 자동 검증 통과 확인
   - 코드 리뷰 요청
   - 피드백 반영 및 수정

## 📚 시리즈별 기여 가이드

### 시리즈 1: 에이전틱 조직의 기초
- AI 에이전트 기초 개념과 실습 중심
- 명세 기반 개발(SDD) 원칙 적용
- 실제 코드 예제와 실행 가능한 데모 포함

### 시리즈 2: 자동화된 SaaS 팩토리
- GitHub Actions, CI/CD 자동화 중심
- 실제 배포 가능한 프로젝트 예제
- 단계별 자동화 구현 가이드

### 시리즈 3: 디지털 인력 관리
- AI 팀 구성 및 관리 방법론
- 에이전트 협업 모델 설계
- 실제 팀 빌딩 사례와 모범 사례

### 시리즈 4: Devin 아키텍처 분석
- 자율 개발 에이전트 아키텍처 분석
- 실제 구현 가능한 기술 스택
- 성능 최적화 및 확장성 고려

### 시리즈 5: 자율성의 경제학
- 비용 최적화 및 ROI 측정
- 실제 비즈니스 메트릭과 KPI
- 경제적 관점에서의 AI 도입 전략

## 🐛 버그 리포트

버그를 발견하셨다면 다음 정보를 포함해주세요:

- **환경 정보**: OS, Python 버전, 브라우저 등
- **재현 단계**: 문제를 재현하는 정확한 단계
- **예상 결과**: 기대했던 결과
- **실제 결과**: 실제로 발생한 결과
- **로그**: 관련 에러 메시지나 로그

## 💡 기능 요청

새로운 기능이나 개선 사항을 제안하실 때:

- **문제 설명**: 해결하고자 하는 문제
- **제안 솔루션**: 구체적인 해결 방안
- **대안 고려**: 다른 가능한 해결책들
- **추가 컨텍스트**: 관련 정보나 제약사항

## 📞 문의

기여 과정에서 궁금한 점이 있으시면:

- 이슈를 생성해주세요
- 이메일로 연락해주세요: contact@your-website.com
- 커뮤니티 포럼에서 질문해주세요

## 📄 라이선스

이 프로젝트에 기여하시면 [MIT 라이선스](LICENSE) 하에 기여하시는 것으로 간주됩니다.

---

**"AI 어시스턴트에서 자율적 파트너로"** - 에이전틱 SaaS 조직의 미래를 함께 만들어가세요!