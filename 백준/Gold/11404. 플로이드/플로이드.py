import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float('inf')

# 거리 행렬 초기화
dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

# 간선 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)  # 여러 간선 대비


# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != INF else 0, end=' ')
    print()