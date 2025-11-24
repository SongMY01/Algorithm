import sys
input = sys.stdin.readline

INF = float('inf')

n, m = map(int, input().split())
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 거리 배열
dist = [INF] * (n + 1)
dist[1] = 0   # 시작점 1번

# 1. 벨만포드: n-1번 완화
for _ in range(n - 1):
    for a, b, w in edges:
        if dist[a] != INF and dist[b] > dist[a] + w:
            dist[b] = dist[a] + w

# 2. 음수 사이클 검사: n번째 완화 시도가 성공하면 사이클 존재!
for a, b, w in edges:
    if dist[a] != INF and dist[b] > dist[a] + w:
        print(-1)
        sys.exit(0)

# 3. 출력
for i in range(2, n + 1):
    print(dist[i] if dist[i] != INF else -1)