from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        cur = queue.popleft()

        # 중요도가 더 높은 문서가 있다면 뒤로 보냄
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            count += 1  # 인쇄됨
            if cur[0] == m:
                print(count)
                break
