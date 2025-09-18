#!/usr/bin/env python3
"""
연속성 검사 도구
가이드 시리즈의 일관성과 연속성을 검사합니다.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Set, Tuple
from dataclasses import dataclass
from datetime import datetime
import argparse
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class LinkIssue:
    """링크 이슈 정보"""
    file_path: str
    line_number: int
    link_text: str
    link_url: str
    issue_type: str
    message: str


@dataclass
class ConsistencyIssue:
    """일관성 이슈 정보"""
    file_path: str
    line_number: int
    issue_type: str
    message: str
    suggested_fix: str


@dataclass
class DependencyIssue:
    """의존성 이슈 정보"""
    file_path: str
    missing_dependency: str
    issue_type: str
    message: str


class LinkChecker:
    """링크 검사 클래스"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
        self.anchor_pattern = re.compile(r'^#')
        self.external_pattern = re.compile(r'^https?://')
        self.file_pattern = re.compile(r'^[^#]+\.md$')
    
    def check_all_links(self, series_path: str) -> List[LinkIssue]:
        """모든 링크 검사"""
        issues = []
        series_path = Path(series_path)
        
        for md_file in series_path.rglob("*.md"):
            file_issues = self.check_file_links(md_file)
            issues.extend(file_issues)
        
        return issues
    
    def check_file_links(self, file_path: Path) -> List[LinkIssue]:
        """파일 내 링크 검사"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                matches = self.link_pattern.findall(line)
                for link_text, link_url in matches:
                    issue = self.check_single_link(file_path, line_num, link_text, link_url)
                    if issue:
                        issues.append(issue)
        
        except Exception as e:
            logger.error(f"파일 읽기 실패: {file_path}, {e}")
        
        return issues
    
    def check_single_link(self, file_path: Path, line_num: int, link_text: str, link_url: str) -> Optional[LinkIssue]:
        """단일 링크 검사"""
        # 앵커 링크 (페이지 내 링크)
        if self.anchor_pattern.match(link_url):
            return self.check_anchor_link(file_path, line_num, link_text, link_url)
        
        # 외부 링크
        elif self.external_pattern.match(link_url):
            return self.check_external_link(file_path, line_num, link_text, link_url)
        
        # 내부 파일 링크
        elif self.file_pattern.match(link_url):
            return self.check_internal_link(file_path, line_num, link_text, link_url)
        
        return None
    
    def check_anchor_link(self, file_path: Path, line_num: int, link_text: str, link_url: str) -> Optional[LinkIssue]:
        """앵커 링크 검사"""
        anchor = link_url[1:]  # # 제거
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 헤딩에서 앵커 찾기
            heading_pattern = re.compile(r'^#+\s+(.+)$', re.MULTILINE)
            headings = heading_pattern.findall(content)
            
            # 앵커가 헤딩에 존재하는지 확인
            if not any(self.normalize_heading(heading) == anchor for heading in headings):
                return LinkIssue(
                    file_path=str(file_path),
                    line_number=line_num,
                    link_text=link_text,
                    link_url=link_url,
                    issue_type="broken_anchor",
                    message=f"앵커 '{anchor}'를 찾을 수 없습니다."
                )
        
        except Exception as e:
            logger.error(f"앵커 검사 실패: {file_path}, {e}")
        
        return None
    
    def check_external_link(self, file_path: Path, line_num: int, link_text: str, link_url: str) -> Optional[LinkIssue]:
        """외부 링크 검사 (기본적인 형식 검사만)"""
        # URL 형식 검사
        if not self.is_valid_url(link_url):
            return LinkIssue(
                file_path=str(file_path),
                line_number=line_num,
                link_text=link_text,
                link_url=link_url,
                issue_type="invalid_url",
                message=f"잘못된 URL 형식: {link_url}"
            )
        
        return None
    
    def check_internal_link(self, file_path: Path, line_num: int, link_text: str, link_url: str) -> Optional[LinkIssue]:
        """내부 파일 링크 검사"""
        # 상대 경로 해결
        target_path = file_path.parent / link_url
        
        if not target_path.exists():
            return LinkIssue(
                file_path=str(file_path),
                line_number=line_num,
                link_text=link_text,
                link_url=link_url,
                issue_type="broken_internal_link",
                message=f"파일을 찾을 수 없습니다: {link_url}"
            )
        
        return None
    
    def normalize_heading(self, heading: str) -> str:
        """헤딩을 앵커 형식으로 정규화"""
        # 소문자 변환, 공백을 하이픈으로 변경, 특수문자 제거
        normalized = re.sub(r'[^\w\s-]', '', heading.lower())
        normalized = re.sub(r'[-\s]+', '-', normalized)
        return normalized.strip('-')
    
    def is_valid_url(self, url: str) -> bool:
        """URL 유효성 검사"""
        url_pattern = re.compile(
            r'^https?://'  # http:// 또는 https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # 도메인
            r'localhost|'  # localhost
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP
            r'(?::\d+)?'  # 포트
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url_pattern.match(url) is not None


class ConsistencyChecker:
    """일관성 검사 클래스"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.terminology = self.load_terminology()
        self.style_rules = self.load_style_rules()
    
    def load_terminology(self) -> Dict[str, List[str]]:
        """용어 사전 로드"""
        return {
            "AI 에이전트": ["AI agent", "autonomous agent", "intelligent agent"],
            "명세 기반 개발": ["Spec-Driven Development", "SDD", "spec-driven development"],
            "에이전틱": ["agentic", "에이전틱 AI", "agentic AI"],
            "자율성": ["autonomy", "autonomous", "자율적"],
            "오케스트레이션": ["orchestration", "조율", "관리"]
        }
    
    def load_style_rules(self) -> Dict[str, Any]:
        """스타일 규칙 로드"""
        return {
            "heading_levels": {
                "max_depth": 6,
                "required_sequence": True
            },
            "code_blocks": {
                "require_language": True,
                "max_length": 1000
            },
            "links": {
                "require_alt_text": True,
                "max_length": 100
            },
            "sections": {
                "required_sections": ["개요", "학습 목표", "다음 단계"],
                "recommended_sections": ["실습", "고급 기능", "문제 해결"]
            }
        }
    
    def check_series(self, series_path: str) -> List[ConsistencyIssue]:
        """시리즈 일관성 검사"""
        issues = []
        series_path = Path(series_path)
        
        for md_file in series_path.rglob("*.md"):
            file_issues = self.check_file_consistency(md_file)
            issues.extend(file_issues)
        
        # 시리즈 전체 일관성 검사
        series_issues = self.check_series_consistency(series_path)
        issues.extend(series_issues)
        
        return issues
    
    def check_file_consistency(self, file_path: Path) -> List[ConsistencyIssue]:
        """파일 일관성 검사"""
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            # 용어 일관성 검사
            terminology_issues = self.check_terminology_consistency(file_path, content)
            issues.extend(terminology_issues)
            
            # 스타일 일관성 검사
            style_issues = self.check_style_consistency(file_path, lines)
            issues.extend(style_issues)
            
            # 구조 일관성 검사
            structure_issues = self.check_structure_consistency(file_path, content)
            issues.extend(structure_issues)
        
        except Exception as e:
            logger.error(f"파일 일관성 검사 실패: {file_path}, {e}")
        
        return issues
    
    def check_terminology_consistency(self, file_path: Path, content: str) -> List[ConsistencyIssue]:
        """용어 일관성 검사"""
        issues = []
        
        for standard_term, variations in self.terminology.items():
            # 표준 용어가 사용되었는지 확인
            if standard_term not in content:
                # 대안 용어가 사용되었는지 확인
                used_variations = [var for var in variations if var in content]
                if used_variations:
                    issues.append(ConsistencyIssue(
                        file_path=str(file_path),
                        line_number=0,
                        issue_type="terminology_inconsistency",
                        message=f"용어 일관성 문제: '{used_variations[0]}' 대신 '{standard_term}' 사용 권장",
                        suggested_fix=f"'{used_variations[0]}'를 '{standard_term}'로 변경"
                    ))
        
        return issues
    
    def check_style_consistency(self, file_path: Path, lines: List[str]) -> List[ConsistencyIssue]:
        """스타일 일관성 검사"""
        issues = []
        
        for line_num, line in enumerate(lines, 1):
            # 헤딩 레벨 검사
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if heading_match:
                level = len(heading_match.group(1))
                if level > self.style_rules["heading_levels"]["max_depth"]:
                    issues.append(ConsistencyIssue(
                        file_path=str(file_path),
                        line_number=line_num,
                        issue_type="heading_level_too_deep",
                        message=f"헤딩 레벨이 너무 깊습니다: {level}",
                        suggested_fix=f"헤딩 레벨을 {self.style_rules['heading_levels']['max_depth']} 이하로 조정"
                    ))
            
            # 코드 블록 검사
            if line.strip().startswith('```'):
                if not re.match(r'^```\w+', line):
                    issues.append(ConsistencyIssue(
                        file_path=str(file_path),
                        line_number=line_num,
                        issue_type="code_block_missing_language",
                        message="코드 블록에 언어가 지정되지 않았습니다.",
                        suggested_fix="코드 블록에 언어를 지정하세요 (예: ```python)"
                    ))
        
        return issues
    
    def check_structure_consistency(self, file_path: Path, content: str) -> List[ConsistencyIssue]:
        """구조 일관성 검사"""
        issues = []
        
        # 필수 섹션 검사
        required_sections = self.style_rules["sections"]["required_sections"]
        for section in required_sections:
            if f"## {section}" not in content:
                issues.append(ConsistencyIssue(
                    file_path=str(file_path),
                    line_number=0,
                    issue_type="missing_required_section",
                    message=f"필수 섹션이 누락되었습니다: {section}",
                    suggested_fix=f"## {section} 섹션을 추가하세요"
                ))
        
        return issues
    
    def check_series_consistency(self, series_path: Path) -> List[ConsistencyIssue]:
        """시리즈 전체 일관성 검사"""
        issues = []
        
        # 시리즈 번호 일관성 검사
        series_files = list(series_path.rglob("*.md"))
        series_numbers = set()
        
        for file_path in series_files:
            # 파일명에서 시리즈 번호 추출
            match = re.search(r'(\d+)-(\d+)', file_path.name)
            if match:
                series_num = int(match.group(1))
                series_numbers.add(series_num)
        
        if len(series_numbers) > 1:
            issues.append(ConsistencyIssue(
                file_path=str(series_path),
                line_number=0,
                issue_type="series_number_inconsistency",
                message=f"시리즈 번호가 일관되지 않습니다: {sorted(series_numbers)}",
                suggested_fix="모든 파일의 시리즈 번호를 통일하세요"
            ))
        
        return issues


class DependencyChecker:
    """의존성 검사 클래스"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.dependency_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)\)')
    
    def check_dependencies(self, series_path: str) -> List[DependencyIssue]:
        """의존성 검사"""
        issues = []
        series_path = Path(series_path)
        
        # 모든 파일의 의존성 맵 생성
        dependency_map = self.build_dependency_map(series_path)
        
        # 순환 의존성 검사
        circular_issues = self.check_circular_dependencies(dependency_map)
        issues.extend(circular_issues)
        
        # 누락된 의존성 검사
        missing_issues = self.check_missing_dependencies(series_path, dependency_map)
        issues.extend(missing_issues)
        
        return issues
    
    def build_dependency_map(self, series_path: Path) -> Dict[str, Set[str]]:
        """의존성 맵 구축"""
        dependency_map = {}
        
        for md_file in series_path.rglob("*.md"):
            dependencies = set()
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 내부 링크에서 의존성 추출
                matches = self.dependency_pattern.findall(content)
                for link_text, link_url in matches:
                    if link_url.endswith('.md'):
                        # 상대 경로를 절대 경로로 변환
                        target_path = md_file.parent / link_url
                        if target_path.exists():
                            dependencies.add(str(target_path.relative_to(series_path)))
                
                dependency_map[str(md_file.relative_to(series_path))] = dependencies
            
            except Exception as e:
                logger.error(f"의존성 맵 구축 실패: {md_file}, {e}")
        
        return dependency_map
    
    def check_circular_dependencies(self, dependency_map: Dict[str, Set[str]]) -> List[DependencyIssue]:
        """순환 의존성 검사"""
        issues = []
        
        def has_circular_dependency(file_path: str, visited: Set[str], rec_stack: Set[str]) -> bool:
            visited.add(file_path)
            rec_stack.add(file_path)
            
            for dependency in dependency_map.get(file_path, set()):
                if dependency not in visited:
                    if has_circular_dependency(dependency, visited, rec_stack):
                        return True
                elif dependency in rec_stack:
                    return True
            
            rec_stack.remove(file_path)
            return False
        
        for file_path in dependency_map:
            if has_circular_dependency(file_path, set(), set()):
                issues.append(DependencyIssue(
                    file_path=file_path,
                    missing_dependency="",
                    issue_type="circular_dependency",
                    message=f"순환 의존성이 발견되었습니다: {file_path}"
                ))
        
        return issues
    
    def check_missing_dependencies(self, series_path: Path, dependency_map: Dict[str, Set[str]]) -> List[DependencyIssue]:
        """누락된 의존성 검사"""
        issues = []
        
        for file_path, dependencies in dependency_map.items():
            for dependency in dependencies:
                dependency_path = series_path / dependency
                if not dependency_path.exists():
                    issues.append(DependencyIssue(
                        file_path=file_path,
                        missing_dependency=dependency,
                        issue_type="missing_dependency",
                        message=f"의존성 파일이 존재하지 않습니다: {dependency}"
                    ))
        
        return issues


class ContinuityChecker:
    """연속성 검사 메인 클래스"""
    
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.link_checker = LinkChecker(base_path)
        self.consistency_checker = ConsistencyChecker(base_path)
        self.dependency_checker = DependencyChecker(base_path)
    
    def check_continuity(self, series_path: str) -> Dict[str, Any]:
        """연속성 검사 실행"""
        logger.info(f"연속성 검사 시작: {series_path}")
        
        # 링크 검사
        link_issues = self.link_checker.check_all_links(series_path)
        logger.info(f"링크 검사 완료: {len(link_issues)}개 이슈 발견")
        
        # 일관성 검사
        consistency_issues = self.consistency_checker.check_series(series_path)
        logger.info(f"일관성 검사 완료: {len(consistency_issues)}개 이슈 발견")
        
        # 의존성 검사
        dependency_issues = self.dependency_checker.check_dependencies(series_path)
        logger.info(f"의존성 검사 완료: {len(dependency_issues)}개 이슈 발견")
        
        # 결과 정리
        result = {
            "timestamp": datetime.now().isoformat(),
            "series_path": series_path,
            "total_issues": len(link_issues) + len(consistency_issues) + len(dependency_issues),
            "link_issues": {
                "count": len(link_issues),
                "issues": [issue.__dict__ for issue in link_issues]
            },
            "consistency_issues": {
                "count": len(consistency_issues),
                "issues": [issue.__dict__ for issue in consistency_issues]
            },
            "dependency_issues": {
                "count": len(dependency_issues),
                "issues": [issue.__dict__ for issue in dependency_issues]
            }
        }
        
        return result
    
    def generate_report(self, result: Dict[str, Any], output_path: str):
        """검사 결과 보고서 생성"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        logger.info(f"연속성 검사 보고서 생성: {output_path}")


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(description="연속성 검사 도구")
    parser.add_argument("--series-path", required=True, help="시리즈 경로")
    parser.add_argument("--base-path", default=".", help="기준 경로")
    parser.add_argument("--output", help="보고서 출력 경로")
    
    args = parser.parse_args()
    
    try:
        # 연속성 검사기 초기화
        checker = ContinuityChecker(args.base_path)
        
        # 연속성 검사 실행
        result = checker.check_continuity(args.series_path)
        
        # 결과 출력
        print(f"연속성 검사 완료:")
        print(f"  총 이슈 수: {result['total_issues']}")
        print(f"  링크 이슈: {result['link_issues']['count']}")
        print(f"  일관성 이슈: {result['consistency_issues']['count']}")
        print(f"  의존성 이슈: {result['dependency_issues']['count']}")
        
        # 보고서 생성
        if args.output:
            checker.generate_report(result, args.output)
        
        # 심각한 이슈가 있으면 종료 코드 1 반환
        if result['total_issues'] > 0:
            return 1
    
    except Exception as e:
        logger.error(f"연속성 검사 실패: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
