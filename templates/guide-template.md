# {{ spec.title }}

{% if spec.subtitle %}
## {{ spec.subtitle }}
{% endif %}

## 📖 개요

{{ spec.overview }}

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

{% for objective in spec.objectives %}
- {{ objective }}
{% endfor %}

## 📋 사전 요구사항

{% for prerequisite in spec.prerequisites %}
- {{ prerequisite }}
{% endfor %}

## ⏱️ 예상 소요 시간

**{{ spec.estimated_time }}** (난이도: {{ spec.difficulty }})

## 🔧 필요한 도구

- Python 3.8+
- Git
- 텍스트 에디터 (VS Code 권장)
- 터미널/명령 프롬프트

## 📚 핵심 개념

{% if spec.sections.core_concepts %}
{% for concept in spec.sections.core_concepts %}
### {{ concept.title }}

{{ concept.content }}

{% endfor %}
{% endif %}

## 🛠️ 실습 단계

{% if spec.sections.practical_steps %}
{% for step in spec.sections.practical_steps %}
### {{ step.title }}

{{ step.content }}

{% endfor %}
{% endif %}

## 💻 코드 예제

{% if spec.code_examples %}
{% for example in spec.code_examples %}
### {{ example.title }}

```{{ example.language }}
{{ example.code }}
```

{% endfor %}
{% endif %}

## 🔍 고급 기능

{% if spec.sections.advanced_features %}
{% for feature in spec.sections.advanced_features %}
### {{ feature.title }}

{{ feature.content }}

{% endfor %}
{% endif %}

## 🚨 문제 해결

{% if spec.sections.troubleshooting %}
{% for issue in spec.sections.troubleshooting %}
### {{ issue.title }}

{{ issue.content }}

{% endfor %}
{% endif %}

## 📖 추가 리소스

{% if spec.resources %}
{% for resource in spec.resources %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}
{% endif %}

## 🚀 다음 단계

{% if spec.next_steps %}
이 가이드를 완료한 후 다음 가이드들을 학습해보세요:

{% for next_step in spec.next_steps %}
- [{{ next_step.title }}]({{ next_step.path }})
{% endfor %}
{% endif %}

## 📝 요약

이 가이드에서는 {{ spec.title }}에 대해 학습했습니다. 주요 내용은 다음과 같습니다:

{% for objective in spec.objectives %}
- {{ objective }}
{% endfor %}

다음 가이드에서는 더 고급 주제를 다룰 예정입니다.

---

**"{{ spec.title }}"** - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드