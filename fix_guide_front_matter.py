#!/usr/bin/env python3
"""
Fix front matter for guide files in the new chapter structure
"""

import os
import re
import glob

def fix_front_matter(file_path):
    """Fix front matter for a single guide file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract front matter
    front_matter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not front_matter_match:
        print(f"No front matter found in {file_path}")
        return
    
    front_matter = front_matter_match.group(1)
    rest_content = content[front_matter_match.end():]
    
    # Parse front matter
    lines = front_matter.split('\n')
    new_lines = []
    
    for line in lines:
        if line.strip().startswith('series:'):
            # Remove series field
            continue
        elif line.strip().startswith('layout:'):
            # Keep layout
            new_lines.append(line)
        elif line.strip().startswith('title:'):
            # Keep title
            new_lines.append(line)
        elif line.strip().startswith('description:'):
            # Keep description
            new_lines.append(line)
        elif line.strip().startswith('order:'):
            # Keep order
            new_lines.append(line)
        elif line.strip() and not line.strip().startswith('#'):
            # Keep other fields
            new_lines.append(line)
    
    # Add permalink based on file path
    relative_path = file_path.replace('.md', '')
    permalink = f"/{relative_path}/"
    new_lines.append(f"permalink: {permalink}")
    
    # Reconstruct content
    new_front_matter = '---\n' + '\n'.join(new_lines) + '\n---\n'
    new_content = new_front_matter + rest_content
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Fixed: {file_path}")

def main():
    """Fix all guide files"""
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
                    fix_front_matter(file_path)

if __name__ == "__main__":
    main()
