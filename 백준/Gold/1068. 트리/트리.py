import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

# 그래프 생성 (부모 → 자식)
graph = [[] for _ in range(n)]
root = -1
for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        graph[parents[i]].append(i)

# DFS로 리프노드 세기
count = 0

def dfs(node):
    global count
    if node == delete_node:
        return

    # 현재 노드의 자식 중 삭제되지 않은 노드만 필터링
    child_list = []
    for child in graph[node]:
        if child != delete_node:
            child_list.append(child)
            
    if not child_list:  # 자식이 없으면 leaf
        count += 1
        return

    for nxt in child_list:
        dfs(nxt)

# 루트 자체가 삭제되는 경우
if root != delete_node:
    dfs(root)

print(count)