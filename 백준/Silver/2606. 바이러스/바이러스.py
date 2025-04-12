from collections import deque

n = int(input()) 
m = int(input()) 
v = 1
total =0

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
    count = 1 
    for neighbor in graph[v]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited)
    return count

visited_dfs = [False] * (n + 1)
total = dfs(v, visited_dfs)
print(total-1)

