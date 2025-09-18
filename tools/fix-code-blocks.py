#!/usr/bin/env python3
"""
코드 블록에 언어를 자동으로 지정하는 도구
"""

import os
import re
import glob
from pathlib import Path

def detect_language_from_content(code_content):
    """코드 내용을 분석하여 언어를 감지합니다."""
    code_content = code_content.strip()
    
    # Python 감지
    if any(keyword in code_content for keyword in [
        'import ', 'from ', 'def ', 'class ', 'if __name__', 
        'print(', 'return ', 'self.', 'super()', 'lambda ',
        'try:', 'except:', 'finally:', 'with ', 'as ',
        'yield ', 'async ', 'await ', 'raise '
    ]):
        return 'python'
    
    # JavaScript/TypeScript 감지
    if any(keyword in code_content for keyword in [
        'function ', 'const ', 'let ', 'var ', '=>', 
        'console.log', 'require(', 'import ', 'export ',
        'interface ', 'type ', 'class ', 'extends ',
        'async ', 'await ', 'Promise', 'fetch('
    ]):
        return 'javascript'
    
    # YAML 감지
    if any(keyword in code_content for keyword in [
        'name:', 'on:', 'jobs:', 'steps:', 'uses:', 'with:',
        'runs-on:', 'if:', 'env:', 'run:', 'id:'
    ]) and ':' in code_content:
        return 'yaml'
    
    # JSON 감지
    if code_content.startswith('{') and code_content.endswith('}'):
        return 'json'
    
    # Shell/Bash 감지
    if any(keyword in code_content for keyword in [
        '#!/bin/', '#!/usr/bin/', 'cd ', 'ls ', 'mkdir ', 
        'rm ', 'cp ', 'mv ', 'grep ', 'find ', 'chmod ',
        'export ', 'echo ', 'cat ', 'head ', 'tail '
    ]):
        return 'bash'
    
    # SQL 감지
    if any(keyword in code_content.upper() for keyword in [
        'SELECT ', 'FROM ', 'WHERE ', 'INSERT ', 'UPDATE ', 
        'DELETE ', 'CREATE ', 'ALTER ', 'DROP ', 'JOIN ',
        'GROUP BY', 'ORDER BY', 'HAVING '
    ]):
        return 'sql'
    
    # Markdown 감지
    if any(keyword in code_content for keyword in [
        '# ', '## ', '### ', '**', '*', '`', '[', '](',
        '- ', '1. ', '| ', '---'
    ]):
        return 'markdown'
    
    # 기본값은 text
    return 'text'

def fix_code_blocks_in_file(file_path):
    """파일의 코드 블록을 수정합니다."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 빈 코드 블록 찾기 (```로 시작하고 바로 다음 줄이 ```인 경우)
        pattern = r'```\n(.*?)\n```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        if not matches:
            return 0
        
        fixed_count = 0
        for match in matches:
            # 이미 언어가 지정된 경우 건너뛰기
            if match.strip() and not match.strip().startswith('```'):
                # 코드 내용에서 언어 감지
                language = detect_language_from_content(match)
                
                # 언어가 감지된 경우에만 수정
                if language != 'text':
                    old_block = f'```\n{match}\n```'
                    new_block = f'```{language}\n{match}\n```'
                    content = content.replace(old_block, new_block)
                    fixed_count += 1
        
        # 수정된 내용이 있으면 파일에 저장
        if fixed_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ {file_path}: {fixed_count}개 코드 블록 수정")
        
        return fixed_count
        
    except Exception as e:
        print(f"❌ {file_path}: 오류 발생 - {e}")
        return 0

def main():
    """메인 함수"""
    print("🔧 코드 블록 언어 지정 수정 시작...")
    
    # 시리즈 1 디렉토리의 모든 .md 파일 처리
    series_path = Path("series-1")
    if not series_path.exists():
        print("❌ series-1 디렉토리를 찾을 수 없습니다.")
        return
    
    md_files = list(series_path.glob("*.md"))
    total_fixed = 0
    
    for file_path in md_files:
        fixed_count = fix_code_blocks_in_file(file_path)
        total_fixed += fixed_count
    
    print(f"\n🎉 완료: 총 {total_fixed}개 코드 블록 수정")

if __name__ == "__main__":
    main()
