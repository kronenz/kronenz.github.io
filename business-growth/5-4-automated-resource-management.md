---
layout: default
title: "5-4: 자동화된 리소스 관리 - 유휴 리소스 자동 종료 및 인스턴스 스케일링 구현"
description: "에이전틱 SaaS 조직 가이드"
order: 5
---

# 5-4: 자동화된 리소스 관리 - 유휴 리소스 자동 종료 및 인스턴스 스케일링 구현

## 개요

AI 에이전트 팀의 효율적인 운영을 위해서는 지능적인 리소스 관리가 필수입니다. 이 가이드에서는 유휴 리소스를 자동으로 감지하고 종료하며, 수요에 따라 인스턴스를 자동으로 스케일링하는 시스템을 구축하는 방법을 학습합니다.

## 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

1. **유휴 리소스 감지**: AI 기반으로 유휴 리소스를 정확하게 식별하는 시스템
2. **자동 스케일링**: 수요 변화에 따른 자동 인스턴스 스케일링 구현
3. **리소스 최적화**: 비용과 성능을 균형있게 고려한 리소스 최적화
4. **안전장치 구현**: 자동화 과정에서의 안전장치와 롤백 메커니즘
5. **모니터링 시스템**: 리소스 관리 상태를 실시간으로 모니터링하는 시스템

## 🔍 유휴 리소스 감지 시스템

### 1. 지능형 유휴 리소스 식별

```python
class IdleResourceDetector:
    def __init__(self):
        self.detection_strategies = {
            'utilization_based': UtilizationBasedDetector(),
            'activity_based': ActivityBasedDetector(),
            'time_based': TimeBasedDetector(),
            'ml_based': MLBasedDetector()
        }
        self.safety_checks = SafetyCheckEngine()
        self.confidence_calculator = ConfidenceCalculator()
    
    def detect_idle_resources(self, resources, detection_config):
        """유휴 리소스 감지"""
        idle_resources = []
        
        for resource in resources:
            # 다중 전략으로 유휴 상태 확인
            detection_results = self.apply_detection_strategies(resource, detection_config)
            
            # 결과 통합
            combined_result = self.combine_detection_results(detection_results)
            
            # 신뢰도 계산
            confidence = self.confidence_calculator.calculate_confidence(
                detection_results, 
                resource
            )
            
            # 안전성 검사
            safety_check = self.safety_checks.check_resource_safety(resource)
            
            if combined_result['is_idle'] and confidence > 0.8 and safety_check['is_safe']:
                idle_resources.append({
                    'resource': resource,
                    'detection_results': detection_results,
                    'confidence': confidence,
                    'safety_check': safety_check,
                    'recommended_action': self.recommend_action(resource, combined_result)
                })
        
        return idle_resources
    
    def apply_detection_strategies(self, resource, config):
        """감지 전략 적용"""
        results = {}
        
        for strategy_name, detector in self.detection_strategies.items():
            if config.get(f'enable_{strategy_name}', True):
                try:
                    result = detector.detect(resource, config)
                    results[strategy_name] = result
                except Exception as e:
                    results[strategy_name] = {
                        'is_idle': False,
                        'confidence': 0.0,
                        'error': str(e)
                    }
        
        return results
    
    def combine_detection_results(self, detection_results):
        """감지 결과 통합"""
        # 가중 평균으로 통합
        weights = {
            'utilization_based': 0.3,
            'activity_based': 0.3,
            'time_based': 0.2,
            'ml_based': 0.2
        }
        
        total_confidence = 0
        total_weight = 0
        idle_votes = 0
        
        for strategy, result in detection_results.items():
            if 'error' not in result:
                weight = weights.get(strategy, 0.25)
                total_confidence += result.get('confidence', 0) * weight
                total_weight += weight
                
                if result.get('is_idle', False):
                    idle_votes += weight
        
        # 과반수 이상이 유휴로 판단하면 유휴로 분류
        is_idle = idle_votes > (total_weight / 2)
        combined_confidence = total_confidence / total_weight if total_weight > 0 else 0
        
        return {
            'is_idle': is_idle,
            'confidence': combined_confidence,
            'individual_results': detection_results
        }

class UtilizationBasedDetector:
    def __init__(self):
        self.thresholds = {
            'cpu_utilization': 0.1,  # 10% 미만
            'memory_utilization': 0.1,  # 10% 미만
            'network_io': 0.05,  # 5% 미만
            'disk_io': 0.05  # 5% 미만
        }
        self.minimum_duration = 3600  # 1시간 이상 지속
    
    def detect(self, resource, config):
        """사용률 기반 유휴 감지"""
        utilization = resource.get('utilization', {})
        
        # 현재 사용률 확인
        cpu_util = utilization.get('cpu', 0)
        memory_util = utilization.get('memory', 0)
        network_util = utilization.get('network', 0)
        disk_util = utilization.get('disk', 0)
        
        # 임계값 이하 사용률 확인
        low_cpu = cpu_util < self.thresholds['cpu_utilization']
        low_memory = memory_util < self.thresholds['memory_utilization']
        low_network = network_util < self.thresholds['network_io']
        low_disk = disk_util < self.thresholds['disk_io']
        
        # 지속 시간 확인
        duration = self.calculate_low_utilization_duration(resource)
        sufficient_duration = duration >= self.minimum_duration
        
        # 유휴 상태 판단
        is_idle = (low_cpu and low_memory and low_network and low_disk) and sufficient_duration
        
        # 신뢰도 계산
        confidence = self.calculate_confidence(
            cpu_util, memory_util, network_util, disk_util, duration
        )
        
        return {
            'is_idle': is_idle,
            'confidence': confidence,
            'utilization_metrics': {
                'cpu': cpu_util,
                'memory': memory_util,
                'network': network_util,
                'disk': disk_util
            },
            'duration': duration,
            'thresholds': self.thresholds
        }
    
    def calculate_confidence(self, cpu, memory, network, disk, duration):
        """신뢰도 계산"""
        # 사용률이 낮을수록 높은 신뢰도
        utilization_score = (
            (1 - cpu) * 0.3 +
            (1 - memory) * 0.3 +
            (1 - network) * 0.2 +
            (1 - disk) * 0.2
        )
        
        # 지속 시간이 길수록 높은 신뢰도
        duration_score = min(1.0, duration / (self.minimum_duration * 2))
        
        # 종합 신뢰도
        confidence = (utilization_score * 0.7 + duration_score * 0.3)
        
        return min(1.0, max(0.0, confidence))

class ActivityBasedDetector:
    def __init__(self):
        self.activity_indicators = {
            'user_logins': 0,
            'api_calls': 0,
            'database_queries': 0,
            'file_operations': 0,
            'process_activity': 0
        }
        self.activity_thresholds = {
            'min_activity_score': 0.1,
            'min_duration': 1800  # 30분
        }
    
    def detect(self, resource, config):
        """활동 기반 유휴 감지"""
        activity_data = resource.get('activity', {})
        
        # 활동 점수 계산
        activity_score = self.calculate_activity_score(activity_data)
        
        # 지속 시간 확인
        low_activity_duration = self.calculate_low_activity_duration(resource)
        
        # 유휴 상태 판단
        is_idle = (
            activity_score < self.activity_thresholds['min_activity_score'] and
            low_activity_duration >= self.activity_thresholds['min_duration']
        )
        
        # 신뢰도 계산
        confidence = self.calculate_activity_confidence(activity_score, low_activity_duration)
        
        return {
            'is_idle': is_idle,
            'confidence': confidence,
            'activity_score': activity_score,
            'low_activity_duration': low_activity_duration,
            'activity_breakdown': activity_data
        }
    
    def calculate_activity_score(self, activity_data):
        """활동 점수 계산"""
        total_score = 0
        total_weight = 0
        
        for indicator, weight in self.activity_indicators.items():
            value = activity_data.get(indicator, 0)
            normalized_value = self.normalize_activity_value(indicator, value)
            total_score += normalized_value * weight
            total_weight += weight
        
        return total_score / total_weight if total_weight > 0 else 0
    
    def normalize_activity_value(self, indicator, value):
        """활동 값 정규화"""
        # 지수적 감소 함수 적용
        return 1 - math.exp(-value / 10)

class MLBasedDetector:
    def __init__(self):
        self.model = IdleResourceMLModel()
        self.feature_extractor = FeatureExtractor()
        self.model_training = ModelTraining()
    
    def detect(self, resource, config):
        """ML 기반 유휴 감지"""
        # 특성 추출
        features = self.feature_extractor.extract_features(resource)
        
        # 모델 예측
        prediction = self.model.predict(features)
        
        # 결과 해석
        is_idle = prediction['is_idle'] > 0.5
        confidence = prediction['confidence']
        
        return {
            'is_idle': is_idle,
            'confidence': confidence,
            'prediction_details': prediction,
            'features_used': features
        }
    
    def train_model(self, training_data):
        """모델 훈련"""
        # 특성 추출
        features = []
        labels = []
        
        for data_point in training_data:
            features.append(self.feature_extractor.extract_features(data_point['resource']))
            labels.append(data_point['is_idle'])
        
        # 모델 훈련
        self.model.train(features, labels)
        
        # 성능 평가
        performance = self.model.evaluate(features, labels)
        
        return performance
```

### 2. 안전장치 시스템

```python
class SafetyCheckEngine:
    def __init__(self):
        self.safety_rules = {
            'critical_workloads': self.check_critical_workloads,
            'dependencies': self.check_dependencies,
            'backup_status': self.check_backup_status,
            'business_hours': self.check_business_hours,
            'approval_required': self.check_approval_required
        }
        self.risk_assessor = RiskAssessor()
    
    def check_resource_safety(self, resource):
        """리소스 안전성 검사"""
        safety_results = {}
        
        for rule_name, rule_function in self.safety_rules.items():
            try:
                result = rule_function(resource)
                safety_results[rule_name] = result
            except Exception as e:
                safety_results[rule_name] = {
                    'passed': False,
                    'error': str(e),
                    'risk_level': 'high'
                }
        
        # 종합 안전성 평가
        overall_safety = self.assess_overall_safety(safety_results)
        
        return {
            'is_safe': overall_safety['is_safe'],
            'risk_level': overall_safety['risk_level'],
            'individual_checks': safety_results,
            'recommendations': overall_safety['recommendations']
        }
    
    def check_critical_workloads(self, resource):
        """중요 워크로드 확인"""
        workload_type = resource.get('workload_type', '')
        critical_types = ['production', 'database', 'load_balancer', 'monitoring']
        
        is_critical = workload_type in critical_types
        
        return {
            'passed': not is_critical,
            'is_critical': is_critical,
            'workload_type': workload_type,
            'risk_level': 'high' if is_critical else 'low'
        }
    
    def check_dependencies(self, resource):
        """의존성 확인"""
        dependencies = resource.get('dependencies', [])
        dependent_resources = resource.get('dependent_resources', [])
        
        # 종료 시 영향을 받는 리소스 확인
        affected_resources = self.find_affected_resources(resource)
        
        has_dependencies = len(affected_resources) > 0
        
        return {
            'passed': not has_dependencies,
            'has_dependencies': has_dependencies,
            'affected_resources': affected_resources,
            'risk_level': 'high' if has_dependencies else 'low'
        }
    
    def check_backup_status(self, resource):
        """백업 상태 확인"""
        backup_info = resource.get('backup', {})
        
        has_recent_backup = backup_info.get('last_backup_age', float('inf')) < 24  # 24시간 이내
        backup_verification = backup_info.get('verification_status', 'unknown')
        
        backup_safe = has_recent_backup and backup_verification == 'verified'
        
        return {
            'passed': backup_safe,
            'has_recent_backup': has_recent_backup,
            'backup_verification': backup_verification,
            'risk_level': 'high' if not backup_safe else 'low'
        }
    
    def check_business_hours(self, resource):
        """업무 시간 확인"""
        current_time = datetime.now()
        current_hour = current_time.hour
        current_weekday = current_time.weekday()
        
        # 업무 시간: 월-금 9-18시
        is_business_hours = (
            current_weekday < 5 and  # 월-금
            9 <= current_hour < 18   # 9-18시
        )
        
        # 업무 시간에는 더 엄격한 검사
        risk_level = 'high' if is_business_hours else 'medium'
        
        return {
            'passed': not is_business_hours,
            'is_business_hours': is_business_hours,
            'current_time': current_time,
            'risk_level': risk_level
        }
    
    def assess_overall_safety(self, safety_results):
        """종합 안전성 평가"""
        high_risk_count = sum(
            1 for result in safety_results.values()
            if result.get('risk_level') == 'high'
        )
        
        failed_checks = sum(
            1 for result in safety_results.values()
            if not result.get('passed', True)
        )
        
        # 안전성 판단
        is_safe = high_risk_count == 0 and failed_checks == 0
        
        # 위험 수준 결정
        if high_risk_count > 0:
            risk_level = 'high'
        elif failed_checks > 0:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        # 권장사항 생성
        recommendations = self.generate_safety_recommendations(safety_results)
        
        return {
            'is_safe': is_safe,
            'risk_level': risk_level,
            'high_risk_count': high_risk_count,
            'failed_checks': failed_checks,
            'recommendations': recommendations
        }
```

## ⚖️ 자동 스케일링 시스템

### 1. 지능형 스케일링 엔진

```python
class IntelligentScalingEngine:
    def __init__(self):
        self.scaling_strategies = {
            'horizontal': HorizontalScalingStrategy(),
            'vertical': VerticalScalingStrategy(),
            'predictive': PredictiveScalingStrategy(),
            'reactive': ReactiveScalingStrategy()
        }
        self.metrics_analyzer = MetricsAnalyzer()
        self.scaling_optimizer = ScalingOptimizer()
        self.safety_controller = ScalingSafetyController()
    
    def scale_resources(self, scaling_request):
        """리소스 스케일링 실행"""
        # 현재 상태 분석
        current_state = self.analyze_current_state(scaling_request)
        
        # 스케일링 전략 선택
        scaling_strategy = self.select_scaling_strategy(scaling_request, current_state)
        
        # 스케일링 계획 수립
        scaling_plan = self.create_scaling_plan(scaling_strategy, current_state)
        
        # 안전성 검증
        safety_check = self.safety_controller.validate_scaling_plan(scaling_plan)
        
        if not safety_check['is_safe']:
            return {
                'status': 'rejected',
                'reason': 'safety_check_failed',
                'safety_issues': safety_check['issues']
            }
        
        # 스케일링 실행
        execution_result = self.execute_scaling_plan(scaling_plan)
        
        # 결과 모니터링
        monitoring_result = self.monitor_scaling_result(execution_result)
        
        return {
            'status': 'completed',
            'scaling_plan': scaling_plan,
            'execution_result': execution_result,
            'monitoring_result': monitoring_result
        }
    
    def select_scaling_strategy(self, request, current_state):
        """스케일링 전략 선택"""
        strategy_config = {
            'scaling_type': request.get('scaling_type', 'auto'),
            'target_metrics': request.get('target_metrics', ['cpu', 'memory']),
            'scaling_policy': request.get('scaling_policy', 'balanced'),
            'time_constraints': request.get('time_constraints', {})
        }
        
        # 전략별 적합성 평가
        strategy_scores = {}
        
        for strategy_name, strategy in self.scaling_strategies.items():
            score = strategy.evaluate_fitness(strategy_config, current_state)
            strategy_scores[strategy_name] = score
        
        # 최적 전략 선택
        best_strategy = max(strategy_scores.items(), key=lambda x: x[1])
        
        return {
            'strategy_name': best_strategy[0],
            'strategy': self.scaling_strategies[best_strategy[0]],
            'score': best_strategy[1],
            'all_scores': strategy_scores
        }
    
    def create_scaling_plan(self, scaling_strategy, current_state):
        """스케일링 계획 수립"""
        strategy = scaling_strategy['strategy']
        
        # 스케일링 목표 설정
        scaling_targets = strategy.calculate_scaling_targets(current_state)
        
        # 실행 단계 계획
        execution_steps = strategy.plan_execution_steps(scaling_targets, current_state)
        
        # 롤백 계획
        rollback_plan = strategy.create_rollback_plan(execution_steps)
        
        # 모니터링 계획
        monitoring_plan = strategy.create_monitoring_plan(execution_steps)
        
        return {
            'strategy_name': scaling_strategy['strategy_name'],
            'scaling_targets': scaling_targets,
            'execution_steps': execution_steps,
            'rollback_plan': rollback_plan,
            'monitoring_plan': monitoring_plan,
            'estimated_duration': strategy.estimate_duration(execution_steps),
            'estimated_cost_impact': strategy.estimate_cost_impact(scaling_targets)
        }

class HorizontalScalingStrategy:
    def __init__(self):
        self.scaling_metrics = ['cpu', 'memory', 'request_rate', 'response_time']
        self.scaling_thresholds = {
            'scale_up': 0.8,
            'scale_down': 0.3
        }
        self.scaling_limits = {
            'min_instances': 1,
            'max_instances': 10
        }
    
    def evaluate_fitness(self, config, current_state):
        """전략 적합성 평가"""
        score = 0
        
        # 수평 스케일링 가능 여부
        if self.can_scale_horizontally(current_state):
            score += 0.4
        
        # 현재 인스턴스 수 확인
        current_instances = current_state.get('instance_count', 1)
        if current_instances < self.scaling_limits['max_instances']:
            score += 0.3
        
        # 메트릭 적합성
        target_metrics = config.get('target_metrics', [])
        if any(metric in self.scaling_metrics for metric in target_metrics):
            score += 0.3
        
        return score
    
    def can_scale_horizontally(self, current_state):
        """수평 스케일링 가능 여부 확인"""
        # 로드 밸런서 존재 여부
        has_load_balancer = current_state.get('has_load_balancer', False)
        
        # 상태 비저장 애플리케이션 여부
        is_stateless = current_state.get('is_stateless', False)
        
        # 오토스케일링 그룹 존재 여부
        has_asg = current_state.get('has_auto_scaling_group', False)
        
        return has_load_balancer and is_stateless and has_asg
    
    def calculate_scaling_targets(self, current_state):
        """스케일링 목표 계산"""
        current_instances = current_state.get('instance_count', 1)
        current_metrics = current_state.get('metrics', {})
        
        # 스케일링 방향 결정
        scale_direction = self.determine_scale_direction(current_metrics)
        
        # 목표 인스턴스 수 계산
        if scale_direction == 'up':
            target_instances = min(
                current_instances * 2,  # 2배 증가
                self.scaling_limits['max_instances']
            )
        elif scale_direction == 'down':
            target_instances = max(
                current_instances // 2,  # 절반 감소
                self.scaling_limits['min_instances']
            )
        else:
            target_instances = current_instances
        
        return {
            'target_instances': target_instances,
            'scale_direction': scale_direction,
            'scale_factor': target_instances / current_instances if current_instances > 0 else 1
        }
    
    def determine_scale_direction(self, metrics):
        """스케일링 방향 결정"""
        cpu_util = metrics.get('cpu', 0)
        memory_util = metrics.get('memory', 0)
        request_rate = metrics.get('request_rate', 0)
        
        # 스케일 업 조건
        if (cpu_util > self.scaling_thresholds['scale_up'] or
            memory_util > self.scaling_thresholds['scale_up'] or
            request_rate > self.scaling_thresholds['scale_up']):
            return 'up'
        
        # 스케일 다운 조건
        elif (cpu_util < self.scaling_thresholds['scale_down'] and
              memory_util < self.scaling_thresholds['scale_down'] and
              request_rate < self.scaling_thresholds['scale_down']):
            return 'down'
        
        else:
            return 'none'

class PredictiveScalingStrategy:
    def __init__(self):
        self.forecasting_model = DemandForecastingModel()
        self.pattern_analyzer = PatternAnalyzer()
        self.scaling_predictor = ScalingPredictor()
    
    def evaluate_fitness(self, config, current_state):
        """예측적 스케일링 적합성 평가"""
        score = 0
        
        # 과거 데이터 충분성
        historical_data = current_state.get('historical_data', [])
        if len(historical_data) > 30:  # 30일 이상 데이터
            score += 0.4
        
        # 패턴 존재 여부
        patterns = self.pattern_analyzer.detect_patterns(historical_data)
        if patterns:
            score += 0.3
        
        # 예측 모델 정확도
        model_accuracy = self.forecasting_model.get_accuracy()
        if model_accuracy > 0.8:
            score += 0.3
        
        return score
    
    def calculate_scaling_targets(self, current_state):
        """예측 기반 스케일링 목표 계산"""
        historical_data = current_state.get('historical_data', [])
        forecast_horizon = 60  # 60분 예측
        
        # 수요 예측
        demand_forecast = self.forecasting_model.predict(historical_data, forecast_horizon)
        
        # 현재 용량
        current_capacity = current_state.get('current_capacity', 1)
        
        # 예상 수요에 따른 목표 용량 계산
        peak_demand = max(demand_forecast)
        target_capacity = self.calculate_required_capacity(peak_demand, current_capacity)
        
        return {
            'target_capacity': target_capacity,
            'demand_forecast': demand_forecast,
            'peak_demand': peak_demand,
            'scaling_reason': 'predictive_demand'
        }
    
    def calculate_required_capacity(self, peak_demand, current_capacity):
        """필요 용량 계산"""
        # 여유 용량 20% 포함
        safety_margin = 1.2
        required_capacity = peak_demand * safety_margin
        
        # 현재 용량과 비교하여 스케일링 필요성 판단
        if required_capacity > current_capacity * 1.5:
            return int(required_capacity)
        elif required_capacity < current_capacity * 0.5:
            return max(1, int(required_capacity))
        else:
            return current_capacity
```

### 2. 스케일링 안전성 제어

```python
class ScalingSafetyController:
    def __init__(self):
        self.safety_rules = {
            'gradual_scaling': self.check_gradual_scaling,
            'resource_limits': self.check_resource_limits,
            'dependency_checks': self.check_dependencies,
            'rollback_capability': self.check_rollback_capability
        }
        self.rate_limiter = ScalingRateLimiter()
        self.health_checker = HealthChecker()
    
    def validate_scaling_plan(self, scaling_plan):
        """스케일링 계획 검증"""
        validation_results = {}
        
        for rule_name, rule_function in self.safety_rules.items():
            try:
                result = rule_function(scaling_plan)
                validation_results[rule_name] = result
            except Exception as e:
                validation_results[rule_name] = {
                    'passed': False,
                    'error': str(e)
                }
        
        # 종합 검증 결과
        overall_validation = self.assess_overall_validation(validation_results)
        
        return overall_validation
    
    def check_gradual_scaling(self, scaling_plan):
        """점진적 스케일링 확인"""
        execution_steps = scaling_plan.get('execution_steps', [])
        
        # 스케일링 단계별 크기 변화 확인
        scaling_changes = []
        for step in execution_steps:
            if step.get('action') == 'scale':
                change = step.get('target_count', 0) - step.get('current_count', 0)
                scaling_changes.append(abs(change))
        
        # 급격한 변화 확인 (50% 이상 변화)
        max_change = max(scaling_changes) if scaling_changes else 0
        current_count = execution_steps[0].get('current_count', 1) if execution_steps else 1
        
        is_gradual = max_change <= current_count * 0.5
        
        return {
            'passed': is_gradual,
            'max_change': max_change,
            'current_count': current_count,
            'change_percentage': (max_change / current_count) * 100 if current_count > 0 else 0
        }
    
    def check_resource_limits(self, scaling_plan):
        """리소스 한도 확인"""
        scaling_targets = scaling_plan.get('scaling_targets', {})
        target_instances = scaling_targets.get('target_instances', 1)
        
        # 최대 인스턴스 수 확인
        max_instances = 10  # 설정에서 가져와야 함
        within_limits = target_instances <= max_instances
        
        # 최소 인스턴스 수 확인
        min_instances = 1
        above_minimum = target_instances >= min_instances
        
        return {
            'passed': within_limits and above_minimum,
            'target_instances': target_instances,
            'max_instances': max_instances,
            'min_instances': min_instances,
            'within_max': within_limits,
            'above_min': above_minimum
        }
    
    def check_dependencies(self, scaling_plan):
        """의존성 확인"""
        # 데이터베이스 연결 확인
        db_connections = self.check_database_connections()
        
        # 로드 밸런서 상태 확인
        lb_status = self.check_load_balancer_status()
        
        # 외부 서비스 의존성 확인
        external_deps = self.check_external_dependencies()
        
        all_deps_healthy = db_connections and lb_status and external_deps
        
        return {
            'passed': all_deps_healthy,
            'database_connections': db_connections,
            'load_balancer_status': lb_status,
            'external_dependencies': external_deps
        }
    
    def check_rollback_capability(self, scaling_plan):
        """롤백 가능성 확인"""
        rollback_plan = scaling_plan.get('rollback_plan', {})
        
        # 롤백 계획 존재 여부
        has_rollback_plan = bool(rollback_plan)
        
        # 롤백 실행 가능성
        rollback_executable = self.verify_rollback_executability(rollback_plan)
        
        # 백업 상태 확인
        backup_available = self.check_backup_availability()
        
        return {
            'passed': has_rollback_plan and rollback_executable and backup_available,
            'has_rollback_plan': has_rollback_plan,
            'rollback_executable': rollback_executable,
            'backup_available': backup_available
        }

class ScalingRateLimiter:
    def __init__(self):
        self.rate_limits = {
            'max_scaling_events_per_hour': 5,
            'max_instances_change_per_event': 3,
            'min_time_between_scaling_events': 300  # 5분
        }
        self.scaling_history = []
    
    def check_rate_limits(self, scaling_request):
        """스케일링 요청 속도 제한 확인"""
        current_time = datetime.now()
        
        # 최근 1시간 내 스케일링 이벤트 수 확인
        recent_events = [
            event for event in self.scaling_history
            if (current_time - event['timestamp']).total_seconds() < 3600
        ]
        
        if len(recent_events) >= self.rate_limits['max_scaling_events_per_hour']:
            return {
                'allowed': False,
                'reason': 'rate_limit_exceeded',
                'recent_events': len(recent_events),
                'limit': self.rate_limits['max_scaling_events_per_hour']
            }
        
        # 인스턴스 수 변화량 확인
        instance_change = abs(scaling_request.get('target_instances', 0) - 
                             scaling_request.get('current_instances', 0))
        
        if instance_change > self.rate_limits['max_instances_change_per_event']:
            return {
                'allowed': False,
                'reason': 'instance_change_too_large',
                'instance_change': instance_change,
                'limit': self.rate_limits['max_instances_change_per_event']
            }
        
        # 마지막 스케일링 이벤트와의 시간 간격 확인
        if self.scaling_history:
            last_event = max(self.scaling_history, key=lambda x: x['timestamp'])
            time_since_last = (current_time - last_event['timestamp']).total_seconds()
            
            if time_since_last < self.rate_limits['min_time_between_scaling_events']:
                return {
                    'allowed': False,
                    'reason': 'insufficient_time_since_last_scaling',
                    'time_since_last': time_since_last,
                    'required_interval': self.rate_limits['min_time_between_scaling_events']
                }
        
        return {'allowed': True}
    
    def record_scaling_event(self, scaling_request, result):
        """스케일링 이벤트 기록"""
        event = {
            'timestamp': datetime.now(),
            'request': scaling_request,
            'result': result
        }
        self.scaling_history.append(event)
        
        # 오래된 이벤트 제거 (24시간 이상)
        cutoff_time = datetime.now() - timedelta(hours=24)
        self.scaling_history = [
            event for event in self.scaling_history
            if event['timestamp'] > cutoff_time
        ]
```

## 📊 리소스 관리 모니터링

### 1. 실시간 모니터링 대시보드

```python
class ResourceManagementDashboard:
    def __init__(self):
        self.metrics_collector = ResourceMetricsCollector()
        self.visualization_engine = VisualizationEngine()
        self.alert_manager = AlertManager()
        self.report_generator = ReportGenerator()
    
    def create_dashboard(self, dashboard_config):
        """리소스 관리 대시보드 생성"""
        # 메트릭 수집
        metrics = self.metrics_collector.collect_all_metrics()
        
        # 시각화 생성
        visualizations = {
            'resource_utilization': self.create_utilization_chart(metrics),
            'scaling_events': self.create_scaling_events_chart(metrics),
            'cost_trends': self.create_cost_trends_chart(metrics),
            'idle_resources': self.create_idle_resources_chart(metrics),
            'safety_status': self.create_safety_status_chart(metrics)
        }
        
        # 알림 설정
        alerts = self.setup_alerts(metrics)
        
        # 보고서 생성
        report = self.generate_report(metrics)
        
        return {
            'dashboard_id': f"resource_management_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'visualizations': visualizations,
            'alerts': alerts,
            'report': report,
            'last_updated': datetime.now()
        }
    
    def create_utilization_chart(self, metrics):
        """사용률 차트 생성"""
        utilization_data = metrics.get('utilization', {})
        
        return {
            'type': 'multi_line_chart',
            'title': '리소스 사용률',
            'data': {
                'labels': utilization_data.get('timestamps', []),
                'datasets': [
                    {
                        'label': 'CPU 사용률',
                        'data': utilization_data.get('cpu', []),
                        'borderColor': 'rgb(75, 192, 192)',
                        'tension': 0.1
                    },
                    {
                        'label': '메모리 사용률',
                        'data': utilization_data.get('memory', []),
                        'borderColor': 'rgb(255, 99, 132)',
                        'tension': 0.1
                    },
                    {
                        'label': '네트워크 사용률',
                        'data': utilization_data.get('network', []),
                        'borderColor': 'rgb(255, 205, 86)',
                        'tension': 0.1
                    }
                ]
            },
            'options': {
                'scales': {
                    'y': {
                        'beginAtZero': True,
                        'max': 1,
                        'title': {
                            'display': True,
                            'text': '사용률 (%)'
                        }
                    }
                }
            }
        }
    
    def create_scaling_events_chart(self, metrics):
        """스케일링 이벤트 차트 생성"""
        scaling_data = metrics.get('scaling_events', {})
        
        return {
            'type': 'bar_chart',
            'title': '스케일링 이벤트',
            'data': {
                'labels': scaling_data.get('timestamps', []),
                'datasets': [
                    {
                        'label': '인스턴스 수',
                        'data': scaling_data.get('instance_counts', []),
                        'backgroundColor': 'rgba(54, 162, 235, 0.5)',
                        'borderColor': 'rgba(54, 162, 235, 1)',
                        'borderWidth': 1
                    }
                ]
            },
            'options': {
                'scales': {
                    'y': {
                        'beginAtZero': True,
                        'title': {
                            'display': True,
                            'text': '인스턴스 수'
                        }
                    }
                }
            }
        }
    
    def setup_alerts(self, metrics):
        """알림 설정"""
        alerts = []
        
        # 높은 사용률 알림
        current_cpu = metrics.get('current_utilization', {}).get('cpu', 0)
        if current_cpu > 0.9:
            alerts.append({
                'type': 'high_utilization',
                'severity': 'high',
                'message': f'CPU 사용률이 {current_cpu:.1%}에 도달했습니다.',
                'metric': 'cpu',
                'value': current_cpu,
                'threshold': 0.9
            })
        
        # 유휴 리소스 알림
        idle_resources = metrics.get('idle_resources', [])
        if len(idle_resources) > 0:
            alerts.append({
                'type': 'idle_resources',
                'severity': 'medium',
                'message': f'{len(idle_resources)}개의 유휴 리소스가 발견되었습니다.',
                'count': len(idle_resources),
                'resources': idle_resources
            })
        
        # 스케일링 실패 알림
        failed_scaling = metrics.get('failed_scaling_events', [])
        if len(failed_scaling) > 0:
            alerts.append({
                'type': 'scaling_failure',
                'severity': 'high',
                'message': f'{len(failed_scaling)}개의 스케일링 이벤트가 실패했습니다.',
                'count': len(failed_scaling),
                'events': failed_scaling
            })
        
        return alerts
```

## 🎯 다음 단계

이 가이드를 완료한 후 다음 단계를 진행하세요:

1. **[5-5: 스팟 인스턴스 마스터](5-5-spot-instance-mastery.md)**: AI 에이전트를 활용한 비용 절감 극대화 전략
2. **[5-6: 자율적 성장 해킹 입문](5-6-autonomous-growth-hacking.md)**: A/B 테스트를 넘어선 새로운 UX 최적화 패러다임
3. **[5-7: 강화 학습(RL)을 이용한 UI/UX 최적화](5-7-rl-ui-ux-optimization.md)**: 기본 개념과 작동 원리

## 📚 추가 리소스

- [자동화된 리소스 관리](https://automated-resource-management.dev/)
- [지능형 스케일링 시스템](https://intelligent-scaling.dev/)
- [유휴 리소스 감지](https://idle-resource-detection.dev/)
- [클라우드 비용 최적화](https://cloud-cost-optimization.dev/)

---

**"지능형 리소스 관리로 효율성 극대화"** - AI 기반 자동화된 리소스 관리 시스템을 구축하여 비용을 절감하고 성능을 최적화하세요!
