---
layout: default
title: "2-8-test-automation: 2 8 test automation"
description: "에이전틱 SaaS 조직 가이드"
order: 10
---

# 테스트 자동화

## Gherkin 시나리오를 Selenium/Playwright 스크립트로 변환하고 실행하기

## 📖 개요

이 가이드는 Gherkin 형식의 테스트 시나리오를 실제 실행 가능한 Selenium/Playwright 스크립트로 변환하고 자동으로 실행하는 방법을 다룹니다. 완전 자동화된 테스트 파이프라인을 구축합니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

- 테스트 자동화 도구 선택 및 설정
- Gherkin to Code 변환 시스템 구축
- 테스트 실행 환경 구축 및 최적화
- 결과 보고서 자동 생성 시스템 구현
- CI/CD 파이프라인과 테스트 통합

## 📋 사전 요구사항

- Selenium 또는 Playwright 기본 지식
- Python 중급 수준
- CI/CD 개념 이해
- Docker 기본 지식

## ⏱️ 예상 소요 시간

**3시간** (난이도: 중급)

## 🔧 필요한 도구

- Python 3.8+
- Git
- 텍스트 에디터 (VS Code 권장)
- 터미널/명령 프롬프트

## 📚 핵심 개념

### 테스트 자동화 아키텍처

Gherkin 시나리오를 실제 테스트 코드로 변환하고 실행하는 전체 아키텍처를 설계합니다.

### 도구 선택 기준

Selenium과 Playwright의 장단점을 비교하여 프로젝트에 적합한 도구를 선택하는 방법을 학습합니다.

### 테스트 실행 최적화

병렬 실행, 리소스 관리, 안정성 향상을 위한 테스트 실행 최적화 전략을 수립합니다.


## 🛠️ 실습 단계

### 테스트 환경 구축

Docker를 사용하여 일관된 테스트 실행 환경을 구축합니다.

### Gherkin 파서 구현

Gherkin 문법을 파싱하여 테스트 스텝을 추출하는 시스템을 구현합니다.

### 코드 생성기 개발

파싱된 테스트 스텝을 실제 테스트 코드로 변환하는 생성기를 개발합니다.

### 테스트 실행 및 리포팅

생성된 테스트를 실행하고 결과를 수집하여 보고서를 생성하는 시스템을 구축합니다.


## 💻 코드 예제

### Gherkin 파서 및 코드 생성기

```python
import re
from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GherkinToSeleniumConverter:
    def __init__(self):
        self.step_definitions = {
            'given': self.convert_given_step,
            'when': self.convert_when_step,
            'then': self.convert_then_step
        }
    
    def parse_gherkin(self, gherkin_content: str) -> List[Dict]:
        """Gherkin 내용을 파싱하여 테스트 스텝 추출"""
        scenarios = []
        current_scenario = None
        
        for line in gherkin_content.split('\n'):
            line = line.strip()
            
            if line.startswith('Scenario:'):
                if current_scenario:
                    scenarios.append(current_scenario)
                current_scenario = {
                    'name': line.replace('Scenario:', '').strip(),
                    'steps': []
                }
            elif line.startswith(('Given', 'When', 'Then', 'And', 'But')):
                if current_scenario:
                    step_type = line.split()[0].lower()
                    step_content = ' '.join(line.split()[1:])
                    current_scenario['steps'].append({
                        'type': step_type,
                        'content': step_content
                    })
        
        if current_scenario:
            scenarios.append(current_scenario)
        
        return scenarios
    
    def convert_to_selenium(self, scenarios: List[Dict]) -> str:
        """시나리오를 Selenium 테스트 코드로 변환"""
        test_code = '''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class GeneratedTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def tearDown(self):
        self.driver.quit()
'''
        
        for i, scenario in enumerate(scenarios):
            test_method = f'''
    def test_{scenario['name'].lower().replace(' ', '_')}(self):
        """{scenario['name']}"""
'''
            
            for step in scenario['steps']:
                step_code = self.convert_step(step)
                test_method += f'        {step_code}\n'
            
            test_code += test_method
        
        return test_code
    
    def convert_step(self, step: Dict) -> str:
        """개별 스텝을 Selenium 코드로 변환"""
        step_type = step['type']
        content = step['content']
        
        if step_type in self.step_definitions:
            return self.step_definitions[step_type](content)
        else:
            return f'# TODO: Convert {step_type} step: {content}'
    
    def convert_given_step(self, content: str) -> str:
        """Given 스텝 변환"""
        if 'user is on' in content.lower():
            url = re.search(r"'([^']+)'", content)
            if url:
                return f'self.driver.get("{url.group(1)}")'
        elif 'user is logged in' in content.lower():
            return 'self.login_user()'
        
        return f'# Given: {content}'
    
    def convert_when_step(self, content: str) -> str:
        """When 스텝 변환"""
        if 'clicks on' in content.lower():
            element = re.search(r"'([^']+)'", content)
            if element:
                return f'self.driver.find_element(By.XPATH, "//*[text()=\"{element.group(1)}\"]").click()'
        elif 'enters' in content.lower():
            field = re.search(r"'([^']+)'", content)
            value = re.search(r"'([^']+)'", content[content.find("enters") + 7:])
            if field and value:
                return f'self.driver.find_element(By.NAME, "{field.group(1)}").send_keys("{value.group(1)}")'
        
        return f'# When: {content}'
    
    def convert_then_step(self, content: str) -> str:
        """Then 스텝 변환"""
        if 'should see' in content.lower():
            text = re.search(r"'([^']+)'", content)
            if text:
                return f'assert "{text.group(1)}" in self.driver.page_source'
        elif 'should be redirected to' in content.lower():
            url = re.search(r"'([^']+)'", content)
            if url:
                return f'assert "{url.group(1)}" in self.driver.current_url'
        
        return f'# Then: {content}'
```

### 테스트 실행 및 리포팅

```python
import subprocess
import json
import xml.etree.ElementTree as ET
from datetime import datetime

class TestRunner:
    def __init__(self, test_directory):
        self.test_directory = test_directory
    
    def run_tests(self, test_file):
        """테스트 실행"""
        try:
            # pytest로 테스트 실행
            result = subprocess.run(
                ['pytest', test_file, '--json-report', '--json-report-file=test_results.json'],
                capture_output=True,
                text=True,
                cwd=self.test_directory
            )
            
            # 결과 파싱
            with open(f'{self.test_directory}/test_results.json', 'r') as f:
                results = json.load(f)
            
            return self.parse_test_results(results, result.returncode)
            
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    def parse_test_results(self, results, return_code):
        """테스트 결과 파싱"""
        summary = results.get('summary', {})
        
        return {
            'status': 'passed' if return_code == 0 else 'failed',
            'total_tests': summary.get('total', 0),
            'passed': summary.get('passed', 0),
            'failed': summary.get('failed', 0),
            'skipped': summary.get('skipped', 0),
            'duration': summary.get('duration', 0),
            'timestamp': datetime.now().isoformat(),
            'details': results.get('tests', [])
        }
    
    def generate_html_report(self, results):
        """HTML 보고서 생성"""
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
                .summary {{ margin: 20px 0; }}}
                .test-case {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; }}
                .passed {{ background-color: #d4edda; }}
                .failed {{ background-color: #f8d7da; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Test Execution Report</h1>
                <p>Generated at: {results['timestamp']}</p>
            </div>
            
            <div class="summary">
                <h2>Summary</h2>
                <p>Total Tests: {results['total_tests']}</p>
                <p>Passed: {results['passed']}</p>
                <p>Failed: {results['failed']}</p>
                <p>Duration: {results['duration']:.2f}s</p>
            </div>
            
            <div class="test-cases">
                <h2>Test Cases</h2>
                {self.generate_test_case_html(results.get('details', []))}
            </div>
        </body>
        </html>
        """
        
        with open(f'{self.test_directory}/test_report.html', 'w') as f:
            f.write(html_template)
        
        return f'{self.test_directory}/test_report.html'
```


## 🔍 고급 기능


## 🚨 문제 해결


## 📖 추가 리소스

- [Selenium Python 문서](https://selenium-python.readthedocs.io/)
- [Playwright Python](https://playwright.dev/python/)
- [pytest 문서](https://docs.pytest.org/)

## 🚀 다음 단계

이 가이드를 완료한 후 다음 가이드들을 학습해보세요:

- [자가 치유 테스트의 구현](2-9-self-healing-tests.md)
- [출하 부두 구축](2-10-shipping-dock-setup.md)

## 📝 요약

이 가이드에서는 테스트 자동화에 대해 학습했습니다. 주요 내용은 다음과 같습니다:

- 테스트 자동화 도구 선택 및 설정
- Gherkin to Code 변환 시스템 구축
- 테스트 실행 환경 구축 및 최적화
- 결과 보고서 자동 생성 시스템 구현
- CI/CD 파이프라인과 테스트 통합

다음 가이드에서는 더 고급 주제를 다룰 예정입니다.

---

**"테스트 자동화"** - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드