def solution(clothes):
    answer = 0
    save = {}
    
    for i in clothes:
        if i[1] not in save:
            save[i[1]] = 1
        else:
            save[i[1]] += 1

    total = 1
    for i in save:
        total *= (save[i] + 1)  # 안 입는 경우 포함

    answer = total - 1  # 아무것도 안 입는 경우 제외
    return answer
