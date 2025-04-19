def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]  # 자리별 가중치
    answer = 0
    
    for i, ch in enumerate(word):
        index = vowels.index(ch)  # 해당 문자가 모음 리스트에서 몇 번째인지
        answer += index * weights[i] + 1  # 누적 + 현재 위치 (+1은 자기 자신 포함)
    
    return answer
