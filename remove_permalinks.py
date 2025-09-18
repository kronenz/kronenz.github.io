#!/usr/bin/env python3
"""
Remove permalink from guide files to let Jekyll handle URLs automatically
"""

import os
import re
import glob

def remove_permalink(file_path):
    """Remove permalink from a single guide file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    front_matter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not front_matter_match:
        print(f"No front matter found in {file_path}")
        return
    
    front_matter = front_matter_match.group(1)
    rest_content = content[front_matter_match.end():]
    
    # Parse front matter and remove permalink
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        if line.strip().startswith('permalink:'):
            # Remove permalink line
            continue
        else:
            new_lines.append(line)
    
    # Reconstruct content
    new_front_matter = '---\n' + '\n'.join(new_lines) + '\n---\n'
    new_content = new_front_matter + rest_content
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Removed permalink from: {file_path}")

def main():
    """Process all guide files"""
    chapters = [
        'ai-development',
        'automation-factory', 
        'team-management',
        'advanced-architecture',
        'business-growth',
        'resources'
    ]
    
    for chapter in chapters:
        if os.path.exists(chapter):
            pattern = f"{chapter}/*.md"
            files = glob.glob(pattern)
            
            for file_path in files:
                if not file_path.endswith('index.md'):
                    remove_permalink(file_path)

if __name__ == "__main__":
    main()
