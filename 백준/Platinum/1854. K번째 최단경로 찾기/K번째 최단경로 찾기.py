import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # (다음 노드, 비용)

# 각 정점까지의 경로 비용을 최대 k개까지 저장하는 최대 힙
dist = [[] for _ in range(n + 1)]

# 다익스트라용 우선순위 큐 (최소 힙)
pq = []
heapq.heappush(pq, (0, 1))           # (비용, 현재 정점)
heapq.heappush(dist[1], 0 * -1)      # 시작점까지의 비용 0 저장 (최대힙이므로 음수로)

while pq:
    cost, node = heapq.heappop(pq)

    # 이 node까지의 경로를 cost로 확장해본다
    for nxt, w in graph[node]:
        new_cost = cost + w

        # 1) 아직 k개 미만이면 그냥 넣기
        if len(dist[nxt]) < k:
            heapq.heappush(dist[nxt], -new_cost)
            heapq.heappush(pq, (new_cost, nxt))

        # 2) 이미 k개인데, 현재 가장 큰 값(= -dist[nxt][0])보다 더 작은 비용이면 교체
        elif -dist[nxt][0] > new_cost:
            heapq.heappop(dist[nxt])              # 가장 큰 값 제거
            heapq.heappush(dist[nxt], -new_cost)  # 새로운 값 넣기
            heapq.heappush(pq, (new_cost, nxt))

# 출력
for i in range(1, n + 1):
    if len(dist[i]) < k:
        print(-1)
    else:
        # dist[i]는 최대힙(음수로 저장) → 가장 큰 값이 k번째 최단경로
        print(-dist[i][0])