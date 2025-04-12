from collections import deque

# 입력
n, m, v = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]

# 간선 정보 저장 (무방향)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호 작은 순 방문을 위해 정렬
for i in range(1, n + 1):
    graph[i].sort()

# DFS (재귀)
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# BFS (큐)
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# 실행
visited_dfs = [False] * (n + 1)
dfs(v, visited_dfs)
print()
bfs(v)
