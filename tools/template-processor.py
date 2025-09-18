#!/usr/bin/env python3
"""
템플릿 처리 도구
다양한 템플릿을 사용하여 문서를 생성합니다.
"""

import os
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, Template
import argparse
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TemplateProcessor:
    """템플릿 처리기 클래스"""
    
    def __init__(self, template_dir: str = "templates"):
        self.template_dir = Path(template_dir)
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def load_template(self, template_name: str) -> Template:
        """템플릿 로드"""
        template_path = f"{template_name}-template.md"
        return self.env.get_template(template_path)
    
    def process_guide_template(self, spec_data: Dict[str, Any]) -> str:
        """가이드 템플릿 처리"""
        template = self.load_template("guide")
        return template.render(spec=spec_data)
    
    def process_series_template(self, spec_data: Dict[str, Any]) -> str:
        """시리즈 템플릿 처리"""
        template = self.load_template("series-overview")
        return template.render(spec=spec_data)
    
    def process_code_template(self, spec_data: Dict[str, Any]) -> str:
        """코드 템플릿 처리"""
        template = self.load_template("code-example")
        return template.render(spec=spec_data)
    
    def process_checklist_template(self, spec_data: Dict[str, Any]) -> str:
        """체크리스트 템플릿 처리"""
        template = self.env.get_template("checklist-template-simple.md")
        return template.render(spec=spec_data)
    
    def generate_from_spec(self, spec_path: str, template_type: str, output_path: str) -> str:
        """명세 파일로부터 문서 생성"""
        # 명세 파일 로드
        spec_path = Path(spec_path)
        with open(spec_path, 'r', encoding='utf-8') as f:
            if spec_path.suffix == '.json':
                spec_data = json.load(f)
            elif spec_path.suffix in ['.yml', '.yaml']:
                spec_data = yaml.safe_load(f)
            else:
                raise ValueError(f"지원하지 않는 파일 형식: {spec_path.suffix}")
        
        # 템플릿 타입에 따른 처리
        if template_type == "guide":
            content = self.process_guide_template(spec_data)
        elif template_type == "series":
            content = self.process_series_template(spec_data)
        elif template_type == "code":
            content = self.process_code_template(spec_data)
        elif template_type == "checklist":
            content = self.process_checklist_template(spec_data)
        else:
            raise ValueError(f"지원하지 않는 템플릿 타입: {template_type}")
        
        # 파일 저장
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"문서 생성 완료: {output_path}")
        return str(output_path)


def create_sample_specs():
    """샘플 명세 파일들 생성"""
    # 가이드 샘플
    guide_spec = {
        "title": "에이전틱 AI 시작하기",
        "subtitle": "AI 어시스턴트에서 자율적 행위자로의 전환",
        "overview": "이 가이드는 AI 어시스턴트의 한계를 넘어서 진정한 자율적 행위자로 전환하는 방법을 다룹니다.",
        "objectives": [
            "AI 어시스턴트와 AI 에이전트의 차이점 이해",
            "자율성의 정의와 구현 방법 파악",
            "에이전트 기반 아키텍처의 핵심 개념 습득",
            "첫 번째 자율 에이전트 구축 실습"
        ],
        "prerequisites": [
            "Python 기본 문법 이해",
            "객체지향 프로그래밍 개념 숙지",
            "API 사용 경험"
        ],
        "estimated_time": "2시간",
        "difficulty": "중급",
        "sections": {
            "core_concepts": [
                {
                    "title": "AI 어시스턴트 vs AI 에이전트",
                    "content": "현재 대부분의 AI 도구들은 반응형 어시스턴트입니다."
                },
                {
                    "title": "자율성의 핵심 구성 요소",
                    "content": "에이전트는 명확한 목표를 가지고 행동합니다."
                }
            ],
            "practical_steps": [
                {
                    "title": "프로젝트 설정",
                    "content": "가상환경 설정 및 필요한 패키지 설치"
                },
                {
                    "title": "기본 에이전트 구현",
                    "content": "간단한 자율 에이전트 클래스 구현"
                }
            ]
        },
        "code_examples": [
            {
                "title": "기본 에이전트 클래스",
                "language": "python",
                "code": "class SimpleAutonomousAgent:\n    def __init__(self, name, role):\n        self.name = name\n        self.role = role"
            }
        ],
        "resources": [
            {
                "title": "OpenAI API Documentation",
                "url": "https://platform.openai.com/docs"
            },
            {
                "title": "CrewAI Framework",
                "url": "https://docs.crewai.com/"
            }
        ],
        "next_steps": [
            {
                "title": "명세 기반 개발(SDD) 마스터하기",
                "path": "1-2-spec-driven-development.md"
            },
            {
                "title": "원칙 기반 엔지니어링으로의 전환",
                "path": "1-3-principle-based-engineering.md"
            }
        ]
    }
    
    # 시리즈 샘플
    series_spec = {
        "title": "에이전틱 조직의 기초",
        "overview": "이 시리즈는 성공적인 AI 에이전트 조직의 기술적, 철학적 토대를 마련하는 데 중점을 둡니다.",
        "objectives": [
            "AI 에이전트 조직의 기본 개념 이해",
            "명세 기반 개발 프로세스 마스터",
            "자율적 AI 에이전트 구축 능력",
            "이중 LLM 아키텍처 설계 및 구현",
            "에이전트 팀 오케스트레이션"
        ],
        "tools": [
            "Python 3.8+",
            "CrewAI",
            "OpenAI API",
            "Anthropic Claude API",
            "Git",
            "Docker (선택사항)"
        ],
        "architecture": "이 시리즈는 명세 기반 개발(SDD) 원칙을 중심으로 한 체계적인 접근 방식을 제시합니다.",
        "sections": {
            "guides": [
                {
                    "guide_number": "1-1",
                    "title": "에이전틱 AI 시작하기",
                    "subtitle": "AI 어시스턴트에서 자율적 행위자로의 전환",
                    "description": "AI 어시스턴트와 AI 에이전트의 차이점을 이해하고 첫 번째 자율 에이전트를 구축합니다.",
                    "key_topics": ["자율성", "에이전트 아키텍처", "기본 구현"],
                    "estimated_time": "2시간",
                    "difficulty": "중급"
                }
            ]
        },
        "next_series": {
            "title": "자동화된 SaaS 팩토리",
            "path": "../series-2/README.md",
            "description": "완전 자동화된 개발 파이프라인 구축"
        }
    }
    
    # 체크리스트 샘플
    checklist_spec = {
        "title": "에이전틱 AI 시작하기",
        "description": "AI 에이전트 구축을 위한 단계별 체크리스트",
        "prerequisites": {
            "environment": [
                "Python 3.8+ 설치 확인",
                "가상환경 설정",
                "프로젝트 디렉토리 생성"
            ],
            "tools": [
                "VS Code 또는 선호하는 에디터 설치",
                "Git 설치 및 설정",
                "터미널/명령 프롬프트 준비"
            ],
            "accounts": [
                "OpenAI API 키 발급",
                "GitHub 계정 생성",
                "필요한 라이브러리 설치"
            ]
        },
        "objectives": [
            "AI 어시스턴트와 AI 에이전트의 차이점 이해",
            "자율성의 정의와 구현 방법 파악",
            "에이전트 기반 아키텍처의 핵심 개념 습득",
            "첫 번째 자율 에이전트 구축 실습"
        ],
        "practical_steps": [
            {
                "title": "프로젝트 설정",
                "items": [
                    "가상환경 생성 및 활성화",
                    "필요한 패키지 설치",
                    "프로젝트 구조 생성"
                ]
            },
            {
                "title": "기본 에이전트 구현",
                "items": [
                    "에이전트 클래스 정의",
                    "기본 메서드 구현",
                    "테스트 코드 작성"
                ]
            }
        ],
        "completion": {
            "basic": [
                "에이전트 클래스가 정상적으로 작동함",
                "기본 메서드들이 구현됨",
                "테스트가 통과함"
            ],
            "advanced": [
                "에러 처리가 구현됨",
                "로깅이 설정됨",
                "설정 파일이 분리됨"
            ],
            "testing": [
                "단위 테스트 작성",
                "통합 테스트 작성",
                "테스트 커버리지 확인"
            ]
        },
        "quality": {
            "code": [
                "코드가 PEP 8 스타일을 따름",
                "문서화가 충분함",
                "에러 처리가 적절함"
            ],
            "documentation": [
                "README.md가 작성됨",
                "API 문서가 작성됨",
                "사용 예제가 포함됨"
            ],
            "security": [
                "API 키가 안전하게 관리됨",
                "민감한 정보가 하드코딩되지 않음",
                "입력 검증이 구현됨"
            ]
        },
        "deployment": {
            "pre_deployment": [
                "모든 테스트가 통과함",
                "코드 리뷰가 완료됨",
                "문서가 업데이트됨"
            ],
            "deployment": [
                "Git에 커밋 및 푸시",
                "CI/CD 파이프라인 실행",
                "배포 환경 확인"
            ],
            "post_deployment": [
                "배포된 애플리케이션 테스트",
                "모니터링 설정",
                "성능 확인"
            ]
        },
        "metrics": {
            "quantitative": [
                {"name": "코드 커버리지", "target": "80% 이상"},
                {"name": "응답 시간", "target": "1초 이하"},
                {"name": "에러율", "target": "1% 이하"}
            ],
            "qualitative": [
                {"name": "코드 가독성", "description": "다른 개발자가 이해하기 쉬운 코드"},
                {"name": "유지보수성", "description": "수정과 확장이 용이한 구조"},
                {"name": "확장성", "description": "새로운 기능 추가가 쉬운 아키텍처"}
            ]
        },
        "next_steps": [
            {
                "title": "명세 기반 개발(SDD) 마스터하기",
                "path": "1-2-spec-driven-development.md"
            },
            {
                "title": "원칙 기반 엔지니어링으로의 전환",
                "path": "1-3-principle-based-engineering.md"
            }
        ]
    }
    
    # 샘플 파일들 저장
    samples = {
        "sample_guide_spec.json": guide_spec,
        "sample_series_spec.json": series_spec,
        "sample_checklist_spec.json": checklist_spec
    }
    
    for filename, spec_data in samples.items():
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(spec_data, f, ensure_ascii=False, indent=2)
        logger.info(f"샘플 명세 파일 생성: {filename}")


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(description="템플릿 처리 도구")
    parser.add_argument("--spec", help="명세 파일 경로")
    parser.add_argument("--template", choices=["guide", "series", "code", "checklist"], help="템플릿 타입")
    parser.add_argument("--output", help="출력 파일 경로")
    parser.add_argument("--template-dir", default="templates", help="템플릿 디렉토리")
    parser.add_argument("--create-samples", action="store_true", help="샘플 명세 파일들 생성")
    
    args = parser.parse_args()
    
    if args.create_samples:
        create_sample_specs()
        return 0
    
    if not args.spec or not args.template or not args.output:
        parser.print_help()
        return 1
    
    try:
        # 템플릿 처리기 초기화
        processor = TemplateProcessor(args.template_dir)
        
        # 문서 생성
        output_path = processor.generate_from_spec(args.spec, args.template, args.output)
        print(f"문서 생성 완료: {output_path}")
        
    except Exception as e:
        logger.error(f"템플릿 처리 실패: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
