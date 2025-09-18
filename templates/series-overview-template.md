# {{ spec.title }}

{{ spec.overview }}

## 📚 가이드 목록

{% if spec.sections.guides %}
{% for guide in spec.sections.guides %}
### {{ guide.guide_number }}: {{ guide.title }}
**{{ guide.subtitle }}**

{% if guide.description %}
{{ guide.description }}
{% endif %}

{% if guide.key_topics %}
**주요 주제:**
{% for topic in guide.key_topics %}
- {{ topic }}
{% endfor %}
{% endif %}

{% if guide.estimated_time %}
**예상 소요 시간:** {{ guide.estimated_time }}
{% endif %}

{% if guide.difficulty %}
**난이도:** {{ guide.difficulty }}
{% endif %}

{% endfor %}
{% endif %}

## 🎯 학습 목표

이 시리즈를 완료하면 다음을 달성할 수 있습니다:

{% for objective in spec.objectives %}
- {{ objective }}
{% endfor %}

## 🛠️ 필요한 도구

{% if spec.tools %}
{% for tool in spec.tools %}
- {{ tool }}
{% endfor %}
{% endif %}

## 🏗️ 아키텍처 개요

{% if spec.architecture %}
{{ spec.architecture }}
{% endif %}

## 📊 성과 측정

{% if spec.metrics %}
### {{ spec.metrics.title }}

{% for metric in spec.metrics.items %}
- **{{ metric.name }}**: {{ metric.description }}
{% endfor %}
{% endif %}

## 🚀 다음 단계

{% if spec.next_series %}
이 시리즈를 완료한 후에는 [{{ spec.next_series.title }}]({{ spec.next_series.path }})로 진행하여 {{ spec.next_series.description }}을 학습할 수 있습니다.
{% endif %}

## 📖 추가 리소스

{% if spec.resources %}
{% for resource in spec.resources %}
- [{{ resource.title }}]({{ resource.url }})
{% endfor %}
{% endif %}

---

**"{{ spec.title }}"** - {{ spec.overview }}