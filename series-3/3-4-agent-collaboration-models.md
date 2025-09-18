# 3-4: 에이전트 협업 모델 설계 - 계층적 모델과 협력적 모델의 구현

## 📋 개요

AI 에이전트들이 효과적으로 협업할 수 있는 모델을 설계하는 것은 디지털 팀 운영의 핵심입니다. 이 가이드에서는 계층적 모델과 협력적 모델을 중심으로 다양한 협업 패턴을 분석하고, 실제 구현 가능한 협업 시스템을 구축하는 방법을 학습합니다.

## 🎯 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

1. **협업 패턴 분석**: 다양한 에이전트 협업 모델의 특징과 장단점 이해
2. **통신 프로토콜 설계**: 에이전트 간 효율적인 의사소통 체계 구축
3. **의사결정 구조 구현**: 계층적 및 협력적 의사결정 메커니즘 설계
4. **갈등 해결 시스템**: 에이전트 간 갈등을 예방하고 해결하는 체계 구축

## 📋 사전 요구사항

- CrewAI 기본 개념 이해
- Python 객체지향 프로그래밍 숙지
- 비동기 프로그래밍 경험
- 팀 관리 및 협업 도구 사용 경험

## ⏱️ 예상 소요 시간

**3시간** (난이도: 고급)

## 🔧 필요한 도구

- Python 3.8+
- CrewAI Framework
- asyncio (비동기 처리)
- Redis (메시지 큐)
- Docker (컨테이너화)

## 📚 핵심 개념

### 1. 협업 모델의 기본 원리

#### 계층적 모델 (Hierarchical Model)
```
Manager Agent
    ├── Product Strategy Agent
    ├── Development Team
    │   ├── Frontend Agent
    │   ├── Backend Agent
    │   └── QA Agent
    └── DevOps Agent
```

**특징:**
- 명확한 상하 관계와 책임 분담
- 의사결정이 상위에서 하위로 전달
- 효율적인 리소스 관리 가능
- 갈등 해결이 상대적으로 용이

#### 협력적 모델 (Collaborative Model)
```
Product Strategy Agent ←→ Development Agent
         ↕                        ↕
   QA Agent ←→ DevOps Agent ←→ Frontend Agent
```

**특징:**
- 수평적 관계와 상호 협력
- 분산된 의사결정 구조
- 빠른 반응과 적응성
- 창의적 문제 해결 능력

### 2. 통신 프로토콜 설계

#### 메시지 기반 통신
```python
class AgentMessage:
    def __init__(self, sender: str, receiver: str, 
                 message_type: str, content: dict):
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.content = content
        self.timestamp = datetime.now()
        self.priority = Priority.NORMAL
```

#### 이벤트 기반 아키텍처
```python
class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)
    
    def subscribe(self, event_type: str, callback):
        self.subscribers[event_type].append(callback)
    
    def publish(self, event: AgentEvent):
        for callback in self.subscribers[event.type]:
            asyncio.create_task(callback(event))
```

## 🛠️ 실습 단계

### 1단계: 기본 협업 모델 구현

#### 계층적 모델 구현
```python
from crewai import Agent, Task, Crew
from typing import List, Dict

class HierarchicalTeam:
    def __init__(self):
        self.manager = self._create_manager_agent()
        self.team_agents = self._create_team_agents()
        self.communication_protocol = CommunicationProtocol()
    
    def _create_manager_agent(self) -> Agent:
        return Agent(
            role="팀 매니저",
            goal="프로젝트 전체 관리 및 의사결정",
            backstory="경험이 풍부한 프로젝트 매니저",
            verbose=True,
            allow_delegation=True
        )
    
    def _create_team_agents(self) -> List[Agent]:
        return [
            Agent(
                role="제품 전략가",
                goal="제품 요구사항 분석 및 전략 수립",
                backstory="사용자 중심 사고의 제품 전문가",
                verbose=True
            ),
            Agent(
                role="개발자",
                goal="고품질 코드 작성 및 기능 구현",
                backstory="기술에 열정적인 개발자",
                verbose=True
            ),
            Agent(
                role="QA 엔지니어",
                goal="품질 보증 및 테스트 수행",
                backstory="세심하고 꼼꼼한 QA 전문가",
                verbose=True
            )
        ]
```

#### 협력적 모델 구현
```python
class CollaborativeTeam:
    def __init__(self):
        self.agents = self._create_collaborative_agents()
        self.consensus_engine = ConsensusEngine()
        self.shared_knowledge = SharedKnowledgeBase()
    
    def _create_collaborative_agents(self) -> List[Agent]:
        agents = []
        roles = ["전략가", "개발자", "디자이너", "QA", "DevOps"]
        
        for role in roles:
            agent = Agent(
                role=role,
                goal=f"{role} 역할 수행 및 팀 협력",
                backstory=f"협력적 사고의 {role} 전문가",
                verbose=True,
                allow_delegation=False  # 협력적 모델에서는 위임 금지
            )
            agents.append(agent)
        
        return agents
```

### 2단계: 통신 프로토콜 구현

#### 메시지 큐 시스템
```python
import asyncio
import redis
from typing import Dict, Any

class MessageQueue:
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_client = redis.from_url(redis_url)
        self.subscribers = {}
    
    async def send_message(self, channel: str, message: Dict[str, Any]):
        """메시지 전송"""
        await asyncio.get_event_loop().run_in_executor(
            None, 
            self.redis_client.publish, 
            channel, 
            json.dumps(message)
        )
    
    async def subscribe(self, channel: str, callback):
        """채널 구독"""
        pubsub = self.redis_client.pubsub()
        pubsub.subscribe(channel)
        
        async def message_handler():
            for message in pubsub.listen():
                if message['type'] == 'message':
                    data = json.loads(message['data'])
                    await callback(data)
        
        asyncio.create_task(message_handler())
```

#### 에이전트 간 통신 래퍼
```python
class AgentCommunication:
    def __init__(self, agent_id: str, message_queue: MessageQueue):
        self.agent_id = agent_id
        self.message_queue = message_queue
        self.message_handlers = {}
    
    async def send_to_agent(self, target_agent: str, message: Dict[str, Any]):
        """특정 에이전트에게 메시지 전송"""
        message['sender'] = self.agent_id
        message['receiver'] = target_agent
        await self.message_queue.send_message(f"agent_{target_agent}", message)
    
    async def broadcast(self, message: Dict[str, Any]):
        """모든 에이전트에게 브로드캐스트"""
        message['sender'] = self.agent_id
        await self.message_queue.send_message("broadcast", message)
    
    def register_handler(self, message_type: str, handler):
        """메시지 핸들러 등록"""
        self.message_handlers[message_type] = handler
    
    async def handle_message(self, message: Dict[str, Any]):
        """메시지 처리"""
        message_type = message.get('type')
        if message_type in self.message_handlers:
            await self.message_handlers[message_type](message)
```

### 3단계: 의사결정 시스템 구현

#### 계층적 의사결정
```python
class HierarchicalDecisionMaker:
    def __init__(self, manager_agent: Agent):
        self.manager_agent = manager_agent
        self.decision_history = []
    
    async def make_decision(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """계층적 의사결정 수행"""
        decision_task = Task(
            description=f"다음 상황에 대한 의사결정을 수행하세요: {context}",
            agent=self.manager_agent,
            expected_output="의사결정 결과와 근거"
        )
        
        result = await decision_task.execute()
        decision = {
            'decision': result,
            'timestamp': datetime.now(),
            'context': context
        }
        
        self.decision_history.append(decision)
        return decision
```

#### 협력적 의사결정 (합의 기반)
```python
class CollaborativeDecisionMaker:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.consensus_threshold = 0.6  # 60% 이상 합의 필요
    
    async def make_consensus_decision(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """합의 기반 의사결정"""
        votes = []
        
        # 각 에이전트의 의견 수집
        for agent in self.agents:
            vote_task = Task(
                description=f"다음 상황에 대한 의견을 제시하세요: {context}",
                agent=agent,
                expected_output="의견과 근거"
            )
            
            vote_result = await vote_task.execute()
            votes.append({
                'agent': agent.role,
                'vote': vote_result,
                'timestamp': datetime.now()
            })
        
        # 합의 도출
        consensus = self._calculate_consensus(votes)
        return {
            'consensus': consensus,
            'votes': votes,
            'context': context
        }
    
    def _calculate_consensus(self, votes: List[Dict]) -> Dict[str, Any]:
        """합의 계산 로직"""
        # 간단한 다수결 로직 (실제로는 더 복잡한 알고리즘 사용)
        vote_counts = {}
        for vote in votes:
            key = str(vote['vote'])
            vote_counts[key] = vote_counts.get(key, 0) + 1
        
        total_votes = len(votes)
        for option, count in vote_counts.items():
            if count / total_votes >= self.consensus_threshold:
                return {
                    'decision': option,
                    'confidence': count / total_votes,
                    'total_votes': total_votes
                }
        
        return {
            'decision': 'NO_CONSENSUS',
            'confidence': 0,
            'total_votes': total_votes
        }
```

### 4단계: 갈등 해결 시스템

#### 갈등 감지 및 분류
```python
class ConflictDetector:
    def __init__(self):
        self.conflict_patterns = [
            'contradictory_goals',
            'resource_competition',
            'priority_mismatch',
            'communication_breakdown'
        ]
    
    def detect_conflict(self, messages: List[Dict]) -> List[Dict]:
        """갈등 상황 감지"""
        conflicts = []
        
        for pattern in self.conflict_patterns:
            if self._check_pattern(messages, pattern):
                conflicts.append({
                    'type': pattern,
                    'severity': self._calculate_severity(messages, pattern),
                    'timestamp': datetime.now()
                })
        
        return conflicts
    
    def _check_pattern(self, messages: List[Dict], pattern: str) -> bool:
        """특정 갈등 패턴 확인"""
        # 실제 구현에서는 NLP 기반 패턴 매칭 사용
        conflict_keywords = {
            'contradictory_goals': ['반대', '다른', '충돌'],
            'resource_competition': ['우선순위', '리소스', '경쟁'],
            'priority_mismatch': ['중요도', '우선순위', '차이'],
            'communication_breakdown': ['이해', '소통', '명확']
        }
        
        keywords = conflict_keywords.get(pattern, [])
        for message in messages:
            content = message.get('content', '').lower()
            if any(keyword in content for keyword in keywords):
                return True
        
        return False
```

#### 갈등 해결 메커니즘
```python
class ConflictResolver:
    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.resolution_strategies = {
            'contradictory_goals': self._resolve_goal_conflict,
            'resource_competition': self._resolve_resource_conflict,
            'priority_mismatch': self._resolve_priority_conflict,
            'communication_breakdown': self._resolve_communication_conflict
        }
    
    async def resolve_conflict(self, conflict: Dict) -> Dict[str, Any]:
        """갈등 해결"""
        conflict_type = conflict['type']
        strategy = self.resolution_strategies.get(conflict_type)
        
        if strategy:
            resolution = await strategy(conflict)
            return {
                'conflict': conflict,
                'resolution': resolution,
                'status': 'RESOLVED',
                'timestamp': datetime.now()
            }
        else:
            return {
                'conflict': conflict,
                'resolution': None,
                'status': 'UNRESOLVED',
                'timestamp': datetime.now()
            }
    
    async def _resolve_goal_conflict(self, conflict: Dict) -> Dict[str, Any]:
        """목표 갈등 해결"""
        # 중재자 에이전트를 통한 해결
        mediator = Agent(
            role="중재자",
            goal="갈등 해결 및 합의 도출",
            backstory="경험이 풍부한 중재 전문가",
            verbose=True
        )
        
        mediation_task = Task(
            description=f"다음 갈등을 해결하세요: {conflict}",
            agent=mediator,
            expected_output="해결 방안과 합의 내용"
        )
        
        result = await mediation_task.execute()
        return {
            'method': 'mediation',
            'result': result,
            'participants': self.agents
        }
```

## 💻 코드 예제

### 완전한 협업 시스템 구현
```python
import asyncio
from typing import List, Dict, Any

class AgentCollaborationSystem:
    def __init__(self, team_type: str = "hierarchical"):
        self.team_type = team_type
        self.message_queue = MessageQueue()
        self.conflict_detector = ConflictDetector()
        self.conflict_resolver = None
        self.agents = []
        self.communication = {}
    
    async def initialize_team(self, agent_configs: List[Dict[str, Any]]):
        """팀 초기화"""
        if self.team_type == "hierarchical":
            self.agents = self._create_hierarchical_team(agent_configs)
        else:
            self.agents = self._create_collaborative_team(agent_configs)
        
        # 통신 시스템 설정
        for agent in self.agents:
            comm = AgentCommunication(agent.role, self.message_queue)
            self.communication[agent.role] = comm
            
            # 메시지 핸들러 등록
            comm.register_handler('task_request', self._handle_task_request)
            comm.register_handler('status_update', self._handle_status_update)
            comm.register_handler('help_request', self._handle_help_request)
        
        # 갈등 해결 시스템 초기화
        self.conflict_resolver = ConflictResolver(self.agents)
    
    async def execute_collaborative_task(self, task_description: str) -> Dict[str, Any]:
        """협업 작업 실행"""
        # 작업을 에이전트들에게 배포
        task_results = []
        
        for agent in self.agents:
            task = Task(
                description=task_description,
                agent=agent,
                expected_output="작업 결과"
            )
            
            result = await task.execute()
            task_results.append({
                'agent': agent.role,
                'result': result,
                'timestamp': datetime.now()
            })
        
        # 결과 통합
        integrated_result = await self._integrate_results(task_results)
        
        # 갈등 감지 및 해결
        conflicts = self.conflict_detector.detect_conflict(task_results)
        if conflicts:
            for conflict in conflicts:
                resolution = await self.conflict_resolver.resolve_conflict(conflict)
                integrated_result['conflicts'] = integrated_result.get('conflicts', [])
                integrated_result['conflicts'].append(resolution)
        
        return integrated_result
    
    async def _integrate_results(self, results: List[Dict]) -> Dict[str, Any]:
        """결과 통합"""
        # 간단한 결과 통합 로직
        integrated = {
            'summary': '통합된 작업 결과',
            'contributions': results,
            'timestamp': datetime.now()
        }
        
        return integrated
```

## 🔍 고급 기능

### 1. 동적 팀 구성
```python
class DynamicTeamManager:
    def __init__(self):
        self.available_agents = {}
        self.active_teams = {}
    
    async def create_team_for_task(self, task_requirements: Dict) -> str:
        """작업 요구사항에 맞는 동적 팀 구성"""
        required_skills = task_requirements.get('skills', [])
        team_size = task_requirements.get('team_size', 3)
        
        # 필요한 스킬을 가진 에이전트 선택
        selected_agents = self._select_agents_by_skills(required_skills, team_size)
        
        # 팀 ID 생성
        team_id = f"team_{len(self.active_teams) + 1}"
        
        # 팀 구성
        team = {
            'id': team_id,
            'agents': selected_agents,
            'created_at': datetime.now(),
            'status': 'active'
        }
        
        self.active_teams[team_id] = team
        return team_id
```

### 2. 성과 모니터링
```python
class TeamPerformanceMonitor:
    def __init__(self):
        self.metrics = {
            'collaboration_efficiency': 0,
            'conflict_resolution_time': 0,
            'task_completion_rate': 0,
            'communication_quality': 0
        }
    
    def update_metrics(self, event: Dict[str, Any]):
        """메트릭 업데이트"""
        event_type = event.get('type')
        
        if event_type == 'task_completed':
            self.metrics['task_completion_rate'] += 1
        elif event_type == 'conflict_resolved':
            resolution_time = event.get('resolution_time', 0)
            self.metrics['conflict_resolution_time'] = resolution_time
        elif event_type == 'communication':
            quality = event.get('quality', 0)
            self.metrics['communication_quality'] = quality
    
    def get_performance_report(self) -> Dict[str, Any]:
        """성과 보고서 생성"""
        return {
            'metrics': self.metrics,
            'timestamp': datetime.now(),
            'recommendations': self._generate_recommendations()
        }
```

## 🚨 문제 해결

### 1. 통신 지연 문제
**문제**: 에이전트 간 통신이 지연되어 작업 효율성이 떨어짐

**해결책**:
- 비동기 메시지 처리 구현
- 메시지 큐 최적화
- 캐싱 시스템 도입

### 2. 갈등 해결 실패
**문제**: 에이전트 간 갈등이 해결되지 않아 작업이 중단됨

**해결책**:
- 다단계 갈등 해결 프로세스 구현
- 중재자 에이전트 도입
- 투표 기반 의사결정 시스템

### 3. 리소스 경합
**문제**: 여러 에이전트가 동일한 리소스를 사용하려고 함

**해결책**:
- 리소스 관리자 에이전트 구현
- 우선순위 기반 할당 시스템
- 대기열 및 스케줄링 메커니즘

## 📖 추가 리소스

- [CrewAI 공식 문서](https://docs.crewai.com/)
- [분산 시스템 설계 원칙](https://microservices.io/)
- [에이전트 기반 모델링](https://agent-based-modeling.com/)
- [협업 도구 비교 분석](https://collaboration-tools.dev/)

## 🚀 다음 단계

이 가이드를 완료한 후 다음 가이드들을 학습해보세요:

- [3-5: AI 에이전트 간의 갈등 해결](3-5-conflict-resolution.md) - 협상, 투표, 중재 프로토콜 구현하기
- [3-6: 코더에서 지휘자로](3-6-coder-to-conductor.md) - 에이전틱 시대의 인간 개발자의 역할 재정의
- [3-7: 미래의 핵심 역량](3-7-future-core-skills.md) - 프롬프트 유창성, 제약 조건 설계, 에이전틱 사고 훈련하기

## 📝 요약

이 가이드에서는 에이전트 협업 모델 설계의 핵심 개념을 학습했습니다:

- **계층적 모델**: 명확한 상하 관계와 효율적인 의사결정
- **협력적 모델**: 수평적 관계와 창의적 문제 해결
- **통신 프로토콜**: 효율적인 에이전트 간 의사소통
- **갈등 해결**: 체계적인 갈등 감지 및 해결 메커니즘

다음 가이드에서는 구체적인 갈등 해결 전략을 다룰 예정입니다.

---

**"협업하는 AI, 성공하는 팀"** - 효과적인 에이전트 협업 모델로 디지털 팀의 잠재력을 극대화하세요!
