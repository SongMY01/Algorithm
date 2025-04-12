from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 방향: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 익은 토마토(1)의 위치를 미리 큐에 담는다
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

# BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

# 결과 확인
res = 0
for row in graph:
    for cell in row:
        if cell == 0:       # 아직도 익지 않은 토마토
            print(-1)
            exit()
        res = max(res, cell)

# 처음 익은 토마토가 1이었으므로 → 최소 일수 = 최대값 - 1
print(res - 1)
