n = int(input())
A = list(map(int, input().split()))

dp = [1] * n  # 최소 길이 1로 초기화

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:  # 감소하는 경우
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 가장 긴 길이 출력
