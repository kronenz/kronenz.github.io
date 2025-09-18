# 출하 부두 구축

## 테스트 통과 후 자동으로 배포를 관리하는 DevOps 에이전트

## 📖 개요

이 가이드는 모든 테스트가 통과한 후 자동으로 배포를 관리하는 DevOps 에이전트를 구축하는 방법을 다룹니다. 완전 자동화된 배포 파이프라인을 통해 안정적이고 효율적인 배포 프로세스를 구현합니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

- DevOps 에이전트 설계 및 구현
- 배포 전략 수립 및 자동화
- 환경 관리 자동화 시스템 구축
- 롤백 메커니즘 구현
- 모니터링 및 알림 시스템 구축

## 📋 사전 요구사항

- Docker 및 컨테이너 기술 이해
- CI/CD 파이프라인 개념 숙지
- Python 중급 수준
- 클라우드 플랫폼 기본 지식

## ⏱️ 예상 소요 시간

**4시간** (난이도: 고급)

## 🔧 필요한 도구

- Python 3.8+
- Git
- 텍스트 에디터 (VS Code 권장)
- 터미널/명령 프롬프트

## 📚 핵심 개념

### 자동 배포 아키텍처

테스트 통과부터 프로덕션 배포까지의 전체 프로세스를 자동화하는 아키텍처를 설계합니다.

### 환경 관리 전략

개발, 스테이징, 프로덕션 환경을 일관되게 관리하고 배포하는 전략을 수립합니다.

### 배포 안전성 보장

블루-그린 배포, 카나리 배포 등을 활용하여 안전한 배포를 보장하는 방법을 학습합니다.


## 🛠️ 실습 단계

### DevOps 에이전트 구축

배포 작업을 자동으로 수행하는 DevOps 에이전트를 CrewAI로 구축합니다.

### Docker 컨테이너화

애플리케이션을 Docker 컨테이너로 패키징하고 배포하는 시스템을 구축합니다.

### 배포 파이프라인 구현

GitHub Actions를 사용하여 자동 배포 파이프라인을 구현합니다.

### 모니터링 및 알림 설정

배포 상태를 모니터링하고 문제 발생 시 알림을 보내는 시스템을 구축합니다.


## 💻 코드 예제

### DevOps 에이전트

```python
from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
import docker
import requests
import json
from datetime import datetime

class DevOpsAgent:
    def __init__(self, openai_api_key, docker_client):
        self.llm = OpenAI(openai_api_key=openai_api_key)
        self.docker_client = docker_client
        
        self.deployment_agent = Agent(
            role='DevOps Engineer',
            goal='Automate deployment processes and ensure system reliability',
            backstory='''You are an expert DevOps engineer with extensive experience 
            in containerization, CI/CD, and cloud deployment. You excel at 
            automating complex deployment processes and ensuring system stability.''',
            verbose=True,
            allow_delegation=False
        )
    
    def deploy_application(self, app_config):
        """애플리케이션 배포"""
        deployment_plan = self.create_deployment_plan(app_config)
        
        # 배포 단계별 실행
        for step in deployment_plan:
            try:
                self.execute_deployment_step(step)
            except Exception as e:
                self.handle_deployment_error(step, e)
                raise
        
        return self.verify_deployment(app_config)
    
    def create_deployment_plan(self, app_config):
        """배포 계획 생성"""
        task = Task(
            description=f"""
            다음 애플리케이션 설정을 바탕으로 배포 계획을 생성해주세요:
            
            {json.dumps(app_config, indent=2)}
            
            다음 단계들을 포함해주세요:
            1. 컨테이너 빌드
            2. 이미지 태깅
            3. 레지스트리 푸시
            4. 환경별 배포
            5. 헬스 체크
            6. 트래픽 전환
            """,
            agent=self.deployment_agent,
            expected_output="Detailed deployment plan with step-by-step instructions"
        )
        
        crew = Crew(
            agents=[self.deployment_agent],
            tasks=[task],
            verbose=True
        )
        
        result = crew.kickoff()
        return self.parse_deployment_plan(result)
    
    def execute_deployment_step(self, step):
        """배포 단계 실행"""
        step_type = step['type']
        
        if step_type == 'build_container':
            self.build_docker_image(step['config'])
        elif step_type == 'push_image':
            self.push_to_registry(step['config'])
        elif step_type == 'deploy_to_environment':
            self.deploy_to_environment(step['config'])
        elif step_type == 'health_check':
            self.perform_health_check(step['config'])
        elif step_type == 'traffic_switch':
            self.switch_traffic(step['config'])
    
    def build_docker_image(self, config):
        """Docker 이미지 빌드"""
        image_name = config['image_name']
        tag = config['tag']
        dockerfile_path = config['dockerfile_path']
        
        try:
            image, build_logs = self.docker_client.images.build(
                path=dockerfile_path,
                tag=f"{image_name}:{tag}",
                rm=True
            )
            
            self.logger.info(f"Successfully built image: {image_name}:{tag}")
            return image
            
        except Exception as e:
            self.logger.error(f"Failed to build image: {e}")
            raise
    
    def deploy_to_environment(self, config):
        """환경에 배포"""
        environment = config['environment']
        image_name = config['image_name']
        tag = config['tag']
        
        # 환경별 배포 로직
        if environment == 'staging':
            self.deploy_to_staging(image_name, tag)
        elif environment == 'production':
            self.deploy_to_production(image_name, tag)
    
    def perform_health_check(self, config):
        """헬스 체크 수행"""
        url = config['health_check_url']
        timeout = config.get('timeout', 30)
        
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            
            self.logger.info(f"Health check passed: {url}")
            return True
            
        except Exception as e:
            self.logger.error(f"Health check failed: {e}")
            return False
```

### 배포 모니터링 시스템

```python
class DeploymentMonitor:
    def __init__(self, notification_config):
        self.notification_config = notification_config
        self.deployment_history = []
    
    def monitor_deployment(self, deployment_id, app_config):
        """배포 모니터링"""
        monitoring_data = {
            'deployment_id': deployment_id,
            'start_time': datetime.now(),
            'app_config': app_config,
            'status': 'in_progress'
        }
        
        try:
            # 배포 상태 확인
            status = self.check_deployment_status(deployment_id)
            monitoring_data['status'] = status
            
            # 메트릭 수집
            metrics = self.collect_metrics(app_config)
            monitoring_data['metrics'] = metrics
            
            # 알림 전송
            if status == 'failed':
                self.send_alert(monitoring_data)
            elif status == 'completed':
                self.send_success_notification(monitoring_data)
            
        except Exception as e:
            monitoring_data['status'] = 'error'
            monitoring_data['error'] = str(e)
            self.send_alert(monitoring_data)
        
        finally:
            monitoring_data['end_time'] = datetime.now()
            self.deployment_history.append(monitoring_data)
    
    def check_deployment_status(self, deployment_id):
        """배포 상태 확인"""
        # 실제 구현에서는 Kubernetes API나 클라우드 API를 사용
        # 여기서는 시뮬레이션
        import random
        
        statuses = ['in_progress', 'completed', 'failed']
        return random.choice(statuses)
    
    def collect_metrics(self, app_config):
        """메트릭 수집"""
        metrics = {
            'cpu_usage': self.get_cpu_usage(),
            'memory_usage': self.get_memory_usage(),
            'response_time': self.get_response_time(),
            'error_rate': self.get_error_rate()
        }
        
        return metrics
    
    def send_alert(self, monitoring_data):
        """알림 전송"""
        alert_message = f"""
        🚨 Deployment Alert
        
        Deployment ID: {monitoring_data['deployment_id']}
        Status: {monitoring_data['status']}
        Time: {monitoring_data['start_time']}
        
        Application: {monitoring_data['app_config']['name']}
        Environment: {monitoring_data['app_config']['environment']}
        
        Please check the deployment logs for more details.
        """
        
        # Slack, 이메일, SMS 등으로 알림 전송
        self.send_to_slack(alert_message)
        self.send_email_alert(alert_message)
    
    def send_to_slack(self, message):
        """Slack 알림 전송"""
        webhook_url = self.notification_config.get('slack_webhook')
        if webhook_url:
            payload = {'text': message}
            requests.post(webhook_url, json=payload)
```


## 🔍 고급 기능


## 🚨 문제 해결


## 📖 추가 리소스

- [Docker 공식 문서](https://docs.docker.com/)
- [Kubernetes 문서](https://kubernetes.io/docs/)
- [GitHub Actions 배포 가이드](https://docs.github.com/en/actions/deployment)

## 🚀 다음 단계

이 가이드를 완료한 후 다음 가이드들을 학습해보세요:

- [엔드-투-엔드 프로젝트](2-11-end-to-end-project.md)

## 📝 요약

이 가이드에서는 출하 부두 구축에 대해 학습했습니다. 주요 내용은 다음과 같습니다:

- DevOps 에이전트 설계 및 구현
- 배포 전략 수립 및 자동화
- 환경 관리 자동화 시스템 구축
- 롤백 메커니즘 구현
- 모니터링 및 알림 시스템 구축

다음 가이드에서는 더 고급 주제를 다룰 예정입니다.

---

**"출하 부두 구축"** - 에이전틱 SaaS 조직 구축을 위한 핵심 가이드