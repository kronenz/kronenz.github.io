#!/usr/bin/env python3
"""
{{ spec.title }}
{{ spec.description }}

이 예제는 {{ spec.context }}를 보여줍니다.
"""

{% if spec.imports %}
{% for import_line in spec.imports %}
{{ import_line }}
{% endfor %}
{% endif %}

{% if spec.classes %}
{% for class_def in spec.classes %}
class {{ class_def.name }}:
    """
    {{ class_def.description }}
    """
    
    def __init__(self{% if class_def.init_params %}, {{ class_def.init_params }}{% endif %}):
        """
        {{ class_def.name }} 초기화
        
        {% if class_def.init_params %}
        Args:
        {% for param in class_def.init_params.split(', ') %}
            {{ param }}: {{ param }} 설명
        {% endfor %}
        {% endif %}
        """
        {% if class_def.init_body %}
        {{ class_def.init_body }}
        {% endif %}
    
    {% if class_def.methods %}
    {% for method in class_def.methods %}
    def {{ method.name }}(self{% if method.params %}, {{ method.params }}{% endif %}):
        """
        {{ method.description }}
        
        {% if method.params %}
        Args:
        {% for param in method.params.split(', ') %}
            {{ param }}: {{ param }} 설명
        {% endfor %}
        {% endif %}
        
        {% if method.returns %}
        Returns:
            {{ method.returns }}
        {% endif %}
        """
        {% if method.body %}
        {{ method.body }}
        {% else %}
        # TODO: {{ method.name }} 메서드 구현
        pass
        {% endif %}
    
    {% endfor %}
    {% endif %}

{% endfor %}
{% endif %}

{% if spec.functions %}
{% for function in spec.functions %}
def {{ function.name }}({{ function.params }}):
    """
    {{ function.description }}
    
    Args:
    {% for param in function.params.split(', ') %}
        {{ param }}: {{ param }} 설명
    {% endfor %}
    
    {% if function.returns %}
    Returns:
        {{ function.returns }}
    {% endif %}
    """
    {% if function.body %}
    {{ function.body }}
    {% else %}
    # TODO: {{ function.name }} 함수 구현
    pass
    {% endif %}

{% endfor %}
{% endif %}

{% if spec.main_section %}
def main():
    """
    메인 실행 함수
    """
    {{ spec.main_section }}

if __name__ == "__main__":
    main()
{% endif %}

{% if spec.usage_example %}
# 사용 예제
{{ spec.usage_example }}
{% endif %}