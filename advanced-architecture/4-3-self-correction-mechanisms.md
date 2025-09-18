---
layout: default
title: "4-3: 자가 수정 메커니즘 - 오류 발생 시 스스로 디버깅하고 학습하는 에이전트 만들기"
description: "에이전틱 SaaS 조직 가이드"
order: 3
---

# 4-3: 자가 수정 메커니즘 - 오류 발생 시 스스로 디버깅하고 학습하는 에이전트 만들기

## 개요

Devin의 가장 혁신적인 특징 중 하나는 오류가 발생했을 때 스스로 문제를 진단하고 수정하는 자가 수정 메커니즘입니다. 이 가이드에서는 AI 에이전트가 자율적으로 오류를 감지, 분석, 수정하고 학습하는 시스템을 구현하는 방법을 학습합니다.

## 학습 목표

이 가이드를 완료하면 다음을 달성할 수 있습니다:

1. **오류 감지 시스템 구현**: 다양한 유형의 오류를 자동으로 감지하는 시스템
2. **자가 진단 알고리즘 설계**: 오류의 원인을 분석하고 해결 방안을 찾는 시스템
3. **자동 수정 메커니즘 구축**: 감지된 오류를 자동으로 수정하는 시스템
4. **학습 및 개선 시스템**: 오류 경험을 통해 지속적으로 개선하는 시스템

## 🔍 오류 감지 시스템

### 1. 다층 오류 감지 아키텍처

#### 개념
다양한 레벨에서 오류를 감지하는 계층적 시스템

```python
class ErrorDetectionSystem:
    def __init__(self):
        self.detection_layers = {
            'syntax': SyntaxErrorDetector(),      # 구문 오류
            'semantic': SemanticErrorDetector(),  # 의미 오류
            'runtime': RuntimeErrorDetector(),    # 런타임 오류
            'logical': LogicalErrorDetector(),    # 논리 오류
            'performance': PerformanceErrorDetector(), # 성능 오류
            'security': SecurityErrorDetector()   # 보안 오류
        }
        self.error_classifier = ErrorClassifier()
        self.error_prioritizer = ErrorPrioritizer()
    
    def detect_errors(self, code, context):
        """다층 오류 감지"""
        detected_errors = []
        
        for layer_name, detector in self.detection_layers.items():
            errors = detector.detect(code, context)
            if errors:
                detected_errors.extend(errors)
        
        # 오류 분류 및 우선순위 설정
        classified_errors = self.error_classifier.classify(detected_errors)
        prioritized_errors = self.error_prioritizer.prioritize(classified_errors)
        
        return prioritized_errors

class SyntaxErrorDetector:
    def detect(self, code, context):
        """구문 오류 감지"""
        errors = []
        
        # 파싱 오류 감지
        try:
            ast.parse(code)
        except SyntaxError as e:
            errors.append({
                'type': 'syntax',
                'severity': 'high',
                'message': str(e),
                'line': e.lineno,
                'column': e.offset,
                'suggestion': self.suggest_syntax_fix(e)
            })
        
        # 스타일 오류 감지
        style_errors = self.check_code_style(code)
        errors.extend(style_errors)
        
        return errors
    
    def suggest_syntax_fix(self, error):
        """구문 오류 수정 제안"""
        suggestions = {
            'unexpected_indent': '들여쓰기를 확인하세요',
            'invalid_syntax': '문법을 확인하세요',
            'unexpected_eof': '괄호나 따옴표가 닫혔는지 확인하세요',
            'invalid_character': '특수 문자를 확인하세요'
        }
        
        return suggestions.get(error.msg, '구문을 확인하세요')

class RuntimeErrorDetector:
    def detect(self, code, context):
        """런타임 오류 감지"""
        errors = []
        
        # 실행 전 예측 가능한 런타임 오류 감지
        potential_errors = self.analyze_potential_runtime_errors(code)
        errors.extend(potential_errors)
        
        # 실제 실행 결과 분석
        if context.get('execution_result'):
            execution_errors = self.analyze_execution_result(
                context['execution_result']
            )
            errors.extend(execution_errors)
        
        return errors
    
    def analyze_potential_runtime_errors(self, code):
        """잠재적 런타임 오류 분석"""
        errors = []
        
        # 변수 미정의 오류
        undefined_vars = self.find_undefined_variables(code)
        for var in undefined_vars:
            errors.append({
                'type': 'runtime',
                'subtype': 'undefined_variable',
                'severity': 'high',
                'variable': var,
                'suggestion': f'변수 {var}를 정의하거나 import하세요'
            })
        
        # 타입 오류
        type_errors = self.detect_type_errors(code)
        errors.extend(type_errors)
        
        # 인덱스 오류
        index_errors = self.detect_index_errors(code)
        errors.extend(index_errors)
        
        return errors
```

### 2. 지능형 오류 분류 시스템

```python
class ErrorClassifier:
    def __init__(self):
        self.classification_rules = {
            'critical': self.is_critical_error,
            'high': self.is_high_priority_error,
            'medium': self.is_medium_priority_error,
            'low': self.is_low_priority_error
        }
        self.error_patterns = self.load_error_patterns()
    
    def classify(self, errors):
        """오류 분류"""
        classified_errors = []
        
        for error in errors:
            classification = self.classify_single_error(error)
            error['classification'] = classification
            classified_errors.append(error)
        
        return classified_errors
    
    def classify_single_error(self, error):
        """단일 오류 분류"""
        for priority, rule in self.classification_rules.items():
            if rule(error):
                return {
                    'priority': priority,
                    'category': self.determine_category(error),
                    'fix_complexity': self.assess_fix_complexity(error),
                    'estimated_time': self.estimate_fix_time(error)
                }
        
        return {
            'priority': 'unknown',
            'category': 'unknown',
            'fix_complexity': 'unknown',
            'estimated_time': 0
        }
    
    def is_critical_error(self, error):
        """치명적 오류 판단"""
        critical_indicators = [
            'syntax' in error.get('type', ''),
            'undefined_variable' in error.get('subtype', ''),
            'import' in error.get('message', '').lower(),
            error.get('severity') == 'critical'
        ]
        return any(critical_indicators)
    
    def determine_category(self, error):
        """오류 카테고리 결정"""
        error_type = error.get('type', '')
        
        if error_type == 'syntax':
            return 'language'
        elif error_type == 'runtime':
            return 'execution'
        elif error_type == 'logical':
            return 'algorithm'
        elif error_type == 'performance':
            return 'optimization'
        elif error_type == 'security':
            return 'security'
        else:
            return 'general'
```

## 🔧 자가 진단 시스템

### 1. 오류 원인 분석 엔진

```python
class SelfDiagnosticSystem:
    def __init__(self):
        self.diagnostic_strategies = {
            'static_analysis': StaticAnalysisDiagnostic(),
            'dynamic_analysis': DynamicAnalysisDiagnostic(),
            'pattern_matching': PatternMatchingDiagnostic(),
            'heuristic_analysis': HeuristicAnalysisDiagnostic(),
            'machine_learning': MLBasedDiagnostic()
        }
        self.diagnostic_history = []
        self.learning_system = DiagnosticLearningSystem()
    
    def diagnose_error(self, error, context):
        """오류 진단"""
        # 진단 전략 선택
        strategy = self.select_diagnostic_strategy(error, context)
        
        # 진단 수행
        diagnosis = self.diagnostic_strategies[strategy].diagnose(error, context)
        
        # 진단 결과 검증
        validated_diagnosis = self.validate_diagnosis(diagnosis, error)
        
        # 학습 데이터 저장
        self.learning_system.record_diagnosis(error, diagnosis, context)
        
        return validated_diagnosis
    
    def select_diagnostic_strategy(self, error, context):
        """진단 전략 선택"""
        # 오류 유형에 따른 전략 선택
        error_type = error.get('type', '')
        
        if error_type == 'syntax':
            return 'static_analysis'
        elif error_type == 'runtime':
            return 'dynamic_analysis'
        elif error_type == 'logical':
            return 'heuristic_analysis'
        else:
            return 'pattern_matching'

class StaticAnalysisDiagnostic:
    def diagnose(self, error, context):
        """정적 분석 기반 진단"""
        code = context.get('code', '')
        
        # AST 분석
        ast_analysis = self.analyze_ast(code)
        
        # 데이터 흐름 분석
        data_flow = self.analyze_data_flow(code)
        
        # 제어 흐름 분석
        control_flow = self.analyze_control_flow(code)
        
        # 진단 결과 생성
        diagnosis = {
            'root_cause': self.identify_root_cause(error, ast_analysis, data_flow),
            'contributing_factors': self.find_contributing_factors(error, context),
            'fix_suggestions': self.generate_fix_suggestions(error, ast_analysis),
            'confidence': self.calculate_confidence(ast_analysis, data_flow),
            'alternative_solutions': self.find_alternative_solutions(error, context)
        }
        
        return diagnosis
    
    def identify_root_cause(self, error, ast_analysis, data_flow):
        """근본 원인 식별"""
        error_line = error.get('line', 0)
        
        # 해당 라인 주변의 코드 분석
        surrounding_code = self.get_surrounding_code(error_line, ast_analysis)
        
        # 변수 사용 패턴 분석
        variable_usage = self.analyze_variable_usage(surrounding_code, data_flow)
        
        # 함수 호출 패턴 분석
        function_calls = self.analyze_function_calls(surrounding_code)
        
        # 근본 원인 추론
        root_cause = self.infer_root_cause(
            error, 
            variable_usage, 
            function_calls, 
            surrounding_code
        )
        
        return root_cause

class DynamicAnalysisDiagnostic:
    def diagnose(self, error, context):
        """동적 분석 기반 진단"""
        execution_trace = context.get('execution_trace', [])
        variable_states = context.get('variable_states', {})
        
        # 실행 흐름 분석
        execution_flow = self.analyze_execution_flow(execution_trace)
        
        # 변수 상태 변화 분석
        state_changes = self.analyze_state_changes(variable_states)
        
        # 메모리 사용 패턴 분석
        memory_patterns = self.analyze_memory_patterns(execution_trace)
        
        # 진단 결과 생성
        diagnosis = {
            'execution_path': execution_flow,
            'state_anomalies': self.find_state_anomalies(state_changes),
            'memory_issues': self.identify_memory_issues(memory_patterns),
            'timing_issues': self.analyze_timing_issues(execution_trace),
            'fix_recommendations': self.generate_dynamic_fixes(
                execution_flow, 
                state_changes, 
                memory_patterns
            )
        }
        
        return diagnosis
```

### 2. 지능형 수정 제안 시스템

```python
class FixSuggestionSystem:
    def __init__(self):
        self.fix_templates = self.load_fix_templates()
        self.fix_history = []
        self.success_rates = {}
        self.learning_engine = FixLearningEngine()
    
    def generate_fixes(self, error, diagnosis, context):
        """수정 제안 생성"""
        # 템플릿 기반 수정 제안
        template_fixes = self.generate_template_fixes(error, diagnosis)
        
        # 패턴 기반 수정 제안
        pattern_fixes = self.generate_pattern_fixes(error, diagnosis)
        
        # 학습 기반 수정 제안
        learned_fixes = self.generate_learned_fixes(error, diagnosis, context)
        
        # 모든 수정 제안 통합
        all_fixes = template_fixes + pattern_fixes + learned_fixes
        
        # 수정 제안 순위 매기기
        ranked_fixes = self.rank_fixes(all_fixes, error, context)
        
        return ranked_fixes
    
    def generate_template_fixes(self, error, diagnosis):
        """템플릿 기반 수정 제안"""
        fixes = []
        error_type = error.get('type', '')
        
        if error_type == 'syntax':
            fixes.extend(self.get_syntax_fixes(error))
        elif error_type == 'runtime':
            fixes.extend(self.get_runtime_fixes(error, diagnosis))
        elif error_type == 'logical':
            fixes.extend(self.get_logical_fixes(error, diagnosis))
        
        return fixes
    
    def get_syntax_fixes(self, error):
        """구문 오류 수정 제안"""
        fixes = []
        error_msg = error.get('message', '')
        
        if 'unexpected indent' in error_msg:
            fixes.append({
                'type': 'indentation_fix',
                'description': '들여쓰기 수정',
                'code_change': self.fix_indentation(error),
                'confidence': 0.9
            })
        
        if 'invalid syntax' in error_msg:
            fixes.append({
                'type': 'syntax_fix',
                'description': '구문 오류 수정',
                'code_change': self.fix_syntax(error),
                'confidence': 0.8
            })
        
        return fixes
    
    def rank_fixes(self, fixes, error, context):
        """수정 제안 순위 매기기"""
        scored_fixes = []
        
        for fix in fixes:
            score = self.calculate_fix_score(fix, error, context)
            fix['score'] = score
            scored_fixes.append(fix)
        
        # 점수 순으로 정렬
        scored_fixes.sort(key=lambda x: x['score'], reverse=True)
        
        return scored_fixes
    
    def calculate_fix_score(self, fix, error, context):
        """수정 제안 점수 계산"""
        score = 0
        
        # 신뢰도 점수
        score += fix.get('confidence', 0) * 0.4
        
        # 복잡도 점수 (낮을수록 좋음)
        complexity = fix.get('complexity', 1)
        score += (1 - complexity) * 0.3
        
        # 과거 성공률 점수
        fix_type = fix.get('type', '')
        success_rate = self.success_rates.get(fix_type, 0.5)
        score += success_rate * 0.3
        
        return score
```

## 🛠️ 자동 수정 시스템

### 1. 코드 자동 수정 엔진

```python
class AutoFixEngine:
    def __init__(self):
        self.fix_strategies = {
            'syntax_fix': SyntaxFixer(),
            'runtime_fix': RuntimeFixer(),
            'logical_fix': LogicalFixer(),
            'performance_fix': PerformanceFixer(),
            'security_fix': SecurityFixer()
        }
        self.fix_validator = FixValidator()
        self.fix_tester = FixTester()
    
    def apply_fix(self, error, fix_suggestion, context):
        """수정 적용"""
        # 수정 전 백업
        original_code = context.get('code', '')
        backup = self.create_backup(original_code)
        
        try:
            # 수정 적용
            fixed_code = self.apply_code_fix(original_code, fix_suggestion)
            
            # 수정 검증
            validation_result = self.fix_validator.validate(fixed_code, error)
            
            if validation_result['is_valid']:
                # 수정 테스트
                test_result = self.fix_tester.test_fix(fixed_code, context)
                
                if test_result['passed']:
                    return {
                        'success': True,
                        'fixed_code': fixed_code,
                        'changes': fix_suggestion.get('code_change', {}),
                        'validation': validation_result,
                        'test_result': test_result
                    }
                else:
                    # 테스트 실패 시 롤백
                    return self.rollback_fix(backup, test_result)
            else:
                # 검증 실패 시 롤백
                return self.rollback_fix(backup, validation_result)
        
        except Exception as e:
            # 예외 발생 시 롤백
            return self.rollback_fix(backup, {'error': str(e)})
    
    def apply_code_fix(self, code, fix_suggestion):
        """코드 수정 적용"""
        fix_type = fix_suggestion.get('type', '')
        code_change = fix_suggestion.get('code_change', {})
        
        if fix_type == 'indentation_fix':
            return self.fix_indentation_in_code(code, code_change)
        elif fix_type == 'syntax_fix':
            return self.fix_syntax_in_code(code, code_change)
        elif fix_type == 'variable_fix':
            return self.fix_variable_in_code(code, code_change)
        elif fix_type == 'import_fix':
            return self.fix_import_in_code(code, code_change)
        else:
            return self.apply_generic_fix(code, code_change)
    
    def fix_indentation_in_code(self, code, change):
        """들여쓰기 수정"""
        lines = code.split('\n')
        error_line = change.get('line', 0)
        
        if error_line < len(lines):
            # 들여쓰기 수정
            fixed_line = self.correct_indentation(lines[error_line])
            lines[error_line] = fixed_line
        
        return '\n'.join(lines)
    
    def fix_syntax_in_code(self, code, change):
        """구문 오류 수정"""
        # AST 기반 수정
        try:
            tree = ast.parse(code)
            fixed_tree = self.fix_ast_syntax(tree, change)
            return ast.unparse(fixed_tree)
        except:
            # AST 수정 실패 시 문자열 기반 수정
            return self.fix_syntax_string(code, change)

class FixValidator:
    def validate(self, code, original_error):
        """수정 검증"""
        validation_results = []
        
        # 구문 검증
        syntax_valid = self.validate_syntax(code)
        validation_results.append({
            'type': 'syntax',
            'valid': syntax_valid,
            'message': '구문 검증 완료' if syntax_valid else '구문 오류 발견'
        })
        
        # 원본 오류 해결 확인
        error_resolved = self.check_error_resolution(code, original_error)
        validation_results.append({
            'type': 'error_resolution',
            'valid': error_resolved,
            'message': '원본 오류 해결됨' if error_resolved else '원본 오류 미해결'
        })
        
        # 새로운 오류 발생 확인
        new_errors = self.check_new_errors(code)
        validation_results.append({
            'type': 'new_errors',
            'valid': len(new_errors) == 0,
            'message': f'새로운 오류 {len(new_errors)}개 발견' if new_errors else '새로운 오류 없음',
            'new_errors': new_errors
        })
        
        # 전체 검증 결과
        is_valid = all(result['valid'] for result in validation_results)
        
        return {
            'is_valid': is_valid,
            'results': validation_results,
            'summary': self.generate_validation_summary(validation_results)
        }
```

### 2. 학습 기반 수정 시스템

```python
class FixLearningSystem:
    def __init__(self):
        self.fix_patterns = {}
        self.success_history = []
        self.failure_history = []
        self.ml_model = FixMLModel()
    
    def learn_from_fix(self, error, fix, result):
        """수정 결과로부터 학습"""
        learning_data = {
            'error': error,
            'fix': fix,
            'result': result,
            'timestamp': time.time()
        }
        
        if result['success']:
            self.success_history.append(learning_data)
            self.update_success_patterns(error, fix)
        else:
            self.failure_history.append(learning_data)
            self.update_failure_patterns(error, fix)
        
        # ML 모델 업데이트
        self.ml_model.update(learning_data)
    
    def update_success_patterns(self, error, fix):
        """성공 패턴 업데이트"""
        error_type = error.get('type', '')
        fix_type = fix.get('type', '')
        
        pattern_key = f"{error_type}_{fix_type}"
        
        if pattern_key not in self.fix_patterns:
            self.fix_patterns[pattern_key] = {
                'success_count': 0,
                'total_count': 0,
                'confidence': 0.0
            }
        
        self.fix_patterns[pattern_key]['success_count'] += 1
        self.fix_patterns[pattern_key]['total_count'] += 1
        self.fix_patterns[pattern_key]['confidence'] = (
            self.fix_patterns[pattern_key]['success_count'] / 
            self.fix_patterns[pattern_key]['total_count']
        )
    
    def suggest_learned_fixes(self, error, context):
        """학습된 수정 제안 생성"""
        error_type = error.get('type', '')
        
        # 유사한 오류 패턴 찾기
        similar_errors = self.find_similar_errors(error, context)
        
        # 성공한 수정 패턴 찾기
        successful_fixes = []
        for similar_error in similar_errors:
            pattern_key = f"{error_type}_{similar_error['fix_type']}"
            if pattern_key in self.fix_patterns:
                pattern = self.fix_patterns[pattern_key]
                if pattern['confidence'] > 0.7:  # 70% 이상 성공률
                    successful_fixes.append({
                        'fix_type': similar_error['fix_type'],
                        'confidence': pattern['confidence'],
                        'success_count': pattern['success_count'],
                        'adaptation': self.adapt_fix_to_error(
                            similar_error['fix'], 
                            error
                        )
                    })
        
        return successful_fixes
    
    def adapt_fix_to_error(self, original_fix, new_error):
        """수정 제안을 새로운 오류에 맞게 적응"""
        adapted_fix = original_fix.copy()
        
        # 오류 위치에 맞게 수정
        adapted_fix['line'] = new_error.get('line', 0)
        adapted_fix['column'] = new_error.get('column', 0)
        
        # 오류 메시지에 맞게 수정 내용 조정
        if 'code_change' in adapted_fix:
            adapted_fix['code_change'] = self.adapt_code_change(
                adapted_fix['code_change'], 
                new_error
            )
        
        return adapted_fix
```

## 🎯 통합 자가 수정 시스템

### 1. 완전한 자가 수정 파이프라인

```python
class SelfCorrectionPipeline:
    def __init__(self):
        self.error_detector = ErrorDetectionSystem()
        self.diagnostic_system = SelfDiagnosticSystem()
        self.fix_suggester = FixSuggestionSystem()
        self.auto_fixer = AutoFixEngine()
        self.learning_system = FixLearningSystem()
        self.monitor = CorrectionMonitor()
    
    def process_error(self, code, context):
        """오류 처리 파이프라인"""
        # 1. 오류 감지
        errors = self.error_detector.detect_errors(code, context)
        
        if not errors:
            return {'status': 'no_errors', 'code': code}
        
        # 2. 오류별 처리
        correction_results = []
        fixed_code = code
        
        for error in errors:
            # 진단
            diagnosis = self.diagnostic_system.diagnose_error(error, context)
            
            # 수정 제안 생성
            fix_suggestions = self.fix_suggester.generate_fixes(
                error, 
                diagnosis, 
                context
            )
            
            # 최적 수정 제안 선택
            best_fix = self.select_best_fix(fix_suggestions, error, context)
            
            if best_fix:
                # 수정 적용
                fix_result = self.auto_fixer.apply_fix(
                    error, 
                    best_fix, 
                    context
                )
                
                if fix_result['success']:
                    fixed_code = fix_result['fixed_code']
                    context['code'] = fixed_code
                    
                    # 학습 데이터 저장
                    self.learning_system.learn_from_fix(
                        error, 
                        best_fix, 
                        fix_result
                    )
                
                correction_results.append({
                    'error': error,
                    'diagnosis': diagnosis,
                    'fix': best_fix,
                    'result': fix_result
                })
        
        # 3. 최종 검증
        final_validation = self.validate_final_code(fixed_code, context)
        
        return {
            'status': 'completed',
            'original_code': code,
            'fixed_code': fixed_code,
            'corrections': correction_results,
            'validation': final_validation,
            'learning_updated': True
        }
    
    def select_best_fix(self, fix_suggestions, error, context):
        """최적 수정 제안 선택"""
        if not fix_suggestions:
            return None
        
        # 점수 기반 선택
        best_fix = max(fix_suggestions, key=lambda x: x.get('score', 0))
        
        # 최소 신뢰도 확인
        if best_fix.get('confidence', 0) < 0.5:
            return None
        
        return best_fix

class CorrectionMonitor:
    def __init__(self):
        self.metrics = {
            'errors_detected': 0,
            'errors_fixed': 0,
            'fix_success_rate': 0.0,
            'average_fix_time': 0.0,
            'learning_improvements': 0
        }
        self.performance_history = []
    
    def track_correction(self, correction_result):
        """수정 과정 추적"""
        self.metrics['errors_detected'] += len(correction_result.get('corrections', []))
        
        successful_fixes = sum(
            1 for correction in correction_result.get('corrections', [])
            if correction.get('result', {}).get('success', False)
        )
        
        self.metrics['errors_fixed'] += successful_fixes
        
        # 성공률 업데이트
        if self.metrics['errors_detected'] > 0:
            self.metrics['fix_success_rate'] = (
                self.metrics['errors_fixed'] / self.metrics['errors_detected']
            )
        
        # 성능 기록
        self.performance_history.append({
            'timestamp': time.time(),
            'success_rate': self.metrics['fix_success_rate'],
            'errors_processed': len(correction_result.get('corrections', []))
        })
    
    def generate_performance_report(self):
        """성능 보고서 생성"""
        return {
            'metrics': self.metrics,
            'trends': self.analyze_trends(),
            'recommendations': self.generate_recommendations()
        }
```

## 📊 성능 모니터링 및 최적화

### 1. 수정 성능 측정

```python
class CorrectionPerformanceAnalyzer:
    def __init__(self):
        self.performance_metrics = {
            'detection_accuracy': [],
            'diagnosis_accuracy': [],
            'fix_success_rate': [],
            'fix_time': [],
            'learning_effectiveness': []
        }
    
    def analyze_correction_performance(self, correction_data):
        """수정 성능 분석"""
        # 감지 정확도
        detection_accuracy = self.calculate_detection_accuracy(correction_data)
        self.performance_metrics['detection_accuracy'].append(detection_accuracy)
        
        # 진단 정확도
        diagnosis_accuracy = self.calculate_diagnosis_accuracy(correction_data)
        self.performance_metrics['diagnosis_accuracy'].append(diagnosis_accuracy)
        
        # 수정 성공률
        fix_success_rate = self.calculate_fix_success_rate(correction_data)
        self.performance_metrics['fix_success_rate'].append(fix_success_rate)
        
        # 수정 시간
        fix_time = self.calculate_fix_time(correction_data)
        self.performance_metrics['fix_time'].append(fix_time)
        
        # 학습 효과성
        learning_effectiveness = self.calculate_learning_effectiveness(correction_data)
        self.performance_metrics['learning_effectiveness'].append(learning_effectiveness)
        
        return {
            'detection_accuracy': detection_accuracy,
            'diagnosis_accuracy': diagnosis_accuracy,
            'fix_success_rate': fix_success_rate,
            'fix_time': fix_time,
            'learning_effectiveness': learning_effectiveness
        }
    
    def calculate_detection_accuracy(self, correction_data):
        """감지 정확도 계산"""
        total_errors = len(correction_data.get('corrections', []))
        if total_errors == 0:
            return 1.0
        
        correctly_detected = sum(
            1 for correction in correction_data.get('corrections', [])
            if correction.get('error', {}).get('type') != 'false_positive'
        )
        
        return correctly_detected / total_errors
    
    def calculate_fix_success_rate(self, correction_data):
        """수정 성공률 계산"""
        corrections = correction_data.get('corrections', [])
        if not corrections:
            return 0.0
        
        successful_fixes = sum(
            1 for correction in corrections
            if correction.get('result', {}).get('success', False)
        )
        
        return successful_fixes / len(corrections)
```

## 🎯 다음 단계

이 가이드를 완료한 후 다음 단계를 진행하세요:

1. **[4-4: MultiDevin 모델의 이해](4-4-multidevin-model.md)**: 병렬 작업 실행을 위한 관리자-작업자 에이전트 구조 설계
2. **[4-5: Devin 플레이북 적용](4-5-devin-playbook-application.md)**: 레거시 시스템 리팩토링 프로젝트에 "Devin 군대" 활용하기
3. **[4-6: 알려진 한계와 현실](4-6-known-limitations-reality.md)**: 현재 AI 에이전트의 한계를 이해하고 현실적인 기대치 설정하기

## 📚 추가 리소스

- [자가 수정 시스템 설계](https://self-correction.dev/)
- [오류 감지 알고리즘](https://error-detection.dev/)
- [자동 디버깅 기법](https://auto-debugging.dev/)
- [AI 학습 시스템 구현](https://ai-learning-systems.dev/)

---

**"스스로 배우고 개선하는 AI"** - 자가 수정 메커니즘을 구현하여 오류를 스스로 감지, 진단, 수정하고 학습하는 AI 에이전트를 구축하세요!
