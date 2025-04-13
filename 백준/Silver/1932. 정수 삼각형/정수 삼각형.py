n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# DP 삼각형 생성 (triangle 자체를 재사용)
for i in range(n-2, -1, -1):  # 아래에서부터 위로
    for j in range(i+1):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

# 맨 꼭대기의 값이 최대 경로의 합
print(triangle[0][0])