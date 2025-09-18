#!/usr/bin/env python3
"""
용어 일관성을 위한 자동 수정 도구
"""

import os
import re
import glob
from pathlib import Path

def fix_terminology_in_file(file_path):
    """파일의 용어를 수정합니다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # "관리"를 "오케스트레이션"으로 변경 (단, 특정 컨텍스트 제외)
        # 예외: "관리자", "관리비", "관리자 권한" 등은 제외
        patterns_to_fix = [
            # "관리" 단독 사용 (문장 끝이나 특수문자 앞)
            (r'\b관리\b(?![자비권한])', '오케스트레이션'),
            # "관리하는" -> "오케스트레이션하는"
            (r'관리하는', '오케스트레이션하는'),
            # "관리할" -> "오케스트레이션할"
            (r'관리할', '오케스트레이션할'),
            # "관리하는" -> "오케스트레이션하는"
            (r'관리하는', '오케스트레이션하는'),
        ]
        
        for pattern, replacement in patterns_to_fix:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                changes_made += 1
        
        # "SDD"를 "명세 기반 개발"로 변경
        sdd_patterns = [
            (r'\bSDD\b', '명세 기반 개발'),
        ]
        
        for pattern, replacement in sdd_patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                changes_made += 1
        
        # 수정된 내용이 있으면 파일에 저장
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {file_path}: {changes_made}개 용어 수정")
        
        return changes_made
        
    except Exception as e:
        print(f"❌ {file_path}: 오류 발생 - {e}")
        return 0

def main():
    """메인 함수"""
    print("🔧 용어 일관성 수정 시작...")
    
    # 시리즈 1 디렉토리의 모든 .md 파일 처리
    series_path = Path("series-1")
    if not series_path.exists():
        print("❌ series-1 디렉토리를 찾을 수 없습니다.")
        return
    
    md_files = list(series_path.glob("*.md"))
    total_fixed = 0
    
    for file_path in md_files:
        fixed_count = fix_terminology_in_file(file_path)
        total_fixed += fixed_count
    
    print(f"\n🎉 완료: 총 {total_fixed}개 용어 수정")

if __name__ == "__main__":
    main()
