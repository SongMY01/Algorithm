K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(line // mid for line in lines)

    if count >= N:
        result = mid  # 조건을 만족하는 최대 길이 후보
        start = mid + 1  # 더 큰 길이가 가능한지 탐색
    else:
        end = mid - 1  # 너무 많이 잘라서 개수가 부족함 → 길이 줄이기

print(result)
