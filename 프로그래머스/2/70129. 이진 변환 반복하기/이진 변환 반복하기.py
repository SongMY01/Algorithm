def solution(s):
    count = 0      # 변환 횟수
    zero_count = 0 # 제거된 0의 개수

    while s != '1':
        zero_count += s.count('0')     # 0 개수 누적
        s = s.replace('0', '')         # 0 제거
        s = bin(len(s))[2:]            # 길이를 2진수로 변환
        count += 1                     # 변환 횟수 +1

    return [count, zero_count]
