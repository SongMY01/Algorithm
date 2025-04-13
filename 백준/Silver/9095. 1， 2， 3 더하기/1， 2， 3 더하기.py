T = int(input())

# n의 최대값이 10이므로 dp는 11까지 만들면 충분
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 미리 DP 테이블 구성
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

# 테스트 케이스마다 정답 출력
for _ in range(T):
    n = int(input())
    print(dp[n])
