---
title: 프런트 오피스 구축
date: 2025-09-18 20:04:21
updated: 2025-09-18 20:04:21
categories: ["AI 가이드"]
tags: ["AI", "가이드", "자동화"]
permalink: /series-2/2-3-front-office-setup/
excerpt: 
toc: True
mathjax: True
comments: True
series:
  id: series-2
  title: 시리즈 2: 자동화된 SaaS 팩토리 - 조립 라인 구축 가이드
  position: 1
---
<h1 id="_1">프런트 오피스 구축</h1>
<h2 id="_2">이슈를 분석하여 명세와 계획을 자동 생성하는 제품 전략가 에이전트</h2>
<h2 id="_3">📖 개요</h2>
<p>이 가이드는 GitHub 이슈를 분석하여 자동으로 명세서와 개발 계획을 생성하는 제품 전략가 AI 에이전트를 구축하는 방법을 다룹니다. 이는 완전 자동화된 개발 파이프라인의 첫 번째 단계입니다.</p>
<h2 id="_4">🎯 학습 목표</h2>
<p>이 가이드를 완료하면 다음을 달성할 수 있습니다:</p>
<ul>
<li>제품 전략가 에이전트의 역할과 책임 이해</li>
<li>이슈 분석 알고리즘 설계 및 구현</li>
<li>명세서 자동 생성 시스템 구축</li>
<li>요구사항 우선순위 설정 로직 개발</li>
<li>AI 에이전트와 GitHub Actions 연동 구현</li>
</ul>
<h2 id="_5">📋 사전 요구사항</h2>
<ul>
<li>GitHub Actions 기본 개념 숙지</li>
<li>OpenAI API 또는 Claude API 사용 경험</li>
<li>Python 중급 수준</li>
<li>명세 기반 개발(SDD) 개념 이해</li>
</ul>
<h2 id="_6">⏱️ 예상 소요 시간</h2>
<p><strong>4시간</strong> (난이도: 고급)</p>
<h2 id="_7">🔧 필요한 도구</h2>
<ul>
<li>Python 3.8+</li>
<li>Git</li>
<li>텍스트 에디터 (VS Code 권장)</li>
<li>터미널/명령 프롬프트</li>
</ul>
<h2 id="_8">📚 핵심 개념</h2>
<h3 id="_9">제품 전략가 에이전트의 역할</h3>
<p>제품 전략가 에이전트는 비즈니스 요구사항을 분석하고, 기술적 명세로 변환하며, 개발 우선순위를 설정하는 핵심 역할을 담당합니다.</p>
<h3 id="_10">이슈 분석 프로세스</h3>
<p>이슈의 제목, 내용, 라벨, 댓글 등을 종합적으로 분석하여 요구사항을 추출하고 분류하는 프로세스를 설계합니다.</p>
<h3 id="_11">명세서 생성 전략</h3>
<p>분석된 요구사항을 바탕으로 명확하고 실행 가능한 명세서를 자동 생성하는 전략을 수립합니다.</p>
<h2 id="_12">🛠️ 실습 단계</h2>
<h3 id="ai">AI 에이전트 기본 구조 설정</h3>
<p>CrewAI를 사용하여 제품 전략가 에이전트의 기본 구조를 설정합니다.</p>
<h3 id="_13">이슈 분석 모듈 구현</h3>
<p>GitHub API를 사용하여 이슈 정보를 가져오고 분석하는 모듈을 구현합니다.</p>
<h3 id="_14">명세서 생성 로직 개발</h3>
<p>분석된 요구사항을 바탕으로 spec.md 파일을 자동 생성하는 로직을 개발합니다.</p>
<h3 id="github-actions">GitHub Actions 워크플로우 연동</h3>
<p>에이전트를 GitHub Actions 워크플로우에 통합하여 자동 실행되도록 설정합니다.</p>
<h2 id="_15">💻 코드 예제</h2>
<h3 id="_16">제품 전략가 에이전트 클래스</h3>
<pre class="codehilite"><code class="language-python">from crewai import Agent, Task, Crew
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
</code></pre>

<h3 id="github-actions_1">GitHub Actions 워크플로우</h3>
<pre class="codehilite"><code class="language-yaml">name: Product Strategist Workflow

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
        git config --local user.email &quot;action@github.com&quot;
        git config --local user.name &quot;GitHub Action&quot;
        git add .
        git commit -m &quot;Auto-generated spec for issue #${{ github.event.issue.number }}&quot; || exit 0
        git push
</code></pre>

<h2 id="_17">🔍 고급 기능</h2>
<h2 id="_18">🚨 문제 해결</h2>
<h2 id="_19">📖 추가 리소스</h2>
<ul>
<li><a href="https://docs.crewai.com/">CrewAI 공식 문서</a></li>
<li><a href="https://docs.github.com/en/rest">GitHub API 문서</a></li>
<li><a href="https://platform.openai.com/docs">OpenAI API 문서</a></li>
</ul>
<h2 id="_20">🚀 다음 단계</h2>
<p>이 가이드를 완료한 후 다음 가이드들을 학습해보세요:</p>
<ul>
<li><a href="2-4-factory-floor-construction.md">공장 플로어 구축</a></li>
<li><a href="2-5-autonomous-commits-prs.md">자율적 코드 커밋 및 PR 생성</a></li>
</ul>
<h2 id="_21">📝 요약</h2>
<p>이 가이드에서는 프런트 오피스 구축에 대해 학습했습니다. 주요 내용은 다음과 같습니다:</p>
<ul>
<li>제품 전략가 에이전트의 역할과 책임 이해</li>
<li>이슈 분석 알고리즘 설계 및 구현</li>
<li>명세서 자동 생성 시스템 구축</li>
<li>요구사항 우선순위 설정 로직 개발</li>
<li>AI 에이전트와 GitHub Actions 연동 구현</li>
</ul>
<p>다음 가이드에서는 더 고급 주제를 다룰 예정입니다.</p>
<hr />
<p><strong>"프런트 오피스 구축"</strong> - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드</p>