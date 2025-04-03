def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    answer = 0
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # 가벼운 사람도 태움
        j -= 1      # 무거운 사람 태움
        answer += 1  # 보트 하나 사용

    return answer
