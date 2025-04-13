import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한

# 4방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[y][x] = True
    size = 1  # 현재 위치도 포함
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                size += dfs(nx, ny)  # 누적합
    return size

while True:
    try:
        n = int(input())
        graph = [list(map(int, input().strip())) for _ in range(n)]
        visited = [[False] * n for _ in range(n)]

        count = 0
        island_sizes = []  # 각 섬의 크기 저장

        for y in range(n):
            for x in range(n):
                if graph[y][x] == 1 and not visited[y][x]:
                    size = dfs(x, y)
                    island_sizes.append(size)
                    count += 1

        print(count)  # 총 섬 개수 출력
        island_sizes.sort()  # 크기 정렬해서 출력
        for s in island_sizes:
            print(s)

    except:
        break  # EOF나 예외 발생 시 종료
