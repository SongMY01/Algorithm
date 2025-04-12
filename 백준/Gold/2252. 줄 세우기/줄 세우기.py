import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)     # a → b
    indegree[b] += 1       # b의 진입 차수 증가

# 큐에 진입 차수가 0인 노드부터 삽입
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

# 위상 정렬 수행
result = []
while queue:
    now = queue.popleft()
    result.append(now)

    for next in graph[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

print(*result)
