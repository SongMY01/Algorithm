from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 거리 배열
dist = [[0] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dist[x][y] = 1   # 시작 거리는 1

    while queue:
        cur_x, cur_y = queue.popleft()

        # 목적지 도착 → 바로 거리 반환
        if cur_x == n-1 and cur_y == m-1:
            return dist[cur_x][cur_y]

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == '1' and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[cur_x][cur_y] + 1
                    queue.append((nx, ny))

    return dist[n-1][m-1]

print(bfs(0, 0))