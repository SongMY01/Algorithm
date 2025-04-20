def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    puddles = set((x, y) for x, y in puddles)  # 빠른 탐색을 위해 set으로 변환

    dp[1][1] = 1  # 시작점

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in puddles:
                dp[y][x] = 0
            elif not (x == 1 and y == 1):  # 시작점 제외
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    return dp[n][m]
