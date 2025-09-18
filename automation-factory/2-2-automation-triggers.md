---
layout: default
title: "2-2-automation-triggers: 2 2 automation triggers"
description: "에이전틱 SaaS 조직 가이드"
order: 4
---

# 자동화의 시작: GitHub 이슈 생성을 트리거로 AI 워크플로우 실행하기

## 개요

GitHub 이슈를 트리거로 AI 워크플로우를 자동 실행하는 것은 에이전틱 SaaS 조직의 핵심 기능입니다. 이 가이드에서는 이슈 생성, 라벨링, 댓글 등을 통해 AI 에이전트가 자동으로 반응하고 작업을 수행하는 시스템을 구축하는 방법을 학습합니다.

## 학습 목표

이 가이드를 완료하면 다음을 할 수 있습니다:
- GitHub 이벤트 기반 워크플로우 트리거 설정
- 이슈 분석 및 자동 분류 시스템 구축
- AI 에이전트와 연동된 자동화 파이프라인 구현
- 워크플로우 조건부 실행 및 에러 처리

## 핵심 개념

### GitHub 이벤트 트리거

GitHub Actions는 다양한 이벤트를 트리거로 사용할 수 있습니다:

- **issues**: 이슈 생성, 수정, 삭제, 라벨링
- **issue_comment**: 이슈 댓글 생성, 수정, 삭제
- **pull_request**: PR 생성, 수정, 머지
- **push**: 코드 푸시
- **workflow_dispatch**: 수동 실행
- **schedule**: 크론 스케줄

### 이벤트 필터링

특정 조건에서만 워크플로우를 실행하도록 필터링할 수 있습니다:

```yaml
on:
  issues:
    types: [opened, labeled]
    branches: [main]
  issue_comment:
    types: [created]
    branches: [main]
```

## 실습: 이슈 기반 자동화 구축

### 1단계: 기본 이슈 트리거 워크플로우

```yaml
name: 이슈 기반 AI 자동화

on:
  issues:
    types: [opened, labeled, assigned]
  issue_comment:
    types: [created]

jobs:
  # 이슈 분석 및 분류
  analyze-issue:
    runs-on: ubuntu-latest
    if: github.event_name == 'issues'
    
    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v4
      
    - name: Python 설정
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 의존성 설치
      run: |
        pip install -r requirements.txt
        pip install openai anthropic requests
        
    - name: 이슈 정보 추출
      id: extract-issue
      run: |
        echo "issue-number=${{ github.event.issue.number }}" >> $GITHUB_OUTPUT
        echo "issue-title=${{ github.event.issue.title }}" >> $GITHUB_OUTPUT
        echo "issue-body=${{ github.event.issue.body }}" >> $GITHUB_OUTPUT
        echo "issue-labels=${{ join(github.event.issue.labels.*.name, ',') }}" >> $GITHUB_OUTPUT
        
    - name: 이슈 분석
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/analyze_issue.py \
          --issue-number ${{ steps.extract-issue.outputs.issue-number }} \
          --title "${{ steps.extract-issue.outputs.issue-title }}" \
          --body "${{ steps.extract-issue.outputs.issue-body }}" \
          --labels "${{ steps.extract-issue.outputs.issue-labels }}"
          
    - name: 이슈 라벨링
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/auto_label_issue.py \
          --issue-number ${{ steps.extract-issue.outputs.issue-number }} \
          --analysis-result analysis_result.json
```

### 2단계: AI 에이전트 연동

이슈를 분석하고 적절한 AI 에이전트에게 작업을 할당하는 시스템을 구축합니다:

```yaml
name: AI 에이전트 자동 할당

on:
  issues:
    types: [opened, labeled]
  issue_comment:
    types: [created]

jobs:
  # 이슈 분석 및 에이전트 할당
  assign-agent:
    runs-on: ubuntu-latest
    if: github.event_name == 'issues'
    
    outputs:
      agent-type: ${{ steps.analyze.outputs.agent-type }}
      priority: ${{ steps.analyze.outputs.priority }}
      estimated-time: ${{ steps.analyze.outputs.estimated-time }}
    
    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v4
      
    - name: Python 설정
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 의존성 설치
      run: |
        pip install -r requirements.txt
        pip install openai anthropic crewai
        
    - name: 이슈 분석 및 에이전트 할당
      id: analyze
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
      run: |
        python scripts/assign_agent.py \
          --issue-number ${{ github.event.issue.number }} \
          --title "${{ github.event.issue.title }}" \
          --body "${{ github.event.issue.body }}"
          
    - name: 이슈 업데이트
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/update_issue.py \
          --issue-number ${{ github.event.issue.number }} \
          --agent-type ${{ steps.analyze.outputs.agent-type }} \
          --priority ${{ steps.analyze.outputs.priority }} \
          --estimated-time ${{ steps.analyze.outputs.estimated-time }}

  # 제품 전략가 에이전트
  product-strategist:
    runs-on: ubuntu-latest
    needs: assign-agent
    if: needs.assign-agent.outputs.agent-type == 'product-strategist'
    
    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v4
      
    - name: Python 설정
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 의존성 설치
      run: |
        pip install -r requirements.txt
        pip install openai anthropic crewai
        
    - name: 제품 전략가 에이전트 실행
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/product_strategist_agent.py \
          --issue-number ${{ github.event.issue.number }} \
          --priority ${{ needs.assign-agent.outputs.priority }}

  # 개발자 에이전트
  developer:
    runs-on: ubuntu-latest
    needs: assign-agent
    if: needs.assign-agent.outputs.agent-type == 'developer'
    
    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v4
      
    - name: Python 설정
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 의존성 설치
      run: |
        pip install -r requirements.txt
        pip install openai anthropic crewai
        
    - name: 개발자 에이전트 실행
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/developer_agent.py \
          --issue-number ${{ github.event.issue.number }} \
          --priority ${{ needs.assign-agent.outputs.priority }}

  # QA 에이전트
  qa-engineer:
    runs-on: ubuntu-latest
    needs: assign-agent
    if: needs.assign-agent.outputs.agent-type == 'qa-engineer'
    
    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v4
      
    - name: Python 설정
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 의존성 설치
      run: |
        pip install -r requirements.txt
        pip install openai anthropic crewai
        
    - name: QA 에이전트 실행
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/qa_agent.py \
          --issue-number ${{ github.event.issue.number }} \
          --priority ${{ needs.assign-agent.outputs.priority }}
```

### 3단계: 댓글 기반 명령어 처리

이슈 댓글을 통해 AI 에이전트에게 명령을 내리는 시스템을 구축합니다:

```yaml
name: 댓글 기반 AI 명령어

on:
  issue_comment:
    types: [created]

jobs:
  # 댓글 명령어 처리
  process-comment:
    runs-on: ubuntu-latest
    if: contains(github.event.comment.body, '/ai')
    
    steps:
    - name: 코드 체크아웃
      uses: actions/checkout@v4
      
    - name: Python 설정
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: 의존성 설치
      run: |
        pip install -r requirements.txt
        pip install openai anthropic crewai
        
    - name: 댓글 명령어 파싱
      id: parse-command
      run: |
        python scripts/parse_comment_command.py \
          --comment "${{ github.event.comment.body }}" \
          --issue-number ${{ github.event.issue.number }}
          
    - name: 명령어 실행
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      run: |
        python scripts/execute_command.py \
          --command "${{ steps.parse-command.outputs.command }}" \
          --args "${{ steps.parse-command.outputs.args }}" \
          --issue-number ${{ github.event.issue.number }} \
          --comment-id ${{ github.event.comment.id }}
```

## 고급 기능

### 1. 조건부 워크플로우 실행

특정 조건에서만 워크플로우를 실행하도록 설정합니다:

```yaml
jobs:
  conditional-workflow:
    runs-on: ubuntu-latest
    if: |
      github.event_name == 'issues' && 
      github.event.action == 'opened' && 
      contains(github.event.issue.labels.*.name, 'enhancement')
    
    steps:
    - name: 조건부 실행
      run: echo "이슈가 enhancement 라벨과 함께 생성되었습니다"
```

### 2. 워크플로우 간 데이터 전달

한 워크플로우의 결과를 다른 워크플로우에서 사용할 수 있습니다:

```yaml
jobs:
  analysis:
    runs-on: ubuntu-latest
    outputs:
      analysis-result: ${{ steps.analyze.outputs.result }}
      next-action: ${{ steps.analyze.outputs.next-action }}
    
    steps:
    - name: 분석 실행
      id: analyze
      run: |
        # 분석 로직
        echo "result=analysis_complete" >> $GITHUB_OUTPUT
        echo "next-action=generate_code" >> $GITHUB_OUTPUT

  code-generation:
    runs-on: ubuntu-latest
    needs: analysis
    if: needs.analysis.outputs.next-action == 'generate_code'
    
    steps:
    - name: 코드 생성
      run: |
        echo "분석 결과: ${{ needs.analysis.outputs.analysis-result }}"
        # 코드 생성 로직
```

### 3. 에러 처리 및 재시도

워크플로우 실행 중 에러가 발생했을 때의 처리 방법:

```yaml
jobs:
  robust-workflow:
    runs-on: ubuntu-latest
    continue-on-error: true
    
    steps:
    - name: 안전한 실행
      id: safe-execution
      continue-on-error: true
      run: |
        python scripts/risky_operation.py
        
    - name: 에러 처리
      if: steps.safe-execution.outcome == 'failure'
      run: |
        echo "작업 실패, 대안 실행"
        python scripts/fallback_operation.py
        
    - name: 재시도 로직
      if: steps.safe-execution.outcome == 'failure'
      run: |
        for i in {1..3}; do
          echo "재시도 $i/3"
          python scripts/retry_operation.py && break
          sleep 10
        done
```

### 4. 워크플로우 상태 알림

워크플로우 실행 결과를 Slack이나 이메일로 알림:

```yaml
jobs:
  notify-completion:
    runs-on: ubuntu-latest
    if: always()
    
    steps:
    - name: Slack 알림
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        channel: '#ai-agents'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
        
    - name: 이메일 알림
      uses: dawidd6/action-send-mail@v3
      with:
        server_address: smtp.gmail.com
        server_port: 587
        username: ${{ secrets.EMAIL_USERNAME }}
        password: ${{ secrets.EMAIL_PASSWORD }}
        subject: "AI 워크플로우 완료: ${{ github.workflow }}"
        body: "워크플로우가 ${{ job.status }} 상태로 완료되었습니다."
        to: ${{ secrets.NOTIFICATION_EMAIL }}
```

## 디버깅 및 모니터링

### 1. 워크플로우 로그 분석

```yaml
- name: 로그 분석
  run: |
    echo "워크플로우 실행 정보:"
    echo "이벤트: ${{ github.event_name }}"
    echo "액션: ${{ github.event.action }}"
    echo "브랜치: ${{ github.ref }}"
    echo "커밋: ${{ github.sha }}"
    echo "실행자: ${{ github.actor }}"
```

### 2. 워크플로우 성능 모니터링

```yaml
- name: 성능 측정
  run: |
    start_time=$(date +%s)
    # 실제 작업 수행
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    echo "작업 소요 시간: ${duration}초"
```

## 다음 단계

이 가이드를 완료한 후 다음 단계를 진행하세요:

1. **[2-3: 프런트 오피스 구축](2-3-front-office-setup.html)**: 제품 전략가 에이전트 구축하기
2. **[2-4: 공장 플로어 구축](2-4-factory-floor-construction.html)**: 개발자 팀 오케스트레이션하기
3. **[시리즈 3: 디지털 인력 관리](../series-3/3-1-gendd-model.html)**: AI 팀 관리 방법 학습하기

## 추가 리소스

- [GitHub Actions 이벤트 참조](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
- [워크플로우 조건부 실행](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif)
- [에이전틱 프로젝트 예제](../examples/github-actions/)
- [AI 에이전트 통합 가이드](../series-1/1-9-crewai-team-building.html)

---

**"이슈 하나로 시작하는 자동화"** - GitHub 이슈를 트리거로 AI 에이전트가 자동으로 반응하는 시스템을 구축하고 진정한 자동화의 시작을 경험하세요!