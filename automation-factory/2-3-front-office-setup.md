---
layout: default
title: "2-3-front-office-setup: 2 3 front office setup"
description: "에이전틱 SaaS 조직 가이드"
order: 5
permalink: /automation-factory/2-3-front-office-setup/
---

# 프런트 오피스 구축

## 이슈를 분석하여 명세와 계획을 자동 생성하는 제품 전략가 에이전트

## 📖 개요

이 가이드는 GitHub 이슈를 분석하여 자동으로 명세서와 개발 계획을 생성하는 제품 전략가 AI 에이전트를 구축하는 방법을 다룹니다. 이는 완전 자동화된 개발 파이프라인의 첫 번째 단계입니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

- 제품 전략가 에이전트의 역할과 책임 이해
- 이슈 분석 알고리즘 설계 및 구현
- 명세서 자동 생성 시스템 구축
- 요구사항 우선순위 설정 로직 개발
- AI 에이전트와 GitHub Actions 연동 구현

## 📋 사전 요구사항

- GitHub Actions 기본 개념 숙지
- OpenAI API 또는 Claude API 사용 경험
- Python 중급 수준
- 명세 기반 개발(SDD) 개념 이해

## ⏱️ 예상 소요 시간

**4시간** (난이도: 고급)

## 🔧 필요한 도구

- Python 3.8+
- Git
- 텍스트 에디터 (VS Code 권장)
- 터미널/명령 프롬프트

## 📚 핵심 개념

### 제품 전략가 에이전트의 역할

제품 전략가 에이전트는 비즈니스 요구사항을 분석하고, 기술적 명세로 변환하며, 개발 우선순위를 설정하는 핵심 역할을 담당합니다.

### 이슈 분석 프로세스

이슈의 제목, 내용, 라벨, 댓글 등을 종합적으로 분석하여 요구사항을 추출하고 분류하는 프로세스를 설계합니다.

### 명세서 생성 전략

분석된 요구사항을 바탕으로 명확하고 실행 가능한 명세서를 자동 생성하는 전략을 수립합니다.


## 🛠️ 실습 단계

### AI 에이전트 기본 구조 설정

CrewAI를 사용하여 제품 전략가 에이전트의 기본 구조를 설정합니다.

### 이슈 분석 모듈 구현

GitHub API를 사용하여 이슈 정보를 가져오고 분석하는 모듈을 구현합니다.

### 명세서 생성 로직 개발

분석된 요구사항을 바탕으로 spec.md 파일을 자동 생성하는 로직을 개발합니다.

### GitHub Actions 워크플로우 연동

에이전트를 GitHub Actions 워크플로우에 통합하여 자동 실행되도록 설정합니다.


## 💻 코드 예제

### 제품 전략가 에이전트 클래스

```python
from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
import requests
import json

class ProductStrategistAgent:
    def __init__(self, github_token, openai_api_key):
        self.github_token = github_token
        self.llm = OpenAI(openai_api_key=openai_api_key)
        
        self.agent = Agent(
            role='Product Strategist',
            goal='Analyze GitHub issues and generate detailed specifications',
            backstory='''You are an expert product strategist with deep experience in 
            translating business requirements into technical specifications. 
            You excel at understanding user needs and creating actionable plans.''',
            verbose=True,
            allow_delegation=False
        )
    
    def analyze_issue(self, issue_number):
        # GitHub API를 사용하여 이슈 정보 가져오기
        issue_data = self.fetch_issue(issue_number)
        
        # 이슈 분석
        analysis = self.analyze_issue_content(issue_data)
        
        # 명세서 생성
        spec = self.generate_specification(analysis)
        
        return spec
    
    def fetch_issue(self, issue_number):
        headers = {'Authorization': f'token {self.github_token}'}
        url = f'https://api.github.com/repos/{{owner}}/{{repo}}/issues/{issue_number}'
        response = requests.get(url, headers=headers)
        return response.json()
    
    def analyze_issue_content(self, issue_data):
        # 이슈 내용 분석 로직
        pass
    
    def generate_specification(self, analysis):
        # 명세서 생성 로직
        pass
```

### GitHub Actions 워크플로우

```yaml
name: Product Strategist Workflow

on:
  issues:
    types: [opened, labeled]

jobs:
  product-strategy:
    if: contains(github.event.issue.labels.*.name, 'needs-spec')
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install crewai openai requests
    
    - name: Run Product Strategist Agent
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
      run: |
        python scripts/product_strategist.py \
          --issue-number ${{ github.event.issue.number }}
    
    - name: Commit generated spec
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add .
        git commit -m "Auto-generated spec for issue #${{ github.event.issue.number }}" || exit 0
        git push
```


## 🔍 고급 기능


## 🚨 문제 해결


## 📖 추가 리소스

- [CrewAI 공식 문서](https://docs.crewai.com/)
- [GitHub API 문서](https://docs.github.com/en/rest)
- [OpenAI API 문서](https://platform.openai.com/docs)

## 🚀 다음 단계

이 가이드를 완료한 후 다음 가이드들을 학습해보세요:

- [공장 플로어 구축](2-4-factory-floor-construction.md)
- [자율적 코드 커밋 및 PR 생성](2-5-autonomous-commits-prs.md)

## 📝 요약

이 가이드에서는 프런트 오피스 구축에 대해 학습했습니다. 주요 내용은 다음과 같습니다:

- 제품 전략가 에이전트의 역할과 책임 이해
- 이슈 분석 알고리즘 설계 및 구현
- 명세서 자동 생성 시스템 구축
- 요구사항 우선순위 설정 로직 개발
- AI 에이전트와 GitHub Actions 연동 구현

다음 가이드에서는 더 고급 주제를 다룰 예정입니다.

---

**"프런트 오피스 구축"** - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드