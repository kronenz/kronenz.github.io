# Hexo 통합 설정 가이드

## 개요

이 가이드는 기존 가이드 시리즈를 Hexo 기반 GitHub Pages 블로그로 통합하는 구체적인 설정 방법을 제공합니다.

## 🚀 1단계: Hexo 사이트 초기화

### 1.1 프로젝트 구조 생성

```bash
# 기존 spec 디렉토리에서 시작
cd /root/spec

# Hexo 사이트 초기화
npx hexo init publishing-system
cd publishing-system

# 필요한 디렉토리 생성
mkdir -p source/_posts/series-1
mkdir -p source/_posts/series-2
mkdir -p source/_posts/series-3
mkdir -p source/_posts/series-4
mkdir -p source/_posts/series-5
mkdir -p source/_books
mkdir -p source/_pages
mkdir -p source/_data
mkdir -p specs/series
mkdir -p specs/books
mkdir -p specs/agents
mkdir -p agents
mkdir -p scripts
mkdir -p templates
```

### 1.2 Hexo 설정 파일

```yaml
# _config.yml
title: AI 가이드 시리즈
subtitle: Spec Driven Development로 배우는 AI와 자동화
description: AI와 자동화를 통해 100배 생산성을 달성하는 완전한 가이드
author: AI Agent Team
language: ko
timezone: Asia/Seoul

# URL 설정
url: https://kronenz.github.io
root: /
permalink: :year/:month/:day/:title/
permalink_defaults:

# 디렉토리 설정
source_dir: source
public_dir: public
tag_dir: tags
archive_dir: archives
category_dir: categories
code_dir: downloads/code
i18n_dir: :lang
skip_render:

# 글쓰기 설정
new_post_name: :title.md
default_layout: post
titlecase: false
external_link: true
filename_case: 0
render_drafts: false
post_asset_folder: false
relative_link: false
future: true

# 코드 하이라이팅
highlight:
  enable: true
  line_number: true
  auto_detect: false
  tab_replace:

# 카테고리 및 태그
default_category: uncategorized
category_map:
  'AI 가이드': ai-guide
  '자동화': automation
  '생산성': productivity
  'DevOps': devops
  'Devin 아키텍처': devin-architecture
tag_map:

# 날짜 형식
date_format: YYYY-MM-DD
time_format: HH:mm:ss

# 페이지 설정
per_page: 10
pagination_dir: page

# 플러그인
plugins:
  - hexo-generator-feed
  - hexo-generator-sitemap
  - hexo-generator-baidu-sitemap
  - hexo-renderer-marked
  - hexo-renderer-stylus
  - hexo-server
  - hexo-deployer-git
  - hexo-generator-index
  - hexo-generator-category
  - hexo-generator-tag
  - hexo-generator-archive

# 배포 설정
deploy:
  type: git
  repo: https://github.com/kronenz/kronenz.github.io.git
  branch: main
  message: "Deploy from AI Agent: {{ now('YYYY-MM-DD HH:mm:ss') }}"

# 검색 설정
search:
  path: search.xml
  field: post
  content: true
  format: html

# 댓글 시스템
utterances:
  repo: kronenz/kronenz.github.io
  issue_term: pathname
  theme: github-light
```

## 🔧 2단계: Agent 시스템 구현

### 2.1 Content Processor Agent

```python
# agents/content_processor.py
import yaml
import markdown
from datetime import datetime
from pathlib import Path
import frontmatter
import re

class ContentProcessorAgent:
    def __init__(self, config_path="config/agents.yaml"):
        self.config = self.load_config(config_path)
        self.hexo_config = self.load_hexo_config()
        self.templates = self.load_templates()
    
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
            
            # 4. SEO 최적화
            seo_data = self.optimize_seo(processed_content, guide_spec)
            
            # 5. Hexo 포스트 생성
            hexo_post = self.create_hexo_post(front_matter, processed_content, seo_data)
            
            # 6. 파일 저장
            output_path = self.save_hexo_post(hexo_post, guide_spec, series_spec)
            
            return {
                'success': True,
                'guide_id': guide_spec['id'],
                'output_path': output_path,
                'seo_score': seo_data.get('score', 0),
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
        
        # 이미지 경로 최적화
        html_content = self.optimize_image_paths(html_content, guide_spec)
        
        # 내부 링크 최적화
        html_content = self.optimize_internal_links(html_content, guide_spec)
        
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
        
        # SEO 메타데이터 추가
        seo_config = guide_spec.get('publishing', {}).get('blog', {}).get('seo', {})
        if seo_config:
            front_matter['seo'] = {
                'focus_keyword': seo_config.get('focus_keyword'),
                'meta_description': seo_config.get('meta_description'),
                'reading_time': seo_config.get('reading_time')
            }
        
        return front_matter
    
    def optimize_seo(self, content, guide_spec):
        """SEO 최적화"""
        seo_config = guide_spec.get('publishing', {}).get('blog', {}).get('seo', {})
        
        # 키워드 밀도 분석
        focus_keyword = seo_config.get('focus_keyword', '')
        keyword_density = self.calculate_keyword_density(content['content'], focus_keyword)
        
        # 메타 설명 생성
        meta_description = seo_config.get('meta_description', '')
        if not meta_description:
            meta_description = self.generate_meta_description(content['content'])
        
        # SEO 점수 계산
        seo_score = self.calculate_seo_score(content, focus_keyword, keyword_density)
        
        return {
            'focus_keyword': focus_keyword,
            'meta_description': meta_description,
            'keyword_density': keyword_density,
            'score': seo_score,
            'recommendations': self.generate_seo_recommendations(seo_score)
        }
    
    def create_hexo_post(self, front_matter, content, seo_data):
        """Hexo 포스트 생성"""
        # Front-matter와 콘텐츠 결합
        post = frontmatter.Post(content['content'])
        post.metadata = front_matter
        
        # SEO 데이터 추가
        post.metadata['seo'] = seo_data
        
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
        text = re.sub(r'[^\w\s-]', '', text.lower())
        text = re.sub(r'[-\s]+', '-', text)
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
```

### 2.2 SEO Optimizer Agent

```python
# agents/seo_optimizer.py
import re
from collections import Counter
import nltk
from textstat import flesch_reading_ease

class SEOOptimizerAgent:
    def __init__(self, config_path="config/seo.yaml"):
        self.config = self.load_config(config_path)
        self.stop_words = self.load_stop_words()
    
    def optimize_content(self, content, guide_spec):
        """콘텐츠 SEO 최적화"""
        try:
            # 1. 키워드 분석
            keywords = self.analyze_keywords(content)
            
            # 2. 콘텐츠 구조 최적화
            optimized_content = self.optimize_structure(content, keywords)
            
            # 3. 메타데이터 최적화
            meta_data = self.optimize_metadata(guide_spec, keywords)
            
            # 4. 내부 링크 최적화
            internal_links = self.optimize_internal_links(content, guide_spec)
            
            # 5. SEO 점수 계산
            seo_score = self.calculate_seo_score(optimized_content, meta_data)
            
            return {
                'success': True,
                'optimized_content': optimized_content,
                'meta_data': meta_data,
                'keywords': keywords,
                'internal_links': internal_links,
                'seo_score': seo_score
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def analyze_keywords(self, content):
        """키워드 분석"""
        # 텍스트에서 HTML 태그 제거
        text = re.sub(r'<[^>]+>', '', content)
        
        # 단어 추출 및 정규화
        words = re.findall(r'\b\w+\b', text.lower())
        
        # 불용어 제거
        filtered_words = [word for word in words if word not in self.stop_words and len(word) > 3]
        
        # 빈도 계산
        word_freq = Counter(filtered_words)
        
        # 키워드 점수 계산
        keywords = []
        for word, freq in word_freq.most_common(20):
            score = self.calculate_keyword_score(word, freq, len(filtered_words))
            keywords.append({
                'word': word,
                'frequency': freq,
                'density': freq / len(filtered_words) * 100,
                'score': score
            })
        
        return keywords
    
    def calculate_keyword_score(self, word, frequency, total_words):
        """키워드 점수 계산"""
        # 빈도 기반 점수
        freq_score = (frequency / total_words) * 100
        
        # 길이 기반 점수 (너무 짧거나 긴 단어는 낮은 점수)
        length_score = 1.0
        if len(word) < 4:
            length_score = 0.5
        elif len(word) > 15:
            length_score = 0.7
        
        # 최종 점수
        return freq_score * length_score
    
    def optimize_structure(self, content, keywords):
        """콘텐츠 구조 최적화"""
        # 주요 키워드를 헤딩에 포함
        primary_keyword = keywords[0]['word'] if keywords else ''
        
        # H1 태그 최적화
        content = self.optimize_h1_tag(content, primary_keyword)
        
        # H2, H3 태그 최적화
        content = self.optimize_heading_tags(content, keywords)
        
        return content
    
    def optimize_h1_tag(self, content, primary_keyword):
        """H1 태그 최적화"""
        if not primary_keyword:
            return content
        
        # H1 태그에 키워드 포함 확인
        h1_pattern = r'<h1[^>]*>(.*?)</h1>'
        if re.search(h1_pattern, content):
            # 기존 H1 태그에 키워드 추가
            content = re.sub(
                h1_pattern,
                lambda m: f'<h1>{primary_keyword} - {m.group(1)}</h1>',
                content
            )
        else:
            # H1 태그가 없으면 추가
            content = f'<h1>{primary_keyword}</h1>\n\n{content}'
        
        return content
    
    def calculate_seo_score(self, content, meta_data):
        """SEO 점수 계산"""
        score = 0
        
        # 제목 최적화 (20점)
        title_score = self.evaluate_title(meta_data.get('title', ''))
        score += title_score * 0.2
        
        # 메타 설명 최적화 (15점)
        description_score = self.evaluate_meta_description(meta_data.get('description', ''))
        score += description_score * 0.15
        
        # 키워드 밀도 (15점)
        keyword_density_score = self.evaluate_keyword_density(content)
        score += keyword_density_score * 0.15
        
        # 헤딩 구조 (10점)
        heading_score = self.evaluate_heading_structure(content)
        score += heading_score * 0.1
        
        # 내부 링크 (10점)
        internal_link_score = self.evaluate_internal_links(content)
        score += internal_link_score * 0.1
        
        # 이미지 최적화 (10점)
        image_score = self.evaluate_images(content)
        score += image_score * 0.1
        
        # 가독성 (10점)
        readability_score = self.evaluate_readability(content)
        score += readability_score * 0.1
        
        # 콘텐츠 길이 (10점)
        length_score = self.evaluate_content_length(content)
        score += length_score * 0.1
        
        return min(score, 100)  # 최대 100점
```

## 🚀 3단계: 자동화 스크립트

### 3.1 Spec 처리 스크립트

```python
# scripts/process_specs.py
#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import yaml
import json
from datetime import datetime

# Agent import
sys.path.append(str(Path(__file__).parent.parent))
from agents.content_processor import ContentProcessorAgent
from agents.seo_optimizer import SEOOptimizerAgent

def main():
    parser = argparse.ArgumentParser(description='Process specs and generate blog posts')
    parser.add_argument('--input', required=True, help='Input specs directory')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--series', help='Specific series to process')
    parser.add_argument('--verbose', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Agent 초기화
    content_processor = ContentProcessorAgent()
    seo_optimizer = SEOOptimizerAgent()
    
    # Spec 디렉토리 스캔
    specs_dir = Path(args.input)
    series_dirs = [d for d in specs_dir.glob('series-*') if d.is_dir()]
    
    if args.series:
        series_dirs = [d for d in series_dirs if d.name == args.series]
    
    total_processed = 0
    total_errors = 0
    
    for series_dir in series_dirs:
        print(f"Processing series: {series_dir.name}")
        
        try:
            # 시리즈 처리
            result = content_processor.process_series(series_dir)
            
            if result['total_guides'] > 0:
                print(f"  ✓ Processed {result['total_guides']} guides")
                total_processed += result['total_guides']
                
                # SEO 최적화
                for guide_result in result['guide_results']:
                    if guide_result['success']:
                        seo_result = seo_optimizer.optimize_content(
                            guide_result, result['series_spec']
                        )
                        if seo_result['success']:
                            print(f"    ✓ SEO optimized: {guide_result['guide_id']}")
                        else:
                            print(f"    ✗ SEO optimization failed: {guide_result['guide_id']}")
                            total_errors += 1
                    else:
                        print(f"    ✗ Failed: {guide_result['guide_id']} - {guide_result['error']}")
                        total_errors += 1
            else:
                print(f"  ⚠ No guides found in {series_dir.name}")
                
        except Exception as e:
            print(f"  ✗ Error processing {series_dir.name}: {e}")
            total_errors += 1
    
    # 결과 요약
    print(f"\nProcessing complete:")
    print(f"  Total guides processed: {total_processed}")
    print(f"  Total errors: {total_errors}")
    print(f"  Success rate: {((total_processed - total_errors) / total_processed * 100):.1f}%" if total_processed > 0 else "N/A")

if __name__ == "__main__":
    main()
```

### 3.2 블로그 생성 스크립트

```python
# scripts/generate_blog_posts.py
#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import yaml
import json
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Generate blog posts from processed specs')
    parser.add_argument('--input', required=True, help='Input posts directory')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--template', help='Template to use')
    
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    output_dir = Path(args.output)
    
    # 출력 디렉토리 생성
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 시리즈 데이터 생성
    series_data = generate_series_data(input_dir)
    
    # 시리즈 데이터 파일 저장
    with open(output_dir / '_data' / 'series.yml', 'w', encoding='utf-8') as f:
        yaml.dump(series_data, f, allow_unicode=True, default_flow_style=False)
    
    # 인덱스 페이지 생성
    generate_index_page(series_data, output_dir)
    
    # 시리즈 페이지 생성
    generate_series_pages(series_data, output_dir)
    
    print(f"Blog generation complete. Output: {output_dir}")

def generate_series_data(input_dir):
    """시리즈 데이터 생성"""
    series_data = {}
    
    for series_dir in input_dir.glob('series-*'):
        if series_dir.is_dir():
            series_id = series_dir.name
            series_spec_file = series_dir / 'series-spec.yaml'
            
            if series_spec_file.exists():
                with open(series_spec_file, 'r', encoding='utf-8') as f:
                    series_spec = yaml.safe_load(f)
                
                # 포스트 목록 생성
                posts = []
                for post_file in series_dir.glob('*.md'):
                    if post_file.name != 'series-spec.yaml':
                        posts.append({
                            'title': post_file.stem,
                            'path': str(post_file.relative_to(input_dir)),
                            'date': post_file.stat().st_mtime
                        })
                
                series_data[series_id] = {
                    'id': series_id,
                    'title': series_spec['series']['title'],
                    'subtitle': series_spec['series']['subtitle'],
                    'description': series_spec['series']['description'],
                    'category': series_spec['series']['metadata']['category'],
                    'tags': series_spec['series']['metadata']['tags'],
                    'posts': sorted(posts, key=lambda x: x['date'])
                }
    
    return series_data

def generate_index_page(series_data, output_dir):
    """인덱스 페이지 생성"""
    index_content = f"""---
title: AI 가이드 시리즈
layout: page
---

# AI 가이드 시리즈

AI와 자동화를 통해 100배 생산성을 달성하는 완전한 가이드 모음입니다.

## 시리즈 목록

"""
    
    for series_id, series_info in series_data.items():
        index_content += f"""
### [{series_info['title']}](/{series_id}/)

{series_info['description']}

- **카테고리**: {series_info['category']}
- **태그**: {', '.join(series_info['tags'])}
- **가이드 수**: {len(series_info['posts'])}개

"""
    
    with open(output_dir / 'index.md', 'w', encoding='utf-8') as f:
        f.write(index_content)

def generate_series_pages(series_data, output_dir):
    """시리즈 페이지 생성"""
    for series_id, series_info in series_data.items():
        series_page_content = f"""---
title: {series_info['title']}
layout: page
---

# {series_info['title']}

{series_info['subtitle']}

{series_info['description']}

## 가이드 목록

"""
        
        for i, post in enumerate(series_info['posts'], 1):
            series_page_content += f"{i}. [{post['title']}](/{series_id}/{post['title']}/)\n"
        
        series_dir = output_dir / series_id
        series_dir.mkdir(exist_ok=True)
        
        with open(series_dir / 'index.md', 'w', encoding='utf-8') as f:
            f.write(series_page_content)

if __name__ == "__main__":
    main()
```

## 🔄 4단계: GitHub Actions 워크플로우

### 4.1 자동 출판 워크플로우

```yaml
# .github/workflows/publish-blog.yml
name: Publish Blog

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
          cd publishing-system
          npm install
      
      - name: Install Python dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Process Specs
        run: |
          python scripts/process_specs.py --input specs/ --output publishing-system/source/_posts/
      
      - name: Generate Blog Posts
        run: |
          cd publishing-system
          python scripts/generate_blog_posts.py --input source/_posts/ --output source/
      
      - name: Build Hexo Site
        run: |
          cd publishing-system
          npx hexo clean
          npx hexo generate
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./publishing-system/public
          cname: kronenz.github.io
```

## 📊 5단계: 모니터링 및 분석

### 5.1 성능 모니터링

```python
# monitoring/performance_monitor.py
import time
import psutil
import json
from datetime import datetime
from pathlib import Path

class PerformanceMonitor:
    def __init__(self, log_file="logs/performance.json"):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(exist_ok=True)
        self.metrics = {
            'processing_times': [],
            'memory_usage': [],
            'cpu_usage': [],
            'error_count': 0,
            'success_count': 0
        }
    
    def start_monitoring(self):
        """모니터링 시작"""
        self.start_time = time.time()
        self.start_memory = psutil.virtual_memory().used
        self.start_cpu = psutil.cpu_percent()
    
    def end_monitoring(self, success=True):
        """모니터링 종료"""
        end_time = time.time()
        processing_time = end_time - self.start_time
        
        # 메트릭 기록
        self.metrics['processing_times'].append(processing_time)
        self.metrics['memory_usage'].append(psutil.virtual_memory().used)
        self.metrics['cpu_usage'].append(psutil.cpu_percent())
        
        if success:
            self.metrics['success_count'] += 1
        else:
            self.metrics['error_count'] += 1
        
        # 로그 저장
        self.save_metrics()
    
    def save_metrics(self):
        """메트릭 저장"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'metrics': self.metrics
        }
        
        # 기존 로그 로드
        if self.log_file.exists():
            with open(self.log_file, 'r', encoding='utf-8') as f:
                logs = json.load(f)
        else:
            logs = []
        
        logs.append(log_entry)
        
        # 로그 저장
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
    
    def get_performance_summary(self):
        """성능 요약 반환"""
        if not self.metrics['processing_times']:
            return None
        
        return {
            'total_processed': self.metrics['success_count'] + self.metrics['error_count'],
            'success_rate': self.metrics['success_count'] / (self.metrics['success_count'] + self.metrics['error_count']) * 100,
            'average_processing_time': sum(self.metrics['processing_times']) / len(self.metrics['processing_times']),
            'average_memory_usage': sum(self.metrics['memory_usage']) / len(self.metrics['memory_usage']),
            'average_cpu_usage': sum(self.metrics['cpu_usage']) / len(self.metrics['cpu_usage'])
        }
```

## 🎯 실행 방법

### 1. 초기 설정

```bash
# 1. Hexo 사이트 초기화
npx hexo init publishing-system
cd publishing-system

# 2. 의존성 설치
npm install
pip install -r requirements.txt

# 3. 설정 파일 복사
cp ../publishing/_config.yml .
cp -r ../publishing/source/* source/
cp -r ../publishing/specs/* specs/
cp -r ../publishing/agents/* agents/
cp -r ../publishing/scripts/* scripts/
```

### 2. Spec 처리

```bash
# 모든 시리즈 처리
python scripts/process_specs.py --input specs/ --output source/_posts/

# 특정 시리즈만 처리
python scripts/process_specs.py --input specs/ --output source/_posts/ --series series-5
```

### 3. 블로그 생성

```bash
# 블로그 포스트 생성
python scripts/generate_blog_posts.py --input source/_posts/ --output source/

# Hexo 사이트 빌드
npx hexo clean
npx hexo generate

# 로컬 서버 실행
npx hexo server
```

### 4. GitHub Pages 배포

```bash
# GitHub Pages에 배포
npx hexo deploy
```

## 📚 다음 단계

이 설정을 완료한 후 다음 작업을 진행합니다:

1. **테마 커스터마이징**: 가이드 시리즈에 최적화된 테마 개발
2. **검색 기능**: Algolia 또는 다른 검색 서비스 통합
3. **댓글 시스템**: Utterances 또는 Disqus 통합
4. **분석 도구**: Google Analytics, Google Search Console 통합
5. **성능 최적화**: 이미지 최적화, CDN 설정

---

**"Hexo 통합 설정 가이드"** - 기존 가이드 시리즈를 Hexo 기반 GitHub Pages 블로그로 완전 자동화하여 출판하는 시스템을 구축합니다!
