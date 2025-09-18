---
title: 테스트 자동화
date: 2025-09-18 20:04:21
updated: 2025-09-18 20:04:21
categories: ["AI 가이드"]
tags: ["AI", "가이드", "자동화"]
permalink: /series-2/2-8-test-automation/
excerpt: 
toc: True
mathjax: True
comments: True
series:
  id: series-2
  title: 시리즈 2: 자동화된 SaaS 팩토리 - 조립 라인 구축 가이드
  position: 1
---
<h1 id="_1">테스트 자동화</h1>
<h2 id="gherkin-seleniumplaywright">Gherkin 시나리오를 Selenium/Playwright 스크립트로 변환하고 실행하기</h2>
<h2 id="_2">📖 개요</h2>
<p>이 가이드는 Gherkin 형식의 테스트 시나리오를 실제 실행 가능한 Selenium/Playwright 스크립트로 변환하고 자동으로 실행하는 방법을 다룹니다. 완전 자동화된 테스트 파이프라인을 구축합니다.</p>
<h2 id="_3">🎯 학습 목표</h2>
<p>이 가이드를 완료하면 다음을 달성할 수 있습니다:</p>
<ul>
<li>테스트 자동화 도구 선택 및 설정</li>
<li>Gherkin to Code 변환 시스템 구축</li>
<li>테스트 실행 환경 구축 및 최적화</li>
<li>결과 보고서 자동 생성 시스템 구현</li>
<li>CI/CD 파이프라인과 테스트 통합</li>
</ul>
<h2 id="_4">📋 사전 요구사항</h2>
<ul>
<li>Selenium 또는 Playwright 기본 지식</li>
<li>Python 중급 수준</li>
<li>CI/CD 개념 이해</li>
<li>Docker 기본 지식</li>
</ul>
<h2 id="_5">⏱️ 예상 소요 시간</h2>
<p><strong>3시간</strong> (난이도: 중급)</p>
<h2 id="_6">🔧 필요한 도구</h2>
<ul>
<li>Python 3.8+</li>
<li>Git</li>
<li>텍스트 에디터 (VS Code 권장)</li>
<li>터미널/명령 프롬프트</li>
</ul>
<h2 id="_7">📚 핵심 개념</h2>
<h3 id="_8">테스트 자동화 아키텍처</h3>
<p>Gherkin 시나리오를 실제 테스트 코드로 변환하고 실행하는 전체 아키텍처를 설계합니다.</p>
<h3 id="_9">도구 선택 기준</h3>
<p>Selenium과 Playwright의 장단점을 비교하여 프로젝트에 적합한 도구를 선택하는 방법을 학습합니다.</p>
<h3 id="_10">테스트 실행 최적화</h3>
<p>병렬 실행, 리소스 관리, 안정성 향상을 위한 테스트 실행 최적화 전략을 수립합니다.</p>
<h2 id="_11">🛠️ 실습 단계</h2>
<h3 id="_12">테스트 환경 구축</h3>
<p>Docker를 사용하여 일관된 테스트 실행 환경을 구축합니다.</p>
<h3 id="gherkin">Gherkin 파서 구현</h3>
<p>Gherkin 문법을 파싱하여 테스트 스텝을 추출하는 시스템을 구현합니다.</p>
<h3 id="_13">코드 생성기 개발</h3>
<p>파싱된 테스트 스텝을 실제 테스트 코드로 변환하는 생성기를 개발합니다.</p>
<h3 id="_14">테스트 실행 및 리포팅</h3>
<p>생성된 테스트를 실행하고 결과를 수집하여 보고서를 생성하는 시스템을 구축합니다.</p>
<h2 id="_15">💻 코드 예제</h2>
<h3 id="gherkin_1">Gherkin 파서 및 코드 생성기</h3>
<pre class="codehilite"><code class="language-python">import re
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

    def parse_gherkin(self, gherkin_content: str) -&gt; List[Dict]:
        &quot;&quot;&quot;Gherkin 내용을 파싱하여 테스트 스텝 추출&quot;&quot;&quot;
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

    def convert_to_selenium(self, scenarios: List[Dict]) -&gt; str:
        &quot;&quot;&quot;시나리오를 Selenium 테스트 코드로 변환&quot;&quot;&quot;
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
        &quot;&quot;&quot;{scenario['name']}&quot;&quot;&quot;
'''

            for step in scenario['steps']:
                step_code = self.convert_step(step)
                test_method += f'        {step_code}\n'

            test_code += test_method

        return test_code

    def convert_step(self, step: Dict) -&gt; str:
        &quot;&quot;&quot;개별 스텝을 Selenium 코드로 변환&quot;&quot;&quot;
        step_type = step['type']
        content = step['content']

        if step_type in self.step_definitions:
            return self.step_definitions[step_type](content)
        else:
            return f'# TODO: Convert {step_type} step: {content}'

    def convert_given_step(self, content: str) -&gt; str:
        &quot;&quot;&quot;Given 스텝 변환&quot;&quot;&quot;
        if 'user is on' in content.lower():
            url = re.search(r&quot;'([^']+)'&quot;, content)
            if url:
                return f'self.driver.get(&quot;{url.group(1)}&quot;)'
        elif 'user is logged in' in content.lower():
            return 'self.login_user()'

        return f'# Given: {content}'

    def convert_when_step(self, content: str) -&gt; str:
        &quot;&quot;&quot;When 스텝 변환&quot;&quot;&quot;
        if 'clicks on' in content.lower():
            element = re.search(r&quot;'([^']+)'&quot;, content)
            if element:
                return f'self.driver.find_element(By.XPATH, &quot;//*[text()=\&quot;{element.group(1)}\&quot;]&quot;).click()'
        elif 'enters' in content.lower():
            field = re.search(r&quot;'([^']+)'&quot;, content)
            value = re.search(r&quot;'([^']+)'&quot;, content[content.find(&quot;enters&quot;) + 7:])
            if field and value:
                return f'self.driver.find_element(By.NAME, &quot;{field.group(1)}&quot;).send_keys(&quot;{value.group(1)}&quot;)'

        return f'# When: {content}'

    def convert_then_step(self, content: str) -&gt; str:
        &quot;&quot;&quot;Then 스텝 변환&quot;&quot;&quot;
        if 'should see' in content.lower():
            text = re.search(r&quot;'([^']+)'&quot;, content)
            if text:
                return f'assert &quot;{text.group(1)}&quot; in self.driver.page_source'
        elif 'should be redirected to' in content.lower():
            url = re.search(r&quot;'([^']+)'&quot;, content)
            if url:
                return f'assert &quot;{url.group(1)}&quot; in self.driver.current_url'

        return f'# Then: {content}'
</code></pre>

<h3 id="_16">테스트 실행 및 리포팅</h3>
<pre class="codehilite"><code class="language-python">import subprocess
import json
import xml.etree.ElementTree as ET
from datetime import datetime

class TestRunner:
    def __init__(self, test_directory):
        self.test_directory = test_directory

    def run_tests(self, test_file):
        &quot;&quot;&quot;테스트 실행&quot;&quot;&quot;
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
        &quot;&quot;&quot;테스트 결과 파싱&quot;&quot;&quot;
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
        &quot;&quot;&quot;HTML 보고서 생성&quot;&quot;&quot;
        html_template = f&quot;&quot;&quot;
        &lt;!DOCTYPE html&gt;
        &lt;html&gt;
        &lt;head&gt;
            &lt;title&gt;Test Report&lt;/title&gt;
            &lt;style&gt;
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
                .summary {{ margin: 20px 0; }}}
                .test-case {{ margin: 10px 0; padding: 10px; border: 1px solid #ddd; }}
                .passed {{ background-color: #d4edda; }}
                .failed {{ background-color: #f8d7da; }}
            &lt;/style&gt;
        &lt;/head&gt;
        &lt;body&gt;
            &lt;div class=&quot;header&quot;&gt;
                &lt;h1&gt;Test Execution Report&lt;/h1&gt;
                &lt;p&gt;Generated at: {results['timestamp']}&lt;/p&gt;
            &lt;/div&gt;

            &lt;div class=&quot;summary&quot;&gt;
                &lt;h2&gt;Summary&lt;/h2&gt;
                &lt;p&gt;Total Tests: {results['total_tests']}&lt;/p&gt;
                &lt;p&gt;Passed: {results['passed']}&lt;/p&gt;
                &lt;p&gt;Failed: {results['failed']}&lt;/p&gt;
                &lt;p&gt;Duration: {results['duration']:.2f}s&lt;/p&gt;
            &lt;/div&gt;

            &lt;div class=&quot;test-cases&quot;&gt;
                &lt;h2&gt;Test Cases&lt;/h2&gt;
                {self.generate_test_case_html(results.get('details', []))}
            &lt;/div&gt;
        &lt;/body&gt;
        &lt;/html&gt;
        &quot;&quot;&quot;

        with open(f'{self.test_directory}/test_report.html', 'w') as f:
            f.write(html_template)

        return f'{self.test_directory}/test_report.html'
</code></pre>

<h2 id="_17">🔍 고급 기능</h2>
<h2 id="_18">🚨 문제 해결</h2>
<h2 id="_19">📖 추가 리소스</h2>
<ul>
<li><a href="https://selenium-python.readthedocs.io/">Selenium Python 문서</a></li>
<li><a href="https://playwright.dev/python/">Playwright Python</a></li>
<li><a href="https://docs.pytest.org/">pytest 문서</a></li>
</ul>
<h2 id="_20">🚀 다음 단계</h2>
<p>이 가이드를 완료한 후 다음 가이드들을 학습해보세요:</p>
<ul>
<li><a href="2-9-self-healing-tests.md">자가 치유 테스트의 구현</a></li>
<li><a href="2-10-shipping-dock-setup.md">출하 부두 구축</a></li>
</ul>
<h2 id="_21">📝 요약</h2>
<p>이 가이드에서는 테스트 자동화에 대해 학습했습니다. 주요 내용은 다음과 같습니다:</p>
<ul>
<li>테스트 자동화 도구 선택 및 설정</li>
<li>Gherkin to Code 변환 시스템 구축</li>
<li>테스트 실행 환경 구축 및 최적화</li>
<li>결과 보고서 자동 생성 시스템 구현</li>
<li>CI/CD 파이프라인과 테스트 통합</li>
</ul>
<p>다음 가이드에서는 더 고급 주제를 다룰 예정입니다.</p>
<hr />
<p><strong>"테스트 자동화"</strong> - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드</p>