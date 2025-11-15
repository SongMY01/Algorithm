import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 나머지 빈도를 저장할 배열
count = [0] * M

prefix = 0
for x in arr:
    prefix = (prefix + x) % M
    count[prefix] += 1

# 정답 계산
# 1) prefix 자체가 0인 경우
answer = count[0]

# 2) 같은 나머리끼리 2개씩 고르는 조합
for c in count:
    if c >= 2:
        answer += c * (c - 1) // 2

print(answer)
