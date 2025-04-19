def solution(progresses, speeds):
    answer = []
    days = []
    for i,j in zip(progresses,speeds):
         days.append((100 - i + j - 1) // j)
    
    current = days[0]
    count = 1

    for d in days[1:]:
        if d <= current:
            count += 1  # 같이 배포됨
        else:
            answer.append(count)
            current = d  # 새로운 배포 기준
            count = 1

    answer.append(count)  # 마지막 묶음
    
    return answer