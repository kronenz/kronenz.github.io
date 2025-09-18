#!/usr/bin/env python3
"""
가이드 생성 도구
Spec Driven Development 원칙을 적용하여 가이드를 자동 생성합니다.
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


class GuideSpec:
    """가이드 명세 클래스"""
    
    def __init__(self, spec_data: Dict[str, Any]):
        self.series_number = spec_data.get("series_number", 1)
        self.guide_number = spec_data.get("guide_number", "1-1")
        self.title = spec_data.get("title", "")
        self.subtitle = spec_data.get("subtitle", "")
        self.overview = spec_data.get("overview", "")
        self.objectives = spec_data.get("objectives", [])
        self.prerequisites = spec_data.get("prerequisites", [])
        self.estimated_time = spec_data.get("estimated_time", "2시간")
        self.difficulty = spec_data.get("difficulty", "중급")
        self.template_type = spec_data.get("template_type", "guide")
        self.sections = spec_data.get("sections", {})
        self.code_examples = spec_data.get("code_examples", [])
        self.resources = spec_data.get("resources", [])
        self.next_steps = spec_data.get("next_steps", [])
        
    def to_dict(self) -> Dict[str, Any]:
        """딕셔너리로 변환"""
        return {
            "series_number": self.series_number,
            "guide_number": self.guide_number,
            "title": self.title,
            "subtitle": self.subtitle,
            "overview": self.overview,
            "objectives": self.objectives,
            "prerequisites": self.prerequisites,
            "estimated_time": self.estimated_time,
            "difficulty": self.difficulty,
            "template_type": self.template_type,
            "sections": self.sections,
            "code_examples": self.code_examples,
            "resources": self.resources,
            "next_steps": self.next_steps
        }


class TemplateEngine:
    """템플릿 엔진 클래스"""
    
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
    
    def render_guide(self, spec: GuideSpec) -> str:
        """가이드 렌더링"""
        template = self.load_template(spec.template_type)
        return template.render(spec=spec)


class GuideValidator:
    """가이드 검증 클래스"""
    
    def __init__(self):
        self.required_sections = [
            "개요", "학습 목표", "핵심 개념", "실습", "다음 단계"
        ]
        self.required_metadata = [
            "title", "objectives", "overview"
        ]
    
    def validate_spec(self, spec: GuideSpec) -> Dict[str, Any]:
        """명세 검증"""
        validation_result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        # 필수 필드 검증
        for field in self.required_metadata:
            if not getattr(spec, field, None):
                validation_result["errors"].append(f"필수 필드 누락: {field}")
                validation_result["valid"] = False
        
        # 목표 검증
        if len(spec.objectives) < 3:
            validation_result["warnings"].append("학습 목표가 3개 미만입니다.")
        
        # 시간 검증
        if not spec.estimated_time:
            validation_result["warnings"].append("예상 소요 시간이 설정되지 않았습니다.")
        
        return validation_result
    
    def validate_content(self, content: str) -> Dict[str, Any]:
        """내용 검증"""
        validation_result = {
            "valid": True,
            "errors": [],
            "warnings": []
        }
        
        # 기본 구조 검증
        if not content.strip():
            validation_result["errors"].append("내용이 비어있습니다.")
            validation_result["valid"] = False
            return validation_result
        
        # 섹션 검증
        for section in self.required_sections:
            if f"## {section}" not in content:
                validation_result["warnings"].append(f"권장 섹션 누락: {section}")
        
        # 링크 검증
        if "http" in content and "]" not in content:
            validation_result["warnings"].append("잘못된 링크 형식이 있을 수 있습니다.")
        
        return validation_result


class GuideGenerator:
    """가이드 생성기 메인 클래스"""
    
    def __init__(self, template_dir: str = "templates"):
        self.template_engine = TemplateEngine(template_dir)
        self.validator = GuideValidator()
        self.output_dir = Path("generated_guides")
        self.output_dir.mkdir(exist_ok=True)
    
    def load_spec(self, spec_path: str) -> GuideSpec:
        """명세 파일 로드"""
        spec_path = Path(spec_path)
        
        if not spec_path.exists():
            raise FileNotFoundError(f"명세 파일을 찾을 수 없습니다: {spec_path}")
        
        with open(spec_path, 'r', encoding='utf-8') as f:
            if spec_path.suffix == '.json':
                spec_data = json.load(f)
            elif spec_path.suffix in ['.yml', '.yaml']:
                spec_data = yaml.safe_load(f)
            else:
                raise ValueError(f"지원하지 않는 파일 형식: {spec_path.suffix}")
        
        return GuideSpec(spec_data)
    
    def generate_guide(self, spec_path: str, output_path: Optional[str] = None) -> str:
        """가이드 생성"""
        logger.info(f"가이드 생성 시작: {spec_path}")
        
        # 명세 로드
        spec = self.load_spec(spec_path)
        
        # 명세 검증
        spec_validation = self.validator.validate_spec(spec)
        if not spec_validation["valid"]:
            logger.error(f"명세 검증 실패: {spec_validation['errors']}")
            raise ValueError(f"명세 검증 실패: {spec_validation['errors']}")
        
        if spec_validation["warnings"]:
            logger.warning(f"명세 경고: {spec_validation['warnings']}")
        
        # 가이드 생성
        content = self.template_engine.render_guide(spec)
        
        # 내용 검증
        content_validation = self.validator.validate_content(content)
        if not content_validation["valid"]:
            logger.error(f"내용 검증 실패: {content_validation['errors']}")
            raise ValueError(f"내용 검증 실패: {content_validation['errors']}")
        
        if content_validation["warnings"]:
            logger.warning(f"내용 경고: {content_validation['warnings']}")
        
        # 출력 경로 설정
        if output_path is None:
            output_path = self.output_dir / f"{spec.guide_number}-{spec.title.lower().replace(' ', '-')}.md"
        else:
            output_path = Path(output_path)
        
        # 파일 저장
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"가이드 생성 완료: {output_path}")
        return str(output_path)
    
    def generate_series(self, series_spec_path: str) -> List[str]:
        """시리즈 전체 생성"""
        logger.info(f"시리즈 생성 시작: {series_spec_path}")
        
        series_spec = self.load_spec(series_spec_path)
        generated_guides = []
        
        if "guides" in series_spec.sections:
            for guide_spec in series_spec.sections["guides"]:
                # 개별 가이드 명세 생성
                guide_spec_data = {
                    "series_number": series_spec.series_number,
                    **guide_spec
                }
                
                # 임시 명세 파일 생성
                temp_spec_path = self.output_dir / f"temp_{guide_spec['guide_number']}.json"
                with open(temp_spec_path, 'w', encoding='utf-8') as f:
                    json.dump(guide_spec_data, f, ensure_ascii=False, indent=2)
                
                try:
                    # 가이드 생성
                    output_path = self.generate_guide(str(temp_spec_path))
                    generated_guides.append(output_path)
                finally:
                    # 임시 파일 삭제
                    temp_spec_path.unlink()
        
        logger.info(f"시리즈 생성 완료: {len(generated_guides)}개 가이드 생성")
        return generated_guides


def create_sample_spec() -> Dict[str, Any]:
    """샘플 명세 생성"""
    return {
        "series_number": 1,
        "guide_number": "1-1",
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
        "template_type": "guide",
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


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(description="가이드 생성 도구")
    parser.add_argument("--spec", help="명세 파일 경로")
    parser.add_argument("--output", help="출력 파일 경로")
    parser.add_argument("--template-dir", default="templates", help="템플릿 디렉토리")
    parser.add_argument("--create-sample", action="store_true", help="샘플 명세 파일 생성")
    
    args = parser.parse_args()
    
    if args.create_sample:
        # 샘플 명세 파일 생성
        sample_spec = create_sample_spec()
        sample_path = "sample_guide_spec.json"
        with open(sample_path, 'w', encoding='utf-8') as f:
            json.dump(sample_spec, f, ensure_ascii=False, indent=2)
        print(f"샘플 명세 파일 생성: {sample_path}")
        return
    
    try:
        # 가이드 생성기 초기화
        generator = GuideGenerator(args.template_dir)
        
        # 가이드 생성
        output_path = generator.generate_guide(args.spec, args.output)
        print(f"가이드 생성 완료: {output_path}")
        
    except Exception as e:
        logger.error(f"가이드 생성 실패: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
