s = input()
result = [-1] * 26  # 알파벳 수만큼 -1로 초기화

for i in range(len(s)):
    idx = ord(s[i]) - ord('a')  # 알파벳을 0~25 인덱스로 변환
    if result[idx] == -1:       # 아직 등장하지 않은 경우에만 저장
        result[idx] = i

print(' '.join(map(str, result)))
