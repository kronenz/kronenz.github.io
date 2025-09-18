#!/usr/bin/env python3
"""
Jekyll front matter를 모든 가이드 파일에 추가하는 스크립트
"""
import os
import re
from pathlib import Path

def add_front_matter_to_file(file_path, series_name, order):
    """파일에 Jekyll front matter 추가"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 이미 front matter가 있는지 확인
    if content.startswith('---'):
        print(f"Front matter already exists in {file_path}")
        return
    
    # 파일명에서 제목 추출
    filename = Path(file_path).stem
    title_match = re.search(r'(\d+-\d+):\s*(.+)', filename)
    
    if title_match:
        guide_number = title_match.group(1)
        title = title_match.group(2).replace('-', ' ')
    else:
        # 첫 번째 줄에서 제목 추출
        first_line = content.split('\n')[0]
        title_match = re.search(r'#\s*(\d+-\d+):\s*(.+)', first_line)
        if title_match:
            guide_number = title_match.group(1)
            title = title_match.group(2)
        else:
            guide_number = filename
            title = filename.replace('-', ' ')
    
    # Front matter 생성
    front_matter = f"""---
layout: default
title: "{guide_number}: {title}"
description: "에이전틱 SaaS 조직 가이드"
series: "{series_name}"
order: {order}
---

"""
    
    # Front matter 추가
    new_content = front_matter + content
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Added front matter to {file_path}")

def main():
    """메인 함수"""
    base_dir = Path('.')
    
    # 각 시리즈별로 처리
    series_dirs = ['series-1', 'series-2', 'series-3', 'series-4', 'series-5']
    
    for series_dir in series_dirs:
        series_path = base_dir / series_dir
        if not series_path.exists():
            continue
            
        print(f"Processing {series_dir}...")
        
        # 시리즈 내의 모든 .md 파일 찾기 (index.md 제외)
        md_files = list(series_path.glob('*.md'))
        md_files = [f for f in md_files if f.name != 'index.md']
        
        # 파일명으로 정렬
        md_files.sort(key=lambda x: x.name)
        
        for i, md_file in enumerate(md_files, 1):
            add_front_matter_to_file(md_file, series_dir, i)
    
    print("Front matter addition completed!")

if __name__ == "__main__":
    main()
