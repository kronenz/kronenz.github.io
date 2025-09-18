---
layout: default
title: "2-9-self-healing-tests: 2 9 self healing tests"
description: "에이전틱 SaaS 조직 가이드"
order: 11
permalink: /automation-factory/2-9-self-healing-tests/
---

# 자가 치유 테스트의 구현

## UI 변경에 자동으로 적응하는 회복탄력성 있는 QA 시스템

## 📖 개요

이 가이드는 UI 변경이나 요소 식별자 변경에 자동으로 적응하여 테스트가 계속 작동하도록 하는 자가 치유 테스트 시스템을 구축하는 방법을 다룹니다. 테스트의 안정성과 유지보수성을 크게 향상시킵니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

- 자가 치유 테스트 개념 이해 및 설계
- 동적 요소 선택자 시스템 구현
- 테스트 안정성 향상 메커니즘 구축
- 실패 시 자동 수정 시스템 개발
- AI 기반 요소 식별 및 매칭 시스템 구현

## 📋 사전 요구사항

- Selenium/Playwright 기본 지식
- Python 중급 수준
- 머신러닝 기본 개념
- 웹 개발 기본 지식

## ⏱️ 예상 소요 시간

**4시간** (난이도: 고급)

## 🔧 필요한 도구

- Python 3.8+
- Git
- 텍스트 에디터 (VS Code 권장)
- 터미널/명령 프롬프트

## 📚 핵심 개념

### 자가 치유 테스트의 원리

테스트가 실패했을 때 자동으로 원인을 분석하고 수정하여 다시 실행하는 메커니즘을 이해합니다.

### 동적 요소 선택 전략

고정된 선택자 대신 여러 속성을 조합하여 요소를 식별하는 동적 선택 전략을 수립합니다.

### AI 기반 요소 매칭

컴퓨터 비전과 자연어 처리를 활용하여 UI 요소를 지능적으로 식별하는 방법을 학습합니다.


## 🛠️ 실습 단계

### 요소 식별자 다중화

하나의 요소를 여러 방법으로 식별할 수 있는 시스템을 구축합니다.

### 실패 분석 시스템 구현

테스트 실패 원인을 자동으로 분석하고 분류하는 시스템을 개발합니다.

### 자동 수정 메커니즘 구축

분석된 실패 원인에 따라 자동으로 테스트를 수정하는 시스템을 구현합니다.

### 학습 및 개선 시스템

수정 경험을 학습하여 향후 유사한 문제를 더 빠르게 해결하는 시스템을 구축합니다.


## 💻 코드 예제

### 자가 치유 요소 찾기

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

class SelfHealingElementFinder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)
    
    def find_element_with_healing(self, element_info):
        """자가 치유 기능이 있는 요소 찾기"""
        strategies = [
            self.find_by_multiple_selectors,
            self.find_by_text_similarity,
            self.find_by_position,
            self.find_by_visual_similarity
        ]
        
        for strategy in strategies:
            try:
                element = strategy(element_info)
                if element:
                    self.logger.info(f"Element found using {strategy.__name__}")
                    return element
            except Exception as e:
                self.logger.warning(f"Strategy {strategy.__name__} failed: {e}")
                continue
        
        raise Exception(f"Could not find element: {element_info}")
    
    def find_by_multiple_selectors(self, element_info):
        """여러 선택자로 요소 찾기"""
        selectors = element_info.get('selectors', [])
        
        for selector in selectors:
            try:
                if selector['type'] == 'id':
                    return self.driver.find_element(By.ID, selector['value'])
                elif selector['type'] == 'class':
                    return self.driver.find_element(By.CLASS_NAME, selector['value'])
                elif selector['type'] == 'xpath':
                    return self.driver.find_element(By.XPATH, selector['value'])
                elif selector['type'] == 'css':
                    return self.driver.find_element(By.CSS_SELECTOR, selector['value'])
            except:
                continue
        
        return None
    
    def find_by_text_similarity(self, element_info):
        """텍스트 유사도로 요소 찾기"""
        target_text = element_info.get('text', '')
        if not target_text:
            return None
        
        # 모든 텍스트 요소 찾기
        text_elements = self.driver.find_elements(By.XPATH, "//*[text()]")
        
        best_match = None
        best_similarity = 0
        
        for element in text_elements:
            element_text = element.text
            similarity = self.calculate_text_similarity(target_text, element_text)
            
            if similarity > best_similarity and similarity > 0.8:
                best_similarity = similarity
                best_match = element
        
        return best_match
    
    def calculate_text_similarity(self, text1, text2):
        """텍스트 유사도 계산"""
        from difflib import SequenceMatcher
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()
    
    def find_by_position(self, element_info):
        """위치 기반 요소 찾기"""
        position = element_info.get('position')
        if not position:
            return None
        
        # 위치 근처의 요소들 찾기
        x, y = position['x'], position['y']
        tolerance = 50  # 픽셀 허용 오차
        
        elements = self.driver.find_elements(By.XPATH, "//*")
        
        for element in elements:
            try:
                location = element.location
                size = element.size
                
                if (abs(location['x'] - x) < tolerance and 
                    abs(location['y'] - y) < tolerance):
                    return element
            except:
                continue
        
        return None
```

### 테스트 자동 수정 시스템

```python
class TestSelfHealer:
    def __init__(self, driver):
        self.driver = driver
        self.element_finder = SelfHealingElementFinder(driver)
        self.healing_history = []
    
    def execute_test_with_healing(self, test_steps):
        """자가 치유 기능이 있는 테스트 실행"""
        for step in test_steps:
            try:
                self.execute_step(step)
            except Exception as e:
                self.logger.warning(f"Step failed: {e}")
                
                # 자가 치유 시도
                if self.attempt_healing(step, e):
                    self.logger.info("Healing successful, retrying step")
                    self.execute_step(step)
                else:
                    self.logger.error("Healing failed, test cannot continue")
                    raise
    
    def execute_step(self, step):
        """테스트 스텝 실행"""
        action = step['action']
        element_info = step['element']
        
        element = self.element_finder.find_element_with_healing(element_info)
        
        if action == 'click':
            element.click()
        elif action == 'type':
            element.clear()
            element.send_keys(step['value'])
        elif action == 'verify':
            expected = step['expected']
            actual = element.text
            assert expected in actual, f"Expected '{expected}' but got '{actual}'"
    
    def attempt_healing(self, step, error):
        """테스트 스텝 자가 치유 시도"""
        healing_strategies = [
            self.update_element_selectors,
            self.wait_for_element_load,
            self.refresh_page_and_retry,
            self.use_alternative_element
        ]
        
        for strategy in healing_strategies:
            try:
                if strategy(step, error):
                    self.healing_history.append({
                        'step': step,
                        'error': str(error),
                        'strategy': strategy.__name__,
                        'success': True
                    })
                    return True
            except Exception as healing_error:
                self.logger.warning(f"Healing strategy {strategy.__name__} failed: {healing_error}")
                continue
        
        return False
    
    def update_element_selectors(self, step, error):
        """요소 선택자 업데이트"""
        element_info = step['element']
        
        # 현재 페이지에서 요소 다시 찾기
        new_element = self.element_finder.find_element_with_healing(element_info)
        
        if new_element:
            # 새로운 선택자 정보 업데이트
            element_info['selectors'] = self.extract_element_selectors(new_element)
            return True
        
        return False
    
    def wait_for_element_load(self, step, error):
        """요소 로딩 대기"""
        time.sleep(2)  # 추가 대기 시간
        
        element_info = step['element']
        element = self.element_finder.find_element_with_healing(element_info)
        
        return element is not None
    
    def refresh_page_and_retry(self, step, error):
        """페이지 새로고침 후 재시도"""
        self.driver.refresh()
        time.sleep(3)
        
        element_info = step['element']
        element = self.element_finder.find_element_with_healing(element_info)
        
        return element is not None
```


## 🔍 고급 기능


## 🚨 문제 해결


## 📖 추가 리소스

- [Selenium WebDriver 문서](https://selenium-python.readthedocs.io/)
- [OpenCV Python](https://opencv-python-tutroals.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/)

## 🚀 다음 단계

이 가이드를 완료한 후 다음 가이드들을 학습해보세요:

- [출하 부두 구축](2-10-shipping-dock-setup.md)
- [엔드-투-엔드 프로젝트](2-11-end-to-end-project.md)

## 📝 요약

이 가이드에서는 자가 치유 테스트의 구현에 대해 학습했습니다. 주요 내용은 다음과 같습니다:

- 자가 치유 테스트 개념 이해 및 설계
- 동적 요소 선택자 시스템 구현
- 테스트 안정성 향상 메커니즘 구축
- 실패 시 자동 수정 시스템 개발
- AI 기반 요소 식별 및 매칭 시스템 구현

다음 가이드에서는 더 고급 주제를 다룰 예정입니다.

---

**"자가 치유 테스트의 구현"** - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드