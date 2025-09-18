# 기여 가이드 (Contributing Guide)

AI 에이전트 조직 구축 및 SaaS 자동화 가이드 프로젝트에 기여해주셔서 감사합니다! 이 문서는 프로젝트에 기여하는 방법을 안내합니다.

## 🤝 기여 방법

### 1. 이슈 보고
- 버그 발견 시 [Issues](https://github.com/your-org/spec-driven-repo/issues)에서 버그 리포트를 작성해주세요
- 새로운 기능 제안도 Issues를 통해 해주세요
- 이슈 작성 시 명확한 제목과 상세한 설명을 포함해주세요

### 2. 코드 기여
- Fork 후 Pull Request를 통해 기여해주세요
- 모든 코드는 기존 스타일을 따라주세요
- 테스트를 작성하고 모든 테스트가 통과하는지 확인해주세요

### 3. 문서 기여
- 오타 수정, 내용 개선, 번역 등 문서 기여를 환영합니다
- 새로운 가이드나 예제 추가도 가능합니다

## 📋 기여 프로세스

### 1. 저장소 포크
```bash
git clone https://github.com/your-username/spec-driven-repo.git
cd spec-driven-repo
```

### 2. 브랜치 생성
```bash
git checkout -b feature/your-feature-name
# 또는
git checkout -b fix/your-bug-fix
```

### 3. 변경사항 커밋
```bash
git add .
git commit -m "feat: Add your feature description"
# 또는
git commit -m "fix: Fix your bug description"
```

### 4. Pull Request 생성
- GitHub에서 Pull Request를 생성해주세요
- 변경사항에 대한 명확한 설명을 포함해주세요
- 관련 이슈가 있다면 링크해주세요

## 📝 코딩 스타일

### 1. 문서 작성
- 마크다운 파일은 명확하고 읽기 쉽게 작성해주세요
- 제목은 계층적으로 구성해주세요
- 코드 블록에는 적절한 언어 태그를 사용해주세요

### 2. 코드 작성
- Python: PEP 8 스타일 가이드 준수
- JavaScript: ESLint 설정 준수
- 기타 언어: 해당 언어의 표준 스타일 가이드 준수

### 3. 커밋 메시지
- [Conventional Commits](https://www.conventionalcommits.org/) 형식 사용
- 예시:
  - `feat: Add new AI agent workflow`
  - `fix: Resolve template parsing issue`
  - `docs: Update series-1 README`
  - `refactor: Simplify task decomposition logic`

## 🧪 테스트

### 1. 코드 테스트
- 새로운 기능 추가 시 테스트 코드를 작성해주세요
- 기존 테스트가 깨지지 않는지 확인해주세요

### 2. 문서 테스트
- 링크가 올바르게 작동하는지 확인해주세요
- 마크다운 문법이 올바른지 확인해주세요

## 📚 가이드라인

### 1. AI 에이전트 관련
- AI 에이전트의 역할과 책임을 명확히 정의해주세요
- 프롬프트와 명세는 구체적이고 실행 가능하게 작성해주세요
- 윤리적 고려사항을 포함해주세요

### 2. 기술 문서
- 단계별 가이드는 명확하고 따라하기 쉽게 작성해주세요
- 코드 예제는 실행 가능하고 주석을 포함해주세요
- 트러블슈팅 섹션을 포함해주세요

### 3. 비즈니스 문서
- ROI와 비용 절감 효과를 구체적으로 제시해주세요
- 성과 측정 지표를 명확히 정의해주세요
- 위험 요소와 대응 방안을 포함해주세요

## 🔍 리뷰 프로세스

### 1. 자동 검사
- 모든 Pull Request는 자동으로 다음 검사를 거칩니다:
  - 코드 스타일 검사
  - 링크 유효성 검사
  - 마크다운 문법 검사

### 2. 수동 리뷰
- 최소 1명의 리뷰어가 코드를 검토합니다
- 리뷰어는 다음 사항을 확인합니다:
  - 코드 품질
  - 문서 완성도
  - 가이드라인 준수

### 3. 승인 기준
- 모든 자동 검사 통과
- 리뷰어 승인
- 충돌 해결 완료

## 🚀 릴리스 프로세스

### 1. 버전 관리
- [Semantic Versioning](https://semver.org/) 사용
- 주요 변경사항은 CHANGELOG.md에 기록

### 2. 릴리스 노트
- 새로운 기능
- 버그 수정
- 주요 변경사항
- 마이그레이션 가이드 (필요시)

## 📞 지원

### 1. 질문
- GitHub Discussions를 사용해주세요
- 이메일: team@example.com

### 2. 실시간 소통
- Slack: #spec-driven-repo
- Discord: AI Agent Community

## 🙏 감사

모든 기여자에게 감사드립니다. 여러분의 기여가 이 프로젝트를 더욱 발전시킵니다!

### 기여자 목록
- [기여자 이름들]

---

**함께 AI 에이전트 조직의 미래를 만들어가요!** 🤖✨
