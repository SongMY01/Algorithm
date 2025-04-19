from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    order = 0  # 실행 순서

    while queue:
        cur = queue.popleft()
        
        # 뒤에 더 높은 우선순위가 있는지 확인
        if any(cur[1] < other[1] for other in queue):
            queue.append(cur)  # 다시 뒤로 보내기
        else:
            order += 1  # 실행됨
            if cur[0] == location:  # 내가 찾던 프로세스
                return order
