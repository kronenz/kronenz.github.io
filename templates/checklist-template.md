# {{ spec.title }} 체크리스트

{{ spec.description }}

## 📋 사전 준비 체크리스트

### 환경 설정
{% for item in spec.prerequisites.environment %}
- [ ] {{ item }}
{% endfor %}

### 도구 설치
{% for item in spec.prerequisites.tools %}
- [ ] {{ item }}
{% endfor %}

### 계정 설정
{% for item in spec.prerequisites.accounts %}
- [ ] {{ item }}
{% endfor %}

## 🎯 학습 목표 체크리스트

{% for objective in spec.objectives %}
- [ ] {{ objective }}
{% endfor %}

## 🛠️ 실습 체크리스트

{% if spec.practical_steps %}
{% for step in spec.practical_steps %}
### {{ step.title }}

{% for item in step.items %}
- [ ] {{ item }}
{% endfor %}

{% endfor %}
{% endif %}

## ✅ 완료 확인 체크리스트

### 기본 기능
{% if spec.completion and spec.completion.basic %}
{% for item in spec.completion.basic %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

### 고급 기능
{% if spec.completion and spec.completion.advanced %}
{% for item in spec.completion.advanced %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

### 테스트
{% if spec.completion and spec.completion.testing %}
{% for item in spec.completion.testing %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

## 🔍 품질 검증 체크리스트

### 코드 품질
{% if spec.quality and spec.quality.code %}
{% for item in spec.quality.code %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

### 문서화
{% if spec.quality and spec.quality.documentation %}
{% for item in spec.quality.documentation %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

### 보안
{% if spec.quality and spec.quality.security %}
{% for item in spec.quality.security %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

## 🚀 배포 준비 체크리스트

### 배포 전 검증
{% if spec.deployment and spec.deployment.pre_deployment %}
{% for item in spec.deployment.pre_deployment %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

### 배포 실행
{% if spec.deployment and spec.deployment.deployment %}
{% for item in spec.deployment.deployment %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

### 배포 후 검증
{% if spec.deployment and spec.deployment.post_deployment %}
{% for item in spec.deployment.post_deployment %}
- [ ] {{ item }}
{% endfor %}
{% endif %}

## 📊 성과 측정

### 정량적 지표
{% if spec.metrics and spec.metrics.quantitative %}
{% for metric in spec.metrics.quantitative %}
- [ ] {{ metric.name }}: {{ metric.target }}
{% endfor %}
{% endif %}

### 정성적 지표
{% if spec.metrics and spec.metrics.qualitative %}
{% for metric in spec.metrics.qualitative %}
- [ ] {{ metric.name }}: {{ metric.description }}
{% endfor %}
{% endif %}

## 🎉 완료!

모든 체크리스트를 완료했다면 다음 단계로 진행하세요:

{% if spec.next_steps %}
{% for next_step in spec.next_steps %}
- [{{ next_step.title }}]({{ next_step.path }})
{% endfor %}
{% endif %}

---

**체크리스트 완료율: [ ]%**

*이 체크리스트를 통해 {{ spec.title }}의 모든 단계를 체계적으로 완료할 수 있습니다.*