from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 그래프 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 인접 리스트 정렬 (DFS를 작은 번호부터 방문하게 만들기 위해)
for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n+1)
# dfs
def dfs(cur):
    visited[cur] = True
    print(cur, end=' ')
    
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)

# bfs
def bfs(graph, cur_v):
    q = deque()
    q.append(v)
    visited = {v: True}
    while q:
        cur_v = q.popleft()
        print(cur_v, end=' ')
        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = True
    return

dfs(v)
print("")
bfs(graph,v)