import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()  # (인덱스, 값)
result = []

for i in range(n):
    # 새로 들어온 값보다 큰 값들은 뒤에서 제거
    while dq and dq[-1][1] > arr[i]:
        dq.pop()

    # 현재 값 추가
    dq.append((i, arr[i]))

    # 윈도우 범위 벗어난 값 제거
    if dq[0][0] <= i - l:
        dq.popleft()

    # 현재 최솟값 저장
    result.append(dq[0][1])

print(*result)
