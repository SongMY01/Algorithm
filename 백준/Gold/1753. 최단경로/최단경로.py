import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

INF = float('inf')
dist = [INF] * (V+1)
dist[K] = 0

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        # 이미 더 짧은 거리로 방문한 적 있으면 무시
        if dist[cur_node] < cur_cost:
            continue

        for weight, next_node in graph[cur_node]:
            next_cost = cur_cost + weight

            # 더 짧은 경로 찾으면 갱신
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))

dijkstra(K)

# 출력
for i in range(1, V+1):
    print(dist[i] if dist[i] != INF else "INF")