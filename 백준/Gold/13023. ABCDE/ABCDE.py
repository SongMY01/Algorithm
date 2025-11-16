import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
answer = 0

def dfs(cur_v, depth):
    global answer
    if depth == 4:  # A-B-C-D-E 연결 완료
        answer = 1
        return
    
    visited[cur_v] = True
    
    for v in graph[cur_v]:   # 다음 친구 v 탐색
        if not visited[v]:
            dfs(v, depth + 1)
            if answer:   # 찾았으면 전체 종료
                return
    
    visited[cur_v] = False   # 백트래킹

# 모든 정점에서 DFS 시작
for i in range(N):
    dfs(i, 0)
    if answer:
        break

print(answer)
