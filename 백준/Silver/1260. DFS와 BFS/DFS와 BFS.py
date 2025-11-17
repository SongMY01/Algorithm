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

# 인접 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()


# ---------------- DFS ----------------
visited_dfs = [False] * (n+1)

def dfs(cur):
    visited_dfs[cur] = True
    print(cur, end=' ')
    for nxt in graph[cur]:
        if not visited_dfs[nxt]:
            dfs(nxt)


# ---------------- BFS ----------------
visited_bfs = [False] * (n+1)

def bfs(start):
    q = deque([start])
    visited_bfs[start] = True
    
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        
        for nxt in graph[cur]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                q.append(nxt)


# 출력
dfs(v)
print()
bfs(v)
