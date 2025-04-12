from collections import deque

# 입력
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            # 처음 가는 길이면 거리 갱신
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    # 마지막 칸의 값이 최소 거리
    return graph[n-1][m-1]

print(bfs(0, 0))
