#!/usr/bin/env python3
"""
Add links to all guides in chapter index files
"""

import os
import re
import glob

def add_links_to_chapter(chapter_dir):
    """Add links to all guides in a chapter index file"""
    index_file = f"{chapter_dir}/index.md"
    if not os.path.exists(index_file):
        print(f"Index file not found: {index_file}")
        return
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all guide files in the chapter
    guide_files = glob.glob(f"{chapter_dir}/*.md")
    guide_files = [f for f in guide_files if not f.endswith('index.md') and not f.endswith('README.md')]
    
    # Extract guide numbers and names
    guides = []
    for file_path in guide_files:
        filename = os.path.basename(file_path)
        if filename.startswith(('1-', '2-', '3-', '4-', '5-')):
            # Extract number and create link
            guide_num = filename.split('-')[0] + '-' + filename.split('-')[1]
            guide_name = filename.replace('.md', '')
            link = f"/{chapter_dir}/{guide_name}/"
            guides.append((guide_num, guide_name, link))
    
    # Sort guides by number
    guides.sort(key=lambda x: x[0])
    
    # Add links to content
    for guide_num, guide_name, link in guides:
        # Look for the guide section and add link
        pattern = rf'### {guide_num}:([^\\n]+)'
        replacement = rf'### {guide_num}:\1\n\n[가이드 보기 →]({link})'
        content = re.sub(pattern, replacement, content)
    
    # Write back
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Added links to {len(guides)} guides in {chapter_dir}")

def main():
    """Add links to all chapter index files"""
    chapters = [
        'ai-development',
        'automation-factory', 
        'team-management',
        'advanced-architecture',
        'business-growth'
    ]
    
    for chapter in chapters:
        if os.path.exists(chapter):
            add_links_to_chapter(chapter)

if __name__ == "__main__":
    main()
