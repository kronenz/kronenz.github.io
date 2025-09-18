#!/usr/bin/env python3
"""
Hexo 블로그 설정 스크립트
기존 가이드 시리즈를 Hexo 기반 GitHub Pages 블로그로 변환
"""

import os
import sys
import subprocess
import yaml
import shutil
from pathlib import Path
from datetime import datetime

class HexoBlogSetup:
    def __init__(self, base_dir="/root/spec"):
        self.base_dir = Path(base_dir)
        self.publishing_dir = self.base_dir / "publishing"
        self.hexo_dir = self.publishing_dir / "hexo-blog"
        self.specs_dir = self.base_dir / "series"
        
    def setup_hexo_blog(self):
        """Hexo 블로그 초기 설정"""
        print("🚀 Hexo 블로그 설정 시작...")
        
        try:
            # 1. Hexo 사이트 초기화
            self.init_hexo_site()
            
            # 2. 디렉토리 구조 생성
            self.create_directory_structure()
            
            # 3. 설정 파일 생성
            self.create_config_files()
            
            # 4. 템플릿 생성
            self.create_templates()
            
            # 5. Agent 스크립트 생성
            self.create_agent_scripts()
            
            # 6. GitHub Actions 워크플로우 생성
            self.create_github_workflows()
            
            print("✅ Hexo 블로그 설정 완료!")
            print(f"📁 블로그 디렉토리: {self.hexo_dir}")
            print(f"🌐 로컬 서버 실행: cd {self.hexo_dir} && npx hexo server")
            
        except Exception as e:
            print(f"❌ 설정 중 오류 발생: {e}")
            sys.exit(1)
    
    def init_hexo_site(self):
        """Hexo 사이트 초기화"""
        print("📦 Hexo 사이트 초기화...")
        
        # 기존 디렉토리가 있으면 제거
        if self.hexo_dir.exists():
            shutil.rmtree(self.hexo_dir)
        
        # Hexo 사이트 초기화
        subprocess.run([
            "npx", "hexo", "init", str(self.hexo_dir)
        ], check=True, cwd=self.publishing_dir)
        
        print("✅ Hexo 사이트 초기화 완료")
    
    def create_directory_structure(self):
        """디렉토리 구조 생성"""
        print("📁 디렉토리 구조 생성...")
        
        directories = [
            "source/_posts/series-1",
            "source/_posts/series-2", 
            "source/_posts/series-3",
            "source/_posts/series-4",
            "source/_posts/series-5",
            "source/_books",
            "source/_pages",
            "source/_data",
            "specs/series",
            "specs/books",
            "specs/agents",
            "agents",
            "scripts",
            "templates",
            "config",
            "logs"
        ]
        
        for directory in directories:
            dir_path = self.hexo_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
        
        print("✅ 디렉토리 구조 생성 완료")
    
    def create_config_files(self):
        """설정 파일 생성"""
        print("⚙️ 설정 파일 생성...")
        
        # Hexo 설정 파일
        hexo_config = {
            'title': 'AI 가이드 시리즈',
            'subtitle': 'Spec Driven Development로 배우는 AI와 자동화',
            'description': 'AI와 자동화를 통해 100배 생산성을 달성하는 완전한 가이드',
            'author': 'AI Agent Team',
            'language': 'ko',
            'timezone': 'Asia/Seoul',
            'url': 'https://kronenz.github.io',
            'root': '/',
            'permalink': ':year/:month/:day/:title/',
            'permalink_defaults': {},
            'source_dir': 'source',
            'public_dir': 'public',
            'tag_dir': 'tags',
            'archive_dir': 'archives',
            'category_dir': 'categories',
            'code_dir': 'downloads/code',
            'i18n_dir': ':lang',
            'skip_render': [],
            'new_post_name': ':title.md',
            'default_layout': 'post',
            'titlecase': False,
            'external_link': True,
            'filename_case': 0,
            'render_drafts': False,
            'post_asset_folder': False,
            'relative_link': False,
            'future': True,
            'highlight': {
                'enable': True,
                'line_number': True,
                'auto_detect': False,
                'tab_replace': ''
            },
            'default_category': 'uncategorized',
            'category_map': {
                'AI 가이드': 'ai-guide',
                '자동화': 'automation',
                '생산성': 'productivity',
                'DevOps': 'devops',
                'Devin 아키텍처': 'devin-architecture'
            },
            'tag_map': {},
            'date_format': 'YYYY-MM-DD',
            'time_format': 'HH:mm:ss',
            'per_page': 10,
            'pagination_dir': 'page',
            'plugins': [
                'hexo-generator-feed',
                'hexo-generator-sitemap',
                'hexo-generator-baidu-sitemap',
                'hexo-renderer-marked',
                'hexo-renderer-stylus',
                'hexo-server',
                'hexo-deployer-git',
                'hexo-generator-index',
                'hexo-generator-category',
                'hexo-generator-tag',
                'hexo-generator-archive'
            ],
            'deploy': {
                'type': 'git',
                'repo': 'https://github.com/kronenz/kronenz.github.io.git',
                'branch': 'main',
                'message': 'Deploy from AI Agent: {{ now(\'YYYY-MM-DD HH:mm:ss\') }}'
            },
            'search': {
                'path': 'search.xml',
                'field': 'post',
                'content': True,
                'format': 'html'
            },
            'utterances': {
                'repo': 'kronenz/kronenz.github.io',
                'issue_term': 'pathname',
                'theme': 'github-light'
            }
        }
        
        with open(self.hexo_dir / '_config.yml', 'w', encoding='utf-8') as f:
            yaml.dump(hexo_config, f, allow_unicode=True, default_flow_style=False)
        
        # Agent 설정 파일
        agent_config = {
            'agents': {
                'content_processor': {
                    'enabled': True,
                    'timeout': 300,
                    'retry_count': 3
                },
                'seo_optimizer': {
                    'enabled': True,
                    'timeout': 180,
                    'retry_count': 2
                },
                'publisher': {
                    'enabled': True,
                    'timeout': 600,
                    'retry_count': 3
                }
            },
            'processing': {
                'parallel_workers': 4,
                'batch_size': 10,
                'max_retries': 3
            },
            'output': {
                'format': 'markdown',
                'encoding': 'utf-8',
                'line_ending': 'lf'
            }
        }
        
        with open(self.hexo_dir / 'config' / 'agents.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(agent_config, f, allow_unicode=True, default_flow_style=False)
        
        print("✅ 설정 파일 생성 완료")
    
    def create_templates(self):
        """템플릿 생성"""
        print("📝 템플릿 생성...")
        
        # 블로그 포스트 템플릿
        post_template = """---
title: {{title}}
date: {{date}}
updated: {{updated}}
categories: [{{category}}]
tags: [{{tags}}]
permalink: /{{series_id}}/{{guide_id}}/
excerpt: {{excerpt}}
toc: true
mathjax: true
comments: true
series:
  id: {{series_id}}
  title: {{series_title}}
  position: {{position}}
seo:
  focus_keyword: {{focus_keyword}}
  meta_description: {{meta_description}}
  reading_time: {{reading_time}}
---

{{content}}
"""
        
        with open(self.hexo_dir / 'scaffolds' / 'post.md', 'w', encoding='utf-8') as f:
            f.write(post_template)
        
        # 시리즈 개요 템플릿
        series_template = """---
title: {{series_title}}
layout: page
---

# {{series_title}}

{{series_subtitle}}

{{series_description}}

## 가이드 목록

{{guide_list}}

## 학습 목표

{{learning_objectives}}

## 필요한 도구

{{required_tools}}

## 실습 프로젝트

{{practical_projects}}
"""
        
        with open(self.hexo_dir / 'scaffolds' / 'series-overview.md', 'w', encoding='utf-8') as f:
            f.write(series_template)
        
        # 온라인 도서 챕터 템플릿
        book_chapter_template = """---
title: {{chapter_title}}
date: {{date}}
updated: {{updated}}
book:
  id: {{book_id}}
  title: {{book_title}}
  chapter_number: {{chapter_number}}
  page_number: {{page_number}}
layout: book-chapter
toc: true
mathjax: true
comments: true
---

{{content}}
"""
        
        with open(self.hexo_dir / 'scaffolds' / 'book-chapter.md', 'w', encoding='utf-8') as f:
            f.write(book_chapter_template)
        
        print("✅ 템플릿 생성 완료")
    
    def create_agent_scripts(self):
        """Agent 스크립트 생성"""
        print("🤖 Agent 스크립트 생성...")
        
        # Content Processor Agent
        content_processor = '''#!/usr/bin/env python3
"""
Content Processor Agent
가이드 시리즈 콘텐츠를 Hexo 블로그 포스트로 변환
"""

import yaml
import markdown
from datetime import datetime
from pathlib import Path
import frontmatter
import re
import sys

class ContentProcessorAgent:
    def __init__(self, config_path="config/agents.yaml"):
        self.config = self.load_config(config_path)
        self.hexo_config = self.load_hexo_config()
    
    def process_series(self, series_path):
        """시리즈 전체 처리"""
        series_spec = self.load_series_spec(series_path)
        guide_specs = self.load_guide_specs(series_path)
        
        results = []
        for guide_spec in guide_specs:
            result = self.process_guide(guide_spec, series_spec)
            results.append(result)
        
        return {
            'series_spec': series_spec,
            'guide_results': results,
            'total_guides': len(guide_specs)
        }
    
    def process_guide(self, guide_spec, series_spec):
        """개별 가이드 처리"""
        try:
            # 1. Markdown 콘텐츠 로드
            markdown_content = self.load_markdown_content(guide_spec)
            
            # 2. Markdown 처리
            processed_content = self.process_markdown(markdown_content, guide_spec)
            
            # 3. Front-matter 생성
            front_matter = self.generate_front_matter(guide_spec, series_spec)
            
            # 4. Hexo 포스트 생성
            hexo_post = self.create_hexo_post(front_matter, processed_content)
            
            # 5. 파일 저장
            output_path = self.save_hexo_post(hexo_post, guide_spec, series_spec)
            
            return {
                'success': True,
                'guide_id': guide_spec['id'],
                'output_path': output_path,
                'word_count': processed_content.get('word_count', 0),
                'reading_time': processed_content.get('reading_time', 0)
            }
            
        except Exception as e:
            return {
                'success': False,
                'guide_id': guide_spec['id'],
                'error': str(e)
            }
    
    def load_series_spec(self, series_path):
        """시리즈 spec 로드"""
        spec_file = Path(series_path) / "series-spec.yaml"
        with open(spec_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def load_guide_specs(self, series_path):
        """가이드 spec들 로드"""
        guides_dir = Path(series_path) / "guides"
        guide_specs = []
        
        if guides_dir.exists():
            for spec_file in guides_dir.glob("*-spec.yaml"):
                with open(spec_file, 'r', encoding='utf-8') as f:
                    guide_spec = yaml.safe_load(f)
                    guide_specs.append(guide_spec)
        
        return sorted(guide_specs, key=lambda x: x['id'])
    
    def load_markdown_content(self, guide_spec):
        """Markdown 콘텐츠 로드"""
        content_source = guide_spec['content']['source']
        content_path = Path(content_source)
        
        if not content_path.exists():
            raise FileNotFoundError(f"Content file not found: {content_source}")
        
        with open(content_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def process_markdown(self, content, guide_spec):
        """Markdown 콘텐츠 처리"""
        # 코드 하이라이팅 설정
        md = markdown.Markdown(extensions=[
            'codehilite',
            'tables',
            'toc',
            'fenced_code',
            'attr_list',
            'def_list',
            'footnotes',
            'md_in_html'
        ])
        
        # Markdown 변환
        html_content = md.convert(content)
        
        # TOC 생성
        toc = md.toc
        
        return {
            'content': html_content,
            'toc': toc,
            'word_count': len(content.split()),
            'reading_time': self.calculate_reading_time(content)
        }
    
    def generate_front_matter(self, guide_spec, series_spec):
        """Hexo front-matter 생성"""
        front_matter = {
            'title': guide_spec['title'],
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'categories': [series_spec['metadata']['category']],
            'tags': guide_spec.get('publishing', {}).get('blog', {}).get('seo', {}).get('tags', []),
            'permalink': f"/{series_spec['id']}/{guide_spec['id']}/",
            'excerpt': self.generate_excerpt(guide_spec),
            'toc': True,
            'mathjax': True,
            'comments': True
        }
        
        # 시리즈 정보 추가
        front_matter['series'] = {
            'id': series_spec['id'],
            'title': series_spec['title'],
            'position': self.get_guide_position(guide_spec, series_spec)
        }
        
        return front_matter
    
    def create_hexo_post(self, front_matter, content):
        """Hexo 포스트 생성"""
        post = frontmatter.Post(content['content'])
        post.metadata = front_matter
        return post
    
    def save_hexo_post(self, hexo_post, guide_spec, series_spec):
        """Hexo 포스트 저장"""
        # 파일명 생성
        filename = f"{guide_spec['id']}-{self.slugify(guide_spec['title'])}.md"
        
        # 저장 경로
        output_dir = Path("source/_posts") / series_spec['id']
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / filename
        
        # 파일 저장
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(hexo_post))
        
        return str(output_path)
    
    def slugify(self, text):
        """텍스트를 URL 친화적인 슬러그로 변환"""
        text = re.sub(r'[^\\w\\s-]', '', text.lower())
        text = re.sub(r'[-\\s]+', '-', text)
        return text.strip('-')
    
    def calculate_reading_time(self, content):
        """읽기 시간 계산 (분)"""
        word_count = len(content.split())
        return max(1, word_count // 200)  # 분당 200단어로 계산
    
    def generate_excerpt(self, guide_spec):
        """요약 생성"""
        return guide_spec.get('subtitle', '') or guide_spec.get('description', '')
    
    def get_guide_position(self, guide_spec, series_spec):
        """가이드 순서 계산"""
        guides = series_spec.get('structure', {}).get('guides', [])
        for i, guide in enumerate(guides, 1):
            if guide['id'] == guide_spec['id']:
                return i
        return 0
    
    def load_config(self, config_path):
        """설정 파일 로드"""
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def load_hexo_config(self):
        """Hexo 설정 로드"""
        with open('_config.yml', 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

if __name__ == "__main__":
    agent = ContentProcessorAgent()
    # 실행 로직 추가
'''
        
        with open(self.hexo_dir / 'agents' / 'content_processor.py', 'w', encoding='utf-8') as f:
            f.write(content_processor)
        
        print("✅ Agent 스크립트 생성 완료")
    
    def create_github_workflows(self):
        """GitHub Actions 워크플로우 생성"""
        print("🔄 GitHub Actions 워크플로우 생성...")
        
        # 자동 출판 워크플로우
        publish_workflow = '''name: Publish Blog

on:
  push:
    branches: [main]
    paths: ['specs/**/*.yaml', 'specs/**/*.md']
  schedule:
    - cron: '0 2 * * *'  # 매일 오전 2시 실행
  workflow_dispatch:

jobs:
  process-specs:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          cache: 'npm'
      
      - name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'
          cache: 'pip'
      
      - name: Install Node.js dependencies
        run: |
          cd publishing/hexo-blog
          npm install
      
      - name: Install Python dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Process Specs
        run: |
          python scripts/process_specs.py --input specs/ --output publishing/hexo-blog/source/_posts/
      
      - name: Generate Blog Posts
        run: |
          cd publishing/hexo-blog
          python scripts/generate_blog_posts.py --input source/_posts/ --output source/
      
      - name: Build Hexo Site
        run: |
          cd publishing/hexo-blog
          npx hexo clean
          npx hexo generate
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./publishing/hexo-blog/public
          cname: kronenz.github.io
'''
        
        # .github/workflows 디렉토리 생성
        workflows_dir = self.base_dir / '.github' / 'workflows'
        workflows_dir.mkdir(parents=True, exist_ok=True)
        
        with open(workflows_dir / 'publish-blog.yml', 'w', encoding='utf-8') as f:
            f.write(publish_workflow)
        
        print("✅ GitHub Actions 워크플로우 생성 완료")
    
    def copy_existing_specs(self):
        """기존 spec 파일들 복사"""
        print("📋 기존 spec 파일들 복사...")
        
        # 시리즈 spec 파일들 복사
        for series_dir in self.specs_dir.glob('series-*'):
            if series_dir.is_dir():
                target_dir = self.hexo_dir / 'specs' / 'series' / series_dir.name
                target_dir.mkdir(parents=True, exist_ok=True)
                
                # README.md 복사
                if (series_dir / 'README.md').exists():
                    shutil.copy2(series_dir / 'README.md', target_dir / 'series-spec.yaml')
                
                # 가이드 파일들 복사
                guides_dir = target_dir / 'guides'
                guides_dir.mkdir(exist_ok=True)
                
                for guide_file in series_dir.glob('*.md'):
                    if guide_file.name != 'README.md':
                        # 가이드 spec 생성
                        guide_spec = {
                            'id': guide_file.stem,
                            'title': self.extract_title_from_markdown(guide_file),
                            'content': {
                                'source': str(guide_file.relative_to(self.hexo_dir)),
                                'type': 'markdown'
                            },
                            'publishing': {
                                'blog': {
                                    'enabled': True,
                                    'seo': {
                                        'focus_keyword': self.extract_keywords_from_markdown(guide_file),
                                        'tags': ['AI', '가이드', '자동화']
                                    }
                                }
                            }
                        }
                        
                        with open(guides_dir / f"{guide_file.stem}-spec.yaml", 'w', encoding='utf-8') as f:
                            yaml.dump(guide_spec, f, allow_unicode=True, default_flow_style=False)
        
        print("✅ 기존 spec 파일들 복사 완료")
    
    def extract_title_from_markdown(self, file_path):
        """Markdown 파일에서 제목 추출"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 첫 번째 H1 제목 찾기
        import re
        match = re.search(r'^# (.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        return file_path.stem
    
    def extract_keywords_from_markdown(self, file_path):
        """Markdown 파일에서 키워드 추출"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 간단한 키워드 추출 (실제로는 더 정교한 방법 사용)
        keywords = []
        if 'AI' in content:
            keywords.append('AI')
        if '자동화' in content:
            keywords.append('자동화')
        if '생산성' in content:
            keywords.append('생산성')
        
        return keywords if keywords else ['가이드']

def main():
    """메인 실행 함수"""
    print("🚀 Hexo 블로그 설정 시작")
    
    setup = HexoBlogSetup()
    setup.setup_hexo_blog()
    setup.copy_existing_specs()
    
    print("\n🎉 설정 완료!")
    print("\n다음 단계:")
    print("1. cd publishing/hexo-blog")
    print("2. npm install")
    print("3. python scripts/process_specs.py --input specs/ --output source/_posts/")
    print("4. npx hexo server")

if __name__ == "__main__":
    main()
