def solution(n, m, section):
    answer = 0
    painted_until = 0
    
    for s in section:
        if s > painted_until:
            painted_until = s + m - 1
            answer += 1
            
    return answer