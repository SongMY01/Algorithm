n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]

# 초기값 설정 (1번 집)
dp[0][0] = cost[0][0]  # 빨강
dp[0][1] = cost[0][1]  # 초록
dp[0][2] = cost[0][2]  # 파랑

# 점화식 적용
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 마지막 집까지의 최솟값
print(min(dp[n-1]))
