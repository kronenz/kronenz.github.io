---
layout: default
title: "5-5: 스팟 인스턴스 마스터 - AI 에이전트를 활용한 비용 절감 극대화 전략"
description: "에이전틱 SaaS 조직 가이드"
series: "series-5"
order: 6
---

# 5-5: 스팟 인스턴스 마스터 - AI 에이전트를 활용한 비용 절감 극대화 전략

## 개요

스팟 인스턴스는 클라우드 비용을 최대 90%까지 절감할 수 있는 강력한 도구입니다. 이 가이드에서는 AI 에이전트를 활용하여 스팟 인스턴스를 안전하고 효율적으로 관리하는 고급 전략을 학습합니다.

## 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

1. **스팟 인스턴스 전략 수립**: 다양한 워크로드에 최적화된 스팟 전략 설계
2. **중단 예측 시스템**: AI 기반 스팟 중단 예측 및 대응 시스템 구축
3. **하이브리드 아키텍처**: 스팟과 온디맨드 인스턴스를 조합한 최적 아키텍처
4. **자동 복구 시스템**: 중단 발생 시 자동으로 복구하는 시스템 구현
5. **비용 최적화**: 스팟 인스턴스를 활용한 최대 비용 절감 달성

## 🎯 스팟 인스턴스 전략 설계

### 1. 워크로드별 스팟 전략

```python
class SpotInstanceStrategy:
    def __init__(self):
        self.workload_strategies = {
            'batch_processing': BatchProcessingStrategy(),
            'machine_learning': MachineLearningStrategy(),
            'web_services': WebServicesStrategy(),
            'data_processing': DataProcessingStrategy(),
            'testing': TestingStrategy()
        }
        self.spot_analyzer = SpotInstanceAnalyzer()
        self.cost_calculator = SpotCostCalculator()
    
    def design_spot_strategy(self, workload_profile):
        """워크로드별 스팟 전략 설계"""
        workload_type = workload_profile.get('type', 'general')
        
        # 워크로드 특성 분석
        workload_analysis = self.analyze_workload_characteristics(workload_profile)
        
        # 스팟 적합성 평가
        spot_suitability = self.evaluate_spot_suitability(workload_analysis)
        
        # 전략 선택
        if workload_type in self.workload_strategies:
            strategy = self.workload_strategies[workload_type]
        else:
            strategy = self.workload_strategies['batch_processing']  # 기본 전략
        
        # 맞춤형 전략 생성
        custom_strategy = strategy.create_custom_strategy(workload_analysis, spot_suitability)
        
        return custom_strategy
    
    def analyze_workload_characteristics(self, workload_profile):
        """워크로드 특성 분석"""
        analysis = {
            'interruptibility': self.assess_interruptibility(workload_profile),
            'time_sensitivity': self.assess_time_sensitivity(workload_profile),
            'resource_requirements': self.assess_resource_requirements(workload_profile),
            'cost_sensitivity': self.assess_cost_sensitivity(workload_profile),
            'availability_requirements': self.assess_availability_requirements(workload_profile)
        }
        
        return analysis
    
    def assess_interruptibility(self, workload_profile):
        """중단 가능성 평가"""
        # 워크로드 유형별 중단 가능성
        workload_type = workload_profile.get('type', '')
        
        interruptibility_scores = {
            'batch_processing': 0.9,  # 높음
            'machine_learning': 0.8,  # 높음
            'data_processing': 0.7,   # 중간
            'web_services': 0.3,      # 낮음
            'testing': 0.9,           # 높음
            'development': 0.8        # 높음
        }
        
        base_score = interruptibility_scores.get(workload_type, 0.5)
        
        # 추가 특성 고려
        if workload_profile.get('checkpointing_enabled', False):
            base_score += 0.2
        
        if workload_profile.get('stateless', False):
            base_score += 0.1
        
        if workload_profile.get('can_restart', False):
            base_score += 0.1
        
        return min(1.0, base_score)
    
    def evaluate_spot_suitability(self, workload_analysis):
        """스팟 적합성 평가"""
        # 중단 가능성이 높을수록 적합
        interruptibility = workload_analysis['interruptibility']
        
        # 시간 민감도가 낮을수록 적합
        time_sensitivity = workload_analysis['time_sensitivity']
        time_tolerance = 1 - time_sensitivity
        
        # 비용 민감도가 높을수록 적합
        cost_sensitivity = workload_analysis['cost_sensitivity']
        
        # 가용성 요구사항이 낮을수록 적합
        availability_requirements = workload_analysis['availability_requirements']
        availability_tolerance = 1 - availability_requirements
        
        # 종합 적합성 점수
        suitability_score = (
            interruptibility * 0.4 +
            time_tolerance * 0.2 +
            cost_sensitivity * 0.2 +
            availability_tolerance * 0.2
        )
        
        return {
            'score': suitability_score,
            'level': self.get_suitability_level(suitability_score),
            'recommendations': self.generate_suitability_recommendations(suitability_score, workload_analysis)
        }
    
    def get_suitability_level(self, score):
        """적합성 수준 결정"""
        if score >= 0.8:
            return 'excellent'
        elif score >= 0.6:
            return 'good'
        elif score >= 0.4:
            return 'fair'
        else:
            return 'poor'

class BatchProcessingStrategy:
    def __init__(self):
        self.spot_optimization = SpotOptimization()
        self.checkpointing = CheckpointingManager()
        self.job_scheduler = JobScheduler()
    
    def create_custom_strategy(self, workload_analysis, spot_suitability):
        """배치 처리용 맞춤 전략"""
        strategy = {
            'strategy_type': 'batch_processing',
            'spot_allocation': self.calculate_spot_allocation(workload_analysis),
            'instance_diversity': self.design_instance_diversity(),
            'checkpointing_strategy': self.design_checkpointing_strategy(workload_analysis),
            'job_scheduling': self.design_job_scheduling(workload_analysis),
            'fallback_strategy': self.design_fallback_strategy(workload_analysis),
            'cost_optimization': self.design_cost_optimization(workload_analysis)
        }
        
        return strategy
    
    def calculate_spot_allocation(self, workload_analysis):
        """스팟 할당 비율 계산"""
        interruptibility = workload_analysis['interruptibility']
        cost_sensitivity = workload_analysis['cost_sensitivity']
        
        # 중단 가능성과 비용 민감도에 따른 할당 비율
        base_allocation = interruptibility * 0.8 + cost_sensitivity * 0.2
        
        # 최소 50%, 최대 95% 할당
        spot_allocation = max(0.5, min(0.95, base_allocation))
        
        return {
            'spot_percentage': spot_allocation,
            'on_demand_percentage': 1 - spot_allocation,
            'reasoning': f'중단 가능성 {interruptibility:.1%}, 비용 민감도 {cost_sensitivity:.1%} 기반'
        }
    
    def design_instance_diversity(self):
        """인스턴스 다양성 설계"""
        return {
            'instance_types': ['m5.large', 'm5.xlarge', 'm5.2xlarge', 'c5.large', 'c5.xlarge'],
            'availability_zones': ['us-east-1a', 'us-east-1b', 'us-east-1c'],
            'diversity_strategy': 'maximize_diversity',
            'max_instances_per_type': 3,
            'max_instances_per_az': 5
        }
    
    def design_checkpointing_strategy(self, workload_analysis):
        """체크포인팅 전략 설계"""
        checkpointing_frequency = self.calculate_checkpointing_frequency(workload_analysis)
        
        return {
            'enabled': True,
            'frequency': checkpointing_frequency,
            'storage_type': 's3',
            'compression': True,
            'encryption': True,
            'retention_policy': '7_days'
        }
    
    def calculate_checkpointing_frequency(self, workload_analysis):
        """체크포인팅 빈도 계산"""
        # 작업 길이에 반비례
        job_duration = workload_analysis.get('resource_requirements', {}).get('estimated_duration', 3600)
        
        if job_duration < 1800:  # 30분 미만
            return 'every_5_minutes'
        elif job_duration < 7200:  # 2시간 미만
            return 'every_15_minutes'
        else:
            return 'every_30_minutes'

class MachineLearningStrategy:
    def __init__(self):
        self.model_checkpointing = ModelCheckpointingManager()
        self.experiment_tracking = ExperimentTrackingManager()
        self.spot_fleet_manager = SpotFleetManager()
    
    def create_custom_strategy(self, workload_analysis, spot_suitability):
        """머신러닝용 맞춤 전략"""
        strategy = {
            'strategy_type': 'machine_learning',
            'spot_allocation': self.calculate_ml_spot_allocation(workload_analysis),
            'gpu_optimization': self.design_gpu_optimization(workload_analysis),
            'model_checkpointing': self.design_model_checkpointing(workload_analysis),
            'experiment_management': self.design_experiment_management(workload_analysis),
            'data_pipeline': self.design_data_pipeline(workload_analysis),
            'training_strategy': self.design_training_strategy(workload_analysis)
        }
        
        return strategy
    
    def calculate_ml_spot_allocation(self, workload_analysis):
        """ML 워크로드용 스팟 할당"""
        # ML 워크로드는 일반적으로 중단 가능성이 높음
        interruptibility = workload_analysis['interruptibility']
        
        # GPU 인스턴스는 스팟 가격 차이가 크므로 더 높은 할당
        gpu_requirement = workload_analysis.get('resource_requirements', {}).get('gpu_required', False)
        
        if gpu_requirement:
            spot_allocation = min(0.9, interruptibility + 0.2)
        else:
            spot_allocation = min(0.8, interruptibility + 0.1)
        
        return {
            'spot_percentage': spot_allocation,
            'on_demand_percentage': 1 - spot_allocation,
            'gpu_spot_priority': gpu_requirement
        }
    
    def design_gpu_optimization(self, workload_analysis):
        """GPU 최적화 설계"""
        gpu_requirements = workload_analysis.get('resource_requirements', {}).get('gpu_requirements', {})
        
        return {
            'gpu_instance_types': ['p3.2xlarge', 'p3.8xlarge', 'p3.16xlarge', 'g4dn.xlarge', 'g4dn.2xlarge'],
            'gpu_spot_allocation': 0.8,
            'gpu_diversity_strategy': 'maximize_gpu_diversity',
            'gpu_fallback': 'on_demand_gpu_instances'
        }
```

### 2. 스팟 인스턴스 분석 및 예측

```python
class SpotInstanceAnalyzer:
    def __init__(self):
        self.price_analyzer = SpotPriceAnalyzer()
        self.interruption_predictor = InterruptionPredictor()
        self.availability_tracker = AvailabilityTracker()
        self.cost_optimizer = SpotCostOptimizer()
    
    def analyze_spot_opportunities(self, region, instance_types, time_horizon=7):
        """스팟 기회 분석"""
        analysis_results = {}
        
        for instance_type in instance_types:
            # 가격 분석
            price_analysis = self.price_analyzer.analyze_prices(region, instance_type, time_horizon)
            
            # 중단 예측
            interruption_prediction = self.interruption_predictor.predict_interruptions(
                region, instance_type, time_horizon
            )
            
            # 가용성 분석
            availability_analysis = self.availability_tracker.analyze_availability(
                region, instance_type, time_horizon
            )
            
            # 비용 절감 계산
            cost_savings = self.calculate_cost_savings(price_analysis, instance_type)
            
            # 종합 점수 계산
            overall_score = self.calculate_overall_score(
                price_analysis, interruption_prediction, availability_analysis, cost_savings
            )
            
            analysis_results[instance_type] = {
                'price_analysis': price_analysis,
                'interruption_prediction': interruption_prediction,
                'availability_analysis': availability_analysis,
                'cost_savings': cost_savings,
                'overall_score': overall_score,
                'recommendation': self.generate_recommendation(overall_score)
            }
        
        return analysis_results
    
    def calculate_cost_savings(self, price_analysis, instance_type):
        """비용 절감 계산"""
        on_demand_price = self.get_on_demand_price(instance_type)
        spot_price = price_analysis.get('average_price', 0)
        
        if on_demand_price > 0:
            savings_percentage = (on_demand_price - spot_price) / on_demand_price
            savings_amount = on_demand_price - spot_price
            
            return {
                'savings_percentage': savings_percentage,
                'savings_amount': savings_amount,
                'on_demand_price': on_demand_price,
                'spot_price': spot_price
            }
        
        return {'savings_percentage': 0, 'savings_amount': 0}
    
    def calculate_overall_score(self, price_analysis, interruption_prediction, availability_analysis, cost_savings):
        """종합 점수 계산"""
        # 가격 안정성 점수 (가격 변동이 적을수록 높음)
        price_stability = 1 - price_analysis.get('price_volatility', 0)
        
        # 중단 확률 점수 (중단 확률이 낮을수록 높음)
        interruption_score = 1 - interruption_prediction.get('interruption_probability', 0)
        
        # 가용성 점수
        availability_score = availability_analysis.get('availability_rate', 0)
        
        # 비용 절감 점수
        cost_savings_score = min(1.0, cost_savings.get('savings_percentage', 0) / 0.9)  # 90% 절감을 최고점으로
        
        # 가중 평균
        overall_score = (
            price_stability * 0.2 +
            interruption_score * 0.3 +
            availability_score * 0.3 +
            cost_savings_score * 0.2
        )
        
        return overall_score

class InterruptionPredictor:
    def __init__(self):
        self.ml_model = InterruptionPredictionModel()
        self.historical_data = HistoricalDataManager()
        self.pattern_analyzer = PatternAnalyzer()
    
    def predict_interruptions(self, region, instance_type, time_horizon):
        """중단 예측"""
        # 과거 데이터 수집
        historical_data = self.historical_data.get_interruption_history(region, instance_type)
        
        # 패턴 분석
        patterns = self.pattern_analyzer.analyze_interruption_patterns(historical_data)
        
        # ML 모델 예측
        ml_prediction = self.ml_model.predict(historical_data, time_horizon)
        
        # 패턴 기반 예측
        pattern_prediction = self.pattern_based_prediction(patterns, time_horizon)
        
        # 예측 결과 통합
        combined_prediction = self.combine_predictions(ml_prediction, pattern_prediction)
        
        return combined_prediction
    
    def pattern_based_prediction(self, patterns, time_horizon):
        """패턴 기반 예측"""
        # 시간대별 중단 패턴
        hourly_patterns = patterns.get('hourly', {})
        
        # 요일별 중단 패턴
        daily_patterns = patterns.get('daily', {})
        
        # 계절별 중단 패턴
        seasonal_patterns = patterns.get('seasonal', {})
        
        # 예측 생성
        predictions = []
        for i in range(time_horizon * 24):  # 시간 단위로 예측
            hour = i % 24
            day_of_week = (datetime.now().weekday() + i // 24) % 7
            
            # 시간대별 확률
            hourly_prob = hourly_patterns.get(str(hour), 0.1)
            
            # 요일별 확률
            daily_prob = daily_patterns.get(str(day_of_week), 0.1)
            
            # 계절별 확률 (간단화)
            seasonal_prob = seasonal_patterns.get('current', 0.1)
            
            # 종합 확률
            combined_prob = (hourly_prob + daily_prob + seasonal_prob) / 3
            
            predictions.append({
                'timestamp': datetime.now() + timedelta(hours=i),
                'interruption_probability': combined_prob,
                'confidence': self.calculate_confidence(hourly_prob, daily_prob, seasonal_prob)
            })
        
        return {
            'predictions': predictions,
            'average_probability': sum(p['interruption_probability'] for p in predictions) / len(predictions),
            'max_probability': max(p['interruption_probability'] for p in predictions),
            'patterns_used': list(patterns.keys())
        }
    
    def combine_predictions(self, ml_prediction, pattern_prediction):
        """예측 결과 통합"""
        # 가중 평균으로 통합
        ml_weight = 0.7
        pattern_weight = 0.3
        
        combined_predictions = []
        for ml_pred, pattern_pred in zip(ml_prediction['predictions'], pattern_prediction['predictions']):
            combined_prob = (
                ml_pred['interruption_probability'] * ml_weight +
                pattern_pred['interruption_probability'] * pattern_weight
            )
            
            combined_confidence = (
                ml_pred.get('confidence', 0.5) * ml_weight +
                pattern_pred.get('confidence', 0.5) * pattern_weight
            )
            
            combined_predictions.append({
                'timestamp': ml_pred['timestamp'],
                'interruption_probability': combined_prob,
                'confidence': combined_confidence,
                'ml_probability': ml_pred['interruption_probability'],
                'pattern_probability': pattern_pred['interruption_probability']
            })
        
        return {
            'predictions': combined_predictions,
            'average_probability': sum(p['interruption_probability'] for p in combined_predictions) / len(combined_predictions),
            'max_probability': max(p['interruption_probability'] for p in combined_predictions),
            'method': 'combined_ml_pattern'
        }
```

## 🔄 하이브리드 아키텍처 설계

### 1. 스팟-온디맨드 조합 전략

```python
class HybridArchitectureDesigner:
    def __init__(self):
        self.workload_analyzer = WorkloadAnalyzer()
        self.cost_optimizer = HybridCostOptimizer()
        self.availability_engineer = AvailabilityEngineer()
        self.load_balancer = LoadBalancer()
    
    def design_hybrid_architecture(self, workload_requirements):
        """하이브리드 아키텍처 설계"""
        # 워크로드 분석
        workload_analysis = self.workload_analyzer.analyze(workload_requirements)
        
        # 아키텍처 구성 요소 설계
        architecture_components = {
            'core_services': self.design_core_services(workload_analysis),
            'batch_processing': self.design_batch_processing(workload_analysis),
            'data_processing': self.design_data_processing(workload_analysis),
            'ml_training': self.design_ml_training(workload_analysis),
            'monitoring': self.design_monitoring(workload_analysis)
        }
        
        # 로드 밸런싱 전략
        load_balancing_strategy = self.design_load_balancing(architecture_components)
        
        # 비용 최적화
        cost_optimization = self.cost_optimizer.optimize_hybrid_costs(architecture_components)
        
        # 가용성 보장
        availability_strategy = self.availability_engineer.design_availability_strategy(
            architecture_components
        )
        
        return {
            'architecture_components': architecture_components,
            'load_balancing_strategy': load_balancing_strategy,
            'cost_optimization': cost_optimization,
            'availability_strategy': availability_strategy,
            'implementation_plan': self.create_implementation_plan(architecture_components)
        }
    
    def design_core_services(self, workload_analysis):
        """핵심 서비스 설계"""
        # 핵심 서비스는 온디맨드 인스턴스 사용
        return {
            'instance_type': 'on_demand',
            'instance_family': 'm5',
            'min_capacity': 2,
            'max_capacity': 10,
            'auto_scaling': True,
            'multi_az': True,
            'health_checks': True,
            'reasoning': '핵심 서비스는 높은 가용성이 필요하므로 온디맨드 사용'
        }
    
    def design_batch_processing(self, workload_analysis):
        """배치 처리 설계"""
        # 배치 처리는 스팟 인스턴스 우선 사용
        return {
            'instance_type': 'spot_primary',
            'spot_allocation': 0.8,
            'on_demand_fallback': 0.2,
            'instance_families': ['m5', 'c5', 'r5'],
            'diversity_strategy': 'maximize_diversity',
            'checkpointing': True,
            'job_restart': True,
            'reasoning': '배치 처리는 중단 가능하므로 스팟 인스턴스로 비용 절감'
        }
    
    def design_ml_training(self, workload_analysis):
        """ML 훈련 설계"""
        # ML 훈련은 GPU 스팟 인스턴스 사용
        return {
            'instance_type': 'spot_gpu',
            'spot_allocation': 0.9,
            'on_demand_fallback': 0.1,
            'gpu_instance_types': ['p3', 'p4', 'g4dn'],
            'model_checkpointing': True,
            'experiment_tracking': True,
            'distributed_training': True,
            'reasoning': 'ML 훈련은 체크포인팅이 가능하므로 GPU 스팟으로 최대 비용 절감'
        }
    
    def design_load_balancing(self, architecture_components):
        """로드 밸런싱 전략 설계"""
        return {
            'strategy': 'weighted_round_robin',
            'health_check_interval': 30,
            'unhealthy_threshold': 2,
            'healthy_threshold': 2,
            'spot_instance_weight': 0.7,
            'on_demand_weight': 1.0,
            'failover_strategy': 'automatic',
            'session_affinity': False
        }

class HybridCostOptimizer:
    def __init__(self):
        self.cost_calculator = CostCalculator()
        self.spot_manager = SpotInstanceManager()
        self.on_demand_manager = OnDemandInstanceManager()
    
    def optimize_hybrid_costs(self, architecture_components):
        """하이브리드 비용 최적화"""
        optimization_results = {}
        
        for component_name, component_config in architecture_components.items():
            if component_config.get('instance_type') == 'spot_primary':
                optimization = self.optimize_spot_component(component_config)
            elif component_config.get('instance_type') == 'on_demand':
                optimization = self.optimize_on_demand_component(component_config)
            else:
                optimization = self.optimize_hybrid_component(component_config)
            
            optimization_results[component_name] = optimization
        
        # 전체 비용 최적화
        total_optimization = self.optimize_total_costs(optimization_results)
        
        return {
            'component_optimizations': optimization_results,
            'total_optimization': total_optimization,
            'cost_savings': self.calculate_total_savings(optimization_results)
        }
    
    def optimize_spot_component(self, component_config):
        """스팟 컴포넌트 최적화"""
        spot_allocation = component_config.get('spot_allocation', 0.8)
        instance_families = component_config.get('instance_families', ['m5'])
        
        # 최적 인스턴스 타입 선택
        optimal_types = self.select_optimal_spot_types(instance_families)
        
        # 가격 기반 최적화
        price_optimization = self.optimize_spot_prices(optimal_types)
        
        # 가용성 기반 최적화
        availability_optimization = self.optimize_spot_availability(optimal_types)
        
        return {
            'optimal_instance_types': optimal_types,
            'price_optimization': price_optimization,
            'availability_optimization': availability_optimization,
            'expected_savings': self.calculate_spot_savings(optimal_types)
        }
    
    def select_optimal_spot_types(self, instance_families):
        """최적 스팟 타입 선택"""
        optimal_types = []
        
        for family in instance_families:
            # 가족별 다양한 크기 테스트
            sizes = ['large', 'xlarge', '2xlarge', '4xlarge']
            
            for size in sizes:
                instance_type = f"{family}.{size}"
                
                # 가격, 가용성, 성능 종합 평가
                score = self.evaluate_spot_instance(instance_type)
                
                if score > 0.7:  # 임계값 이상
                    optimal_types.append({
                        'instance_type': instance_type,
                        'score': score,
                        'price': self.get_spot_price(instance_type),
                        'availability': self.get_spot_availability(instance_type)
                    })
        
        # 점수 순으로 정렬
        optimal_types.sort(key=lambda x: x['score'], reverse=True)
        
        return optimal_types[:5]  # 상위 5개 반환
```

### 2. 자동 복구 시스템

```python
class SpotRecoverySystem:
    def __init__(self):
        self.interruption_detector = InterruptionDetector()
        self.job_manager = JobManager()
        self.checkpoint_manager = CheckpointManager()
        self.fallback_manager = FallbackManager()
        self.notification_system = NotificationSystem()
    
    def handle_spot_interruption(self, interrupted_instance, job_context):
        """스팟 중단 처리"""
        # 중단 감지
        interruption_event = self.interruption_detector.detect_interruption(interrupted_instance)
        
        # 작업 상태 저장
        job_state = self.job_manager.save_job_state(job_context)
        
        # 체크포인트 저장
        checkpoint = self.checkpoint_manager.create_checkpoint(job_context)
        
        # 대체 인스턴스 요청
        replacement_instance = self.request_replacement_instance(interrupted_instance, job_context)
        
        # 작업 재시작
        restart_result = self.restart_job_on_replacement(job_state, checkpoint, replacement_instance)
        
        # 알림 전송
        self.notification_system.send_interruption_notification(
            interruption_event, restart_result
        )
        
        return {
            'interruption_event': interruption_event,
            'job_state': job_state,
            'checkpoint': checkpoint,
            'replacement_instance': replacement_instance,
            'restart_result': restart_result
        }
    
    def request_replacement_instance(self, interrupted_instance, job_context):
        """대체 인스턴스 요청"""
        # 원본 인스턴스 정보
        original_type = interrupted_instance.get('instance_type')
        original_az = interrupted_instance.get('availability_zone')
        
        # 대체 전략 결정
        replacement_strategy = self.determine_replacement_strategy(job_context)
        
        if replacement_strategy == 'spot_retry':
            # 다른 AZ에서 스팟 인스턴스 재시도
            replacement = self.request_spot_instance(original_type, exclude_az=original_az)
        elif replacement_strategy == 'on_demand_fallback':
            # 온디맨드 인스턴스로 폴백
            replacement = self.request_on_demand_instance(original_type)
        elif replacement_strategy == 'different_type':
            # 다른 인스턴스 타입으로 변경
            alternative_type = self.find_alternative_instance_type(original_type)
            replacement = self.request_spot_instance(alternative_type)
        else:
            # 기본 전략: 스팟 재시도
            replacement = self.request_spot_instance(original_type)
        
        return replacement
    
    def determine_replacement_strategy(self, job_context):
        """대체 전략 결정"""
        # 작업 우선순위 확인
        priority = job_context.get('priority', 'normal')
        
        # 작업 진행률 확인
        progress = job_context.get('progress', 0)
        
        # 시간 제약 확인
        time_constraint = job_context.get('time_constraint', 'flexible')
        
        # 전략 결정 로직
        if priority == 'high' or time_constraint == 'strict':
            return 'on_demand_fallback'
        elif progress > 0.8:  # 80% 이상 완료
            return 'on_demand_fallback'
        elif progress < 0.2:  # 20% 미만 완료
            return 'different_type'
        else:
            return 'spot_retry'
    
    def restart_job_on_replacement(self, job_state, checkpoint, replacement_instance):
        """대체 인스턴스에서 작업 재시작"""
        try:
            # 작업 상태 복원
            restored_job = self.job_manager.restore_job_state(job_state, replacement_instance)
            
            # 체크포인트에서 재시작
            restart_point = self.checkpoint_manager.get_restart_point(checkpoint)
            
            # 작업 재시작
            restart_result = self.job_manager.restart_job(
                restored_job, 
                restart_point, 
                replacement_instance
            )
            
            return {
                'status': 'success',
                'restart_point': restart_point,
                'restart_time': datetime.now(),
                'replacement_instance': replacement_instance,
                'estimated_completion': self.estimate_completion_time(restart_result)
            }
            
        except Exception as e:
            return {
                'status': 'failed',
                'error': str(e),
                'fallback_required': True
            }
    
    def estimate_completion_time(self, restart_result):
        """완료 시간 추정"""
        # 작업 진행률
        progress = restart_result.get('progress', 0)
        
        # 남은 작업량
        remaining_work = 1 - progress
        
        # 현재 처리 속도
        processing_rate = restart_result.get('processing_rate', 1)
        
        # 예상 완료 시간
        estimated_time = remaining_work / processing_rate if processing_rate > 0 else 0
        
        return datetime.now() + timedelta(seconds=estimated_time)
```

## 📊 스팟 인스턴스 모니터링

### 1. 실시간 모니터링 시스템

```python
class SpotInstanceMonitor:
    def __init__(self):
        self.metrics_collector = SpotMetricsCollector()
        self.alert_manager = SpotAlertManager()
        self.dashboard_creator = SpotDashboardCreator()
        self.cost_tracker = SpotCostTracker()
    
    def monitor_spot_instances(self, spot_instances):
        """스팟 인스턴스 모니터링"""
        monitoring_results = {}
        
        for instance in spot_instances:
            instance_id = instance.get('id')
            
            # 실시간 메트릭 수집
            metrics = self.metrics_collector.collect_instance_metrics(instance)
            
            # 중단 위험 평가
            interruption_risk = self.assess_interruption_risk(instance, metrics)
            
            # 비용 추적
            cost_info = self.cost_tracker.track_instance_costs(instance)
            
            # 알림 생성
            alerts = self.alert_manager.generate_alerts(instance, metrics, interruption_risk)
            
            monitoring_results[instance_id] = {
                'metrics': metrics,
                'interruption_risk': interruption_risk,
                'cost_info': cost_info,
                'alerts': alerts,
                'last_updated': datetime.now()
            }
        
        return monitoring_results
    
    def assess_interruption_risk(self, instance, metrics):
        """중단 위험 평가"""
        # 가격 변동성
        price_volatility = metrics.get('price_volatility', 0)
        
        # 가용성 추세
        availability_trend = metrics.get('availability_trend', 0)
        
        # 인스턴스 연령
        instance_age = metrics.get('instance_age_hours', 0)
        
        # 리전별 중단 패턴
        region_pattern = metrics.get('region_interruption_rate', 0)
        
        # 위험 점수 계산
        risk_score = (
            price_volatility * 0.3 +
            (1 - availability_trend) * 0.3 +
            min(instance_age / 24, 1) * 0.2 +  # 24시간 이상이면 최대 위험
            region_pattern * 0.2
        )
        
        # 위험 수준 결정
        if risk_score > 0.8:
            risk_level = 'high'
        elif risk_score > 0.5:
            risk_level = 'medium'
        else:
            risk_level = 'low'
        
        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'factors': {
                'price_volatility': price_volatility,
                'availability_trend': availability_trend,
                'instance_age': instance_age,
                'region_pattern': region_pattern
            },
            'recommendations': self.generate_risk_recommendations(risk_level, risk_score)
        }
    
    def generate_risk_recommendations(self, risk_level, risk_score):
        """위험 기반 권장사항 생성"""
        recommendations = []
        
        if risk_level == 'high':
            recommendations.extend([
                '즉시 체크포인트 생성',
                '대체 인스턴스 준비',
                '작업 우선순위 재평가',
                '온디맨드 폴백 고려'
            ])
        elif risk_level == 'medium':
            recommendations.extend([
                '정기 체크포인트 확인',
                '대체 인스턴스 모니터링',
                '작업 진행률 확인'
            ])
        else:
            recommendations.extend([
                '정상 모니터링 계속',
                '비용 절감 효과 확인'
            ])
        
        return recommendations

class SpotCostTracker:
    def __init__(self):
        self.price_history = PriceHistoryManager()
        self.usage_tracker = UsageTracker()
        self.savings_calculator = SavingsCalculator()
    
    def track_instance_costs(self, instance):
        """인스턴스 비용 추적"""
        instance_id = instance.get('id')
        instance_type = instance.get('instance_type')
        
        # 현재 가격
        current_price = self.get_current_spot_price(instance_type)
        
        # 사용 시간
        usage_hours = self.usage_tracker.get_usage_hours(instance_id)
        
        # 누적 비용
        total_cost = current_price * usage_hours
        
        # 온디맨드 대비 절약액
        on_demand_price = self.get_on_demand_price(instance_type)
        savings = (on_demand_price - current_price) * usage_hours
        savings_percentage = (savings / (on_demand_price * usage_hours)) * 100 if on_demand_price > 0 else 0
        
        # 가격 변동 추적
        price_history = self.price_history.get_price_history(instance_type, hours=24)
        price_volatility = self.calculate_price_volatility(price_history)
        
        return {
            'instance_id': instance_id,
            'instance_type': instance_type,
            'current_price': current_price,
            'usage_hours': usage_hours,
            'total_cost': total_cost,
            'on_demand_price': on_demand_price,
            'savings': savings,
            'savings_percentage': savings_percentage,
            'price_volatility': price_volatility,
            'cost_efficiency': self.calculate_cost_efficiency(savings_percentage, price_volatility)
        }
    
    def calculate_cost_efficiency(self, savings_percentage, price_volatility):
        """비용 효율성 계산"""
        # 절약률이 높고 가격 변동성이 낮을수록 효율적
        efficiency = savings_percentage * (1 - price_volatility)
        return min(100, max(0, efficiency))
```

## 🎯 다음 단계

이 가이드를 완료한 후 다음 단계를 진행하세요:

1. **[5-6: 자율적 성장 해킹 입문](5-6-autonomous-growth-hacking.md)**: A/B 테스트를 넘어선 새로운 UX 최적화 패러다임
2. **[5-7: 강화 학습(RL)을 이용한 UI/UX 최적화](5-7-rl-ui-ux-optimization.md)**: 기본 개념과 작동 원리
3. **[5-8: RL 에이전트 구축](5-8-rl-agent-construction.md)**: 사용자 행동을 학습하고 UI를 실시간으로 최적화하는 에이전트 만들기

## 📚 추가 리소스

- [스팟 인스턴스 마스터 가이드](https://spot-instance-mastery.dev/)
- [하이브리드 아키텍처 설계](https://hybrid-architecture.dev/)
- [자동 복구 시스템](https://automated-recovery.dev/)
- [클라우드 비용 최적화](https://cloud-cost-optimization.dev/)

---

**"스팟 인스턴스 마스터로 비용 절감 극대화"** - AI 에이전트를 활용하여 스팟 인스턴스를 안전하고 효율적으로 관리하여 최대 90%의 비용 절감을 달성하세요!
