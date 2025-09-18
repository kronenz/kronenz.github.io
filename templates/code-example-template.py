#!/usr/bin/env python3
"""
[파일명]: [파일 설명]
[가이드]: [관련 가이드 링크]
[작성일]: [작성 날짜]
[작성자]: [작성자 정보]
"""

# 표준 라이브러리 임포트
import os
import sys
import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

# 서드파티 라이브러리 임포트
# import openai
# import anthropic
# from langchain import LangChain
# from crewai import Agent, Task, Crew

# 로컬 모듈 임포트
# from .utils import helper_function
# from .config import settings


class ExampleClass:
    """
    [클래스 설명]
    
    이 클래스는 [클래스의 목적과 기능]을 제공합니다.
    
    Attributes:
        attribute1 (type): [속성 설명]
        attribute2 (type): [속성 설명]
    
    Example:
        >>> example = ExampleClass("value1", "value2")
        >>> result = example.example_method()
        >>> print(result)
    """
    
    def __init__(self, param1: str, param2: str = "default"):
        """
        클래스 초기화
        
        Args:
            param1 (str): [매개변수 설명]
            param2 (str, optional): [매개변수 설명]. Defaults to "default".
        
        Raises:
            ValueError: [예외 조건 설명]
        """
        self.param1 = param1
        self.param2 = param2
        self._private_attribute = None
        
        # 초기화 검증
        if not param1:
            raise ValueError("param1은 빈 값일 수 없습니다.")
    
    def public_method(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        [메서드 설명]
        
        Args:
            input_data (Dict[str, Any]): [입력 데이터 설명]
        
        Returns:
            Dict[str, Any]: [반환값 설명]
        
        Raises:
            ValueError: [예외 조건 설명]
            RuntimeError: [예외 조건 설명]
        
        Example:
            >>> example = ExampleClass("test")
            >>> result = example.public_method({"key": "value"})
            >>> print(result["status"])
        """
        try:
            # 입력 검증
            if not isinstance(input_data, dict):
                raise ValueError("input_data는 딕셔너리여야 합니다.")
            
            # 메인 로직
            result = self._process_data(input_data)
            
            # 결과 반환
            return {
                "status": "success",
                "data": result,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def _private_method(self, data: Any) -> Any:
        """
        [내부 메서드 설명]
        
        Args:
            data (Any): [데이터 설명]
        
        Returns:
            Any: [반환값 설명]
        """
        # 내부 로직 구현
        return data
    
    def _process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        데이터 처리 로직
        
        Args:
            data (Dict[str, Any]): 처리할 데이터
        
        Returns:
            Dict[str, Any]: 처리된 데이터
        """
        processed = {}
        
        for key, value in data.items():
            if isinstance(value, str):
                processed[key] = value.upper()
            elif isinstance(value, (int, float)):
                processed[key] = value * 2
            else:
                processed[key] = value
        
        return processed
    
    @property
    def computed_property(self) -> str:
        """
        계산된 속성
        
        Returns:
            str: [속성 설명]
        """
        return f"{self.param1}_{self.param2}"
    
    @computed_property.setter
    def computed_property(self, value: str):
        """
        계산된 속성 설정자
        
        Args:
            value (str): [값 설명]
        """
        parts = value.split("_")
        if len(parts) == 2:
            self.param1, self.param2 = parts
    
    def __str__(self) -> str:
        """문자열 표현"""
        return f"ExampleClass(param1='{self.param1}', param2='{self.param2}')"
    
    def __repr__(self) -> str:
        """개발자용 문자열 표현"""
        return f"ExampleClass('{self.param1}', '{self.param2}')"


class AdvancedExample(ExampleClass):
    """
    [고급 클래스 설명]
    
    ExampleClass를 상속받아 [추가 기능]을 제공합니다.
    """
    
    def __init__(self, param1: str, param2: str = "default", advanced_param: str = ""):
        """
        고급 클래스 초기화
        
        Args:
            param1 (str): [매개변수 설명]
            param2 (str, optional): [매개변수 설명]. Defaults to "default".
            advanced_param (str, optional): [고급 매개변수 설명]. Defaults to "".
        """
        super().__init__(param1, param2)
        self.advanced_param = advanced_param
        self.history = []
    
    def advanced_method(self, data: List[Any]) -> List[Any]:
        """
        [고급 메서드 설명]
        
        Args:
            data (List[Any]): [입력 데이터 설명]
        
        Returns:
            List[Any]: [반환값 설명]
        """
        results = []
        
        for item in data:
            try:
                # 고급 처리 로직
                processed_item = self._advanced_processing(item)
                results.append(processed_item)
                
                # 히스토리 기록
                self.history.append({
                    "item": item,
                    "result": processed_item,
                    "timestamp": datetime.now().isoformat()
                })
                
            except Exception as e:
                # 에러 처리
                results.append({
                    "error": str(e),
                    "original_item": item
                })
        
        return results
    
    def _advanced_processing(self, item: Any) -> Any:
        """
        고급 처리 로직
        
        Args:
            item (Any): 처리할 아이템
        
        Returns:
            Any: 처리된 아이템
        """
        # 고급 처리 구현
        if isinstance(item, str):
            return f"[{self.advanced_param}] {item}"
        elif isinstance(item, (int, float)):
            return item ** 2
        else:
            return item


def utility_function(param1: str, param2: Optional[str] = None) -> str:
    """
    [유틸리티 함수 설명]
    
    Args:
        param1 (str): [매개변수 설명]
        param2 (Optional[str], optional): [매개변수 설명]. Defaults to None.
    
    Returns:
        str: [반환값 설명]
    
    Example:
        >>> result = utility_function("hello", "world")
        >>> print(result)
        "hello_world"
    """
    if param2 is None:
        return param1
    
    return f"{param1}_{param2}"


def async_example() -> None:
    """
    비동기 처리 예제
    """
    import asyncio
    
    async def async_task(task_id: int) -> str:
        """비동기 작업"""
        await asyncio.sleep(1)  # 비동기 대기
        return f"Task {task_id} completed"
    
    async def main():
        """메인 비동기 함수"""
        tasks = [async_task(i) for i in range(5)]
        results = await asyncio.gather(*tasks)
        
        for result in results:
            print(result)
    
    # 비동기 실행
    asyncio.run(main())


def error_handling_example():
    """
    에러 처리 예제
    """
    try:
        # 위험한 작업
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"0으로 나누기 에러: {e}")
    except Exception as e:
        print(f"예상치 못한 에러: {e}")
    else:
        print("에러 없이 실행됨")
    finally:
        print("항상 실행되는 정리 코드")


def configuration_example():
    """
    설정 관리 예제
    """
    # 환경 변수에서 설정 읽기
    api_key = os.getenv("API_KEY", "default_key")
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    
    # 설정 딕셔너리
    config = {
        "api_key": api_key,
        "debug_mode": debug_mode,
        "timeout": int(os.getenv("TIMEOUT", "30")),
        "retry_count": int(os.getenv("RETRY_COUNT", "3"))
    }
    
    return config


def logging_example():
    """
    로깅 예제
    """
    import logging
    
    # 로거 설정
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    # 핸들러 설정
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # 로그 메시지
    logger.info("정보 메시지")
    logger.warning("경고 메시지")
    logger.error("에러 메시지")


def main():
    """
    메인 함수 - 실행 예제
    """
    print("=== 예제 실행 시작 ===")
    
    # 기본 클래스 사용
    example = ExampleClass("test", "example")
    print(f"생성된 객체: {example}")
    
    # 메서드 호출
    result = example.public_method({"name": "test", "value": 42})
    print(f"메서드 결과: {result}")
    
    # 속성 접근
    print(f"계산된 속성: {example.computed_property}")
    
    # 고급 클래스 사용
    advanced = AdvancedExample("advanced", "test", "prefix")
    results = advanced.advanced_method(["hello", 5, {"key": "value"}])
    print(f"고급 메서드 결과: {results}")
    
    # 유틸리티 함수 사용
    util_result = utility_function("hello", "world")
    print(f"유틸리티 함수 결과: {util_result}")
    
    # 에러 처리 예제
    print("\n=== 에러 처리 예제 ===")
    error_handling_example()
    
    # 설정 예제
    print("\n=== 설정 예제 ===")
    config = configuration_example()
    print(f"설정: {config}")
    
    # 로깅 예제
    print("\n=== 로깅 예제 ===")
    logging_example()
    
    print("\n=== 예제 실행 완료 ===")


if __name__ == "__main__":
    main()
