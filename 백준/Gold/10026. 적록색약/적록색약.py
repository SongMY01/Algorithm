import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 늘림
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
graph = [list(input().strip()) for _ in range(N)]

# 일반인과 적록색약인을 위한 방문 배열 (각각 별도로 사용)
visited_normal = [[False] * N for _ in range(N)]
visited_colorblind = [[False] * N for _ in range(N)]

# 상하좌우 4방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS: 일반인용, R, G, B를 각각 다른 색으로 취급
def dfs_normal(x, y, color):
    visited_normal[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 좌표 유효성 검사
        if 0 <= nx < N and 0 <= ny < N:
            if not visited_normal[nx][ny] and graph[nx][ny] == color:
                dfs_normal(nx, ny, color)

# DFS: 적록색약용, R과 G는 같은 색으로 취급
def dfs_colorblind(x, y, color):
    visited_colorblind[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited_colorblind[nx][ny]:
                # 파랑은 그대로 구분, R과 G는 같은 취급
                if color == 'B':
                    if graph[nx][ny] == 'B':
                        dfs_colorblind(nx, ny, graph[nx][ny])
                else:
                    if graph[nx][ny] != 'B':  # R 또는 G인 경우
                        dfs_colorblind(nx, ny, graph[nx][ny])

# 구역 수 세기
normal_count = 0
colorblind_count = 0

for i in range(N):
    for j in range(N):
        # 일반인용 탐색: 아직 방문하지 않았고, 땅(색깔)이 있을 때 DFS 진행
        if not visited_normal[i][j]:
            dfs_normal(i, j, graph[i][j])
            normal_count += 1

        # 적록색약용 탐색: 동일하게 처리하되, R과 G가 같은 구역으로 취급
        if not visited_colorblind[i][j]:
            dfs_colorblind(i, j, graph[i][j])
            colorblind_count += 1

print(normal_count, colorblind_count)
