from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2

    # 총합이 홀수면 절대 불가능
    if total % 2 != 0:
        return -1

    target = total // 2
    count = 0
    limit = len(queue1) * 3  # 최대 이동 횟수 제한 (무한 루프 방지)

    # 두 합이 같아질 때까지 반복
    while sum1 != target and count <= limit:
        if sum1 > target:  # queue1이 더 많으면
            x = q1.popleft()
            sum1 -= x
            q2.append(x)
        else:              # queue2가 더 많으면
            x = q2.popleft()
            sum1 += x
            q1.append(x)
        count += 1

    return count if sum1 == target else -1
