# GitHub Pages 블로그 출판 시스템 Spec

## 개요

이 spec은 가이드 시리즈를 GitHub Pages를 활용한 markdown 기반 블로그로 출판하고, 향후 다른 주제와 분야의 가이드 시리즈, 온라인 도서를 위한 구조를 정의합니다. [kronenz.github.io](https://github.com/kronenz/kronenz.github.io/)의 Hexo 기반 구조를 참고하여 Spec Driven Development 방식으로 Agent가 하위 spec을 선택해서 진행할 수 있게 설계됩니다.

## 🎯 목표

1. **GitHub Pages 통합**: Hexo 기반의 정적 사이트 생성으로 GitHub Pages에 자동 배포
2. **Markdown 기반 콘텐츠**: 기존 가이드 시리즈를 Markdown으로 변환하여 블로그 포스트로 출판
3. **Agent 기반 자동화**: AI Agent가 spec을 선택하고 자동으로 콘텐츠를 생성 및 출판
4. **다중 시리즈 지원**: 다양한 주제와 분야의 가이드 시리즈를 체계적으로 관리
5. **온라인 도서 기능**: 시리즈를 온라인 도서 형태로도 제공

## 🏗️ 시스템 아키텍처

### 1. 전체 구조

```
github-pages-blog/
├── .github/
│   └── workflows/
│       ├── publish-blog.yml          # 블로그 자동 출판
│       ├── process-specs.yml         # Spec 처리
│       └── deploy-book.yml           # 온라인 도서 배포
├── source/
│   ├── _posts/                       # 블로그 포스트
│   │   ├── series-1/
│   │   ├── series-2/
│   │   └── series-5/
│   ├── _books/                       # 온라인 도서
│   │   ├── ai-productivity-guide/
│   │   └── devops-mastery/
│   ├── _drafts/                      # 초안
│   ├── _pages/                       # 정적 페이지
│   │   ├── about.md
│   │   ├── series.md
│   │   └── books.md
│   └── _data/                        # 데이터 파일
│       ├── series.yml
│       ├── books.yml
│       └── agents.yml
├── themes/
│   └── custom-theme/                 # 커스텀 테마
├── scaffolds/                        # 템플릿
│   ├── post.md
│   ├── book-chapter.md
│   └── series-overview.md
├── specs/                            # Spec 파일들
│   ├── series/
│   ├── books/
│   └── agents/
├── agents/                           # Agent 구현
│   ├── content-processor/
│   ├── seo-optimizer/
│   └── publisher/
├── _config.yml                       # Hexo 설정
├── package.json
└── README.md
```

### 2. Hexo 기반 구조

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

# 배포 설정
deploy:
  type: git
  repo: https://github.com/kronenz/kronenz.github.io.git
  branch: main
  message: "Deploy from AI Agent: {{ now('YYYY-MM-DD HH:mm:ss') }}"
```

## 📋 Spec 구조

### 1. 시리즈 Spec

```yaml
# specs/series/series-5/series-spec.yaml
series:
  id: "series-5"
  title: "자율성의 경제학"
  subtitle: "100배 생산성 달성"
  description: "AI와 자동화를 통해 100배 생산성을 달성하는 방법"
  
  metadata:
    author: "AI Agent Team"
    category: "Productivity"
    tags: ["AI", "Automation", "Productivity", "FinOps", "RL"]
    difficulty: "Advanced"
    duration: "10 weeks"
    target_audience: "Developers, DevOps, Product Managers"
    cover_image: "/images/series-5-cover.jpg"
  
  structure:
    type: "progressive"
    total_guides: 10
    guides:
      - id: "5-1"
        title: "100배 생산성 정량화"
        type: "foundation"
        prerequisites: []
        estimated_time: "30 min"
        difficulty: "Intermediate"
      - id: "5-2"
        title: "AI FinOps 입문"
        type: "concept"
        prerequisites: ["5-1"]
        estimated_time: "45 min"
        difficulty: "Intermediate"
      # ... 더 많은 가이드들
  
  publishing:
    blog:
      enabled: true
      template: "series-guide"
      seo:
        focus_keyword: "100배 생산성"
        meta_description: "AI와 자동화를 통해 100배 생산성을 달성하는 완전한 가이드"
        tags: ["AI", "Productivity", "Automation"]
      social:
        twitter_card: "summary_large_image"
        og_image: "/images/series-5-og.jpg"
    
    book:
      enabled: true
      template: "progressive-book"
      title: "AI로 100배 생산성 달성하기"
      isbn: "978-89-1234-567-8"
      chapters: "auto-generated"
      table_of_contents: true
      index: true
      cover_design: "custom"
```

### 2. 가이드 Spec

```yaml
# specs/series/series-5/guides/5-1-guide-spec.yaml
guide:
  id: "5-1"
  series_id: "series-5"
  title: "100배 생산성 정량화"
  subtitle: "생산성 측정의 과학적 접근"
  
  content:
    type: "markdown"
    source: "5-1-100x-productivity-quantification.md"
    word_count: 2500
    reading_time: "15 min"
  
  structure:
    sections:
      - type: "overview"
        required: true
        weight: 1
      - type: "learning-objectives"
        required: true
        weight: 2
      - type: "main-content"
        required: true
        weight: 3
        subsections:
          - "생산성의 정의"
          - "측정 방법론"
          - "100배 생산성 지표"
          - "경제적 가치 계산"
      - type: "code-examples"
        required: true
        weight: 4
        languages: ["python", "yaml", "markdown"]
      - type: "practical-exercises"
        required: false
        weight: 5
      - type: "next-steps"
        required: true
        weight: 6
      - type: "resources"
        required: true
        weight: 7
  
  publishing:
    blog:
      template: "guide-post"
      layout: "post"
      seo:
        focus_keyword: "생산성 정량화"
        meta_description: "생산성 측정의 과학적 접근과 100배 생산성 달성 방법"
        reading_time: "15 min"
        difficulty: "Intermediate"
        tags: ["생산성", "측정", "AI", "자동화"]
      social:
        twitter_card: "summary"
        og_image: "/images/5-1-og.jpg"
      comments:
        enabled: true
        provider: "utterances"
    
    book:
      chapter_number: 1
      chapter_title: "생산성 정량화의 기초"
      page_number: 1
      word_count: 2500
```

### 3. Agent Spec

```yaml
# specs/agents/content-processor-agent.yaml
agent:
  id: "content-processor"
  name: "Content Processor Agent"
  description: "가이드 시리즈 콘텐츠를 Hexo 블로그 포스트로 변환하는 Agent"
  version: "1.0.0"
  
  capabilities:
    - "markdown-processing"
    - "front-matter-generation"
    - "image-optimization"
    - "code-highlighting"
    - "seo-optimization"
    - "social-meta-generation"
  
  inputs:
    - type: "guide-spec"
      required: true
      format: "yaml"
    - type: "series-spec"
      required: true
      format: "yaml"
    - type: "markdown-content"
      required: true
      format: "markdown"
  
  outputs:
    - type: "hexo-post"
      format: "markdown"
      location: "source/_posts/"
    - type: "front-matter"
      format: "yaml"
    - type: "seo-data"
      format: "json"
  
  processing:
    workflow:
      - step: "parse-spec"
        description: "가이드 spec 파싱"
      - step: "process-markdown"
        description: "Markdown 콘텐츠 처리"
      - step: "generate-front-matter"
        description: "Hexo front-matter 생성"
      - step: "optimize-seo"
        description: "SEO 최적화"
      - step: "generate-social-meta"
        description: "소셜 미디어 메타데이터 생성"
      - step: "create-hexo-post"
        description: "Hexo 포스트 파일 생성"
  
  resources:
    cpu: "low"
    memory: "512MB"
    storage: "100MB"
    network: "low"
  
  performance:
    processing_time: "< 30 seconds per post"
    success_rate: "> 95%"
    error_handling: "automatic_retry"
```

## 🤖 Agent 워크플로우

### 1. Content Processor Agent

```python
# agents/content-processor/content_processor.py
import yaml
import markdown
from datetime import datetime
from pathlib import Path
import frontmatter

class ContentProcessorAgent:
    def __init__(self, config):
        self.config = config
        self.hexo_config = self.load_hexo_config()
        self.templates = self.load_templates()
    
    def process_guide(self, guide_spec, series_spec, markdown_content):
        """가이드 처리"""
        try:
            # 1. Spec 파싱
            parsed_spec = self.parse_guide_spec(guide_spec)
            
            # 2. Markdown 처리
            processed_content = self.process_markdown(markdown_content, parsed_spec)
            
            # 3. Front-matter 생성
            front_matter = self.generate_front_matter(parsed_spec, series_spec)
            
            # 4. SEO 최적화
            seo_data = self.optimize_seo(processed_content, parsed_spec)
            
            # 5. 소셜 미디어 메타데이터 생성
            social_meta = self.generate_social_meta(parsed_spec, seo_data)
            
            # 6. Hexo 포스트 생성
            hexo_post = self.create_hexo_post(
                front_matter, processed_content, seo_data, social_meta
            )
            
            # 7. 파일 저장
            output_path = self.save_hexo_post(hexo_post, parsed_spec)
            
            return {
                'success': True,
                'output_path': output_path,
                'processing_time': self.calculate_processing_time(),
                'seo_score': seo_data.get('score', 0)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'processing_time': self.calculate_processing_time()
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
    
    def create_hexo_post(self, front_matter, content, seo_data, social_meta):
        """Hexo 포스트 생성"""
        # Front-matter와 콘텐츠 결합
        post = frontmatter.Post(content['content'])
        post.metadata = front_matter
        
        # SEO 데이터 추가
        post.metadata['seo'] = seo_data
        
        # 소셜 미디어 메타데이터 추가
        post.metadata['social'] = social_meta
        
        return post
```

### 2. SEO Optimizer Agent

```python
# agents/seo-optimizer/seo_optimizer.py
import re
from collections import Counter
import nltk
from textstat import flesch_reading_ease

class SEOOptimizerAgent:
    def __init__(self, config):
        self.config = config
        self.stop_words = self.load_stop_words()
        self.keyword_tools = KeywordTools()
    
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
            
            # 5. 이미지 최적화
            image_optimization = self.optimize_images(content, guide_spec)
            
            # 6. SEO 점수 계산
            seo_score = self.calculate_seo_score(optimized_content, meta_data)
            
            return {
                'success': True,
                'optimized_content': optimized_content,
                'meta_data': meta_data,
                'keywords': keywords,
                'internal_links': internal_links,
                'image_optimization': image_optimization,
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
    
    def optimize_structure(self, content, keywords):
        """콘텐츠 구조 최적화"""
        # 주요 키워드를 헤딩에 포함
        primary_keyword = keywords[0]['word'] if keywords else ''
        
        # H1 태그 최적화
        content = self.optimize_h1_tag(content, primary_keyword)
        
        # H2, H3 태그 최적화
        content = self.optimize_heading_tags(content, keywords)
        
        # 문단 구조 최적화
        content = self.optimize_paragraphs(content)
        
        # 리스트 최적화
        content = self.optimize_lists(content)
        
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

## 🔄 GitHub Actions 워크플로우

### 1. 자동 출판 워크플로우

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
      
      - name: Install dependencies
        run: |
          npm install
          pip install -r requirements.txt
      
      - name: Process Specs
        run: |
          python scripts/process_specs.py --input specs/ --output source/_posts/
      
      - name: Generate Blog Posts
        run: |
          python scripts/generate_blog_posts.py --input source/_posts/ --output source/
      
      - name: Build Hexo Site
        run: |
          npx hexo clean
          npx hexo generate
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
          cname: kronenz.github.io
```

### 2. Spec 처리 워크플로우

```yaml
# .github/workflows/process-specs.yml
name: Process Specs

on:
  push:
    branches: [main]
    paths: ['specs/**/*.yaml']
  pull_request:
    paths: ['specs/**/*.yaml']

jobs:
  validate-specs:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      
      - name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Validate Specs
        run: |
          python scripts/validate_specs.py --input specs/
      
      - name: Generate Preview
        run: |
          python scripts/generate_preview.py --input specs/ --output preview/
      
      - name: Upload Preview
        uses: actions/upload-artifact@v3
        with:
          name: spec-preview
          path: preview/
```

## 📊 모니터링 및 분석

### 1. 성능 지표

```python
# monitoring/analytics.py
class BlogAnalytics:
    def __init__(self):
        self.metrics = {
            'posts_published': 0,
            'series_completed': 0,
            'seo_scores': [],
            'processing_times': [],
            'error_rates': []
        }
    
    def track_post_publication(self, post_data):
        """포스트 출판 추적"""
        self.metrics['posts_published'] += 1
        
        # SEO 점수 기록
        if 'seo_score' in post_data:
            self.metrics['seo_scores'].append(post_data['seo_score'])
        
        # 처리 시간 기록
        if 'processing_time' in post_data:
            self.metrics['processing_times'].append(post_data['processing_time'])
    
    def generate_report(self):
        """분석 보고서 생성"""
        return {
            'total_posts': self.metrics['posts_published'],
            'average_seo_score': sum(self.metrics['seo_scores']) / len(self.metrics['seo_scores']) if self.metrics['seo_scores'] else 0,
            'average_processing_time': sum(self.metrics['processing_times']) / len(self.metrics['processing_times']) if self.metrics['processing_times'] else 0,
            'success_rate': self.calculate_success_rate()
        }
```

### 2. SEO 모니터링

```python
# monitoring/seo_monitor.py
class SEOMonitor:
    def __init__(self):
        self.seo_metrics = {
            'keyword_rankings': {},
            'page_speeds': {},
            'mobile_scores': {},
            'accessibility_scores': {}
        }
    
    def monitor_keyword_rankings(self, keywords, urls):
        """키워드 순위 모니터링"""
        for keyword, url in zip(keywords, urls):
            ranking = self.get_google_ranking(keyword, url)
            self.seo_metrics['keyword_rankings'][keyword] = ranking
    
    def monitor_page_speed(self, urls):
        """페이지 속도 모니터링"""
        for url in urls:
            speed_score = self.get_page_speed_score(url)
            self.seo_metrics['page_speeds'][url] = speed_score
```

## 🎯 다음 단계

이 spec을 기반으로 다음 작업을 진행합니다:

1. **Hexo 사이트 설정**: 기존 GitHub Pages 사이트에 Hexo 통합
2. **Agent 구현**: Content Processor와 SEO Optimizer Agent 구현
3. **워크플로우 구축**: GitHub Actions를 통한 자동화 파이프라인
4. **테마 커스터마이징**: 가이드 시리즈에 최적화된 테마 개발
5. **모니터링 시스템**: 성능 및 SEO 모니터링 구축

---

**"GitHub Pages 블로그 출판 시스템"** - Hexo 기반의 정적 사이트 생성과 AI Agent를 활용하여 가이드 시리즈를 자동으로 블로그로 출판하고, GitHub Pages에 배포하는 완전 자동화된 시스템을 구축합니다!
