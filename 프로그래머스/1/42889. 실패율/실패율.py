def solution(N, stages):
    answer = []
    total = len(stages)
    
    for stage in range(1,N+1):
        same = stages.count(stage)
        if total == 0:
            failure_rate = 0
        else:
            failure_rate = same / total
        
        
        answer.append((stage, failure_rate))
        total -= same  # 다음 스테이지로 넘어감
        
        answer.sort(key=lambda x: (-x[1], x[0]))


    return [stage for stage, _ in answer]