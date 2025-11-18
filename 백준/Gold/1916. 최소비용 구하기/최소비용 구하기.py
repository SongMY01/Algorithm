import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

start,end = map(int,input().split())

INF = float('inf')
dist = [INF] * (N+1)
dist[start] = 0

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        # 이미 더 짧은 거리로 방문한 적 있으면 무시
        if dist[cur_node] < cur_cost:
            continue
        if cur_node == end:
            return cur_cost
        
        for weight, next_node in graph[cur_node]:
            next_cost = cur_cost + weight

            # 더 짧은 경로 찾으면 갱신
            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))

print(dijkstra(start))