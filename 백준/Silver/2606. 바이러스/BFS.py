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

# BFS (큐)
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1
    return count

total = bfs(v)
print(total-1)
