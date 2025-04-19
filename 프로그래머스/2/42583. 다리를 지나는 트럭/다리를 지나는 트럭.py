from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리 위 상태
    truck_weights = deque(truck_weights)  # 대기 중 트럭
    total_weight = 0  # 다리 위 트럭 총 무게

    while bridge:
        time += 1
        # 다리에서 트럭 한 칸 전진 (앞에서 하나 나감)
        out = bridge.popleft()
        total_weight -= out

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                # 새 트럭 투입
                t = truck_weights.popleft()
                bridge.append(t)
                total_weight += t
            else:
                # 못 들어가면 0 추가 (빈 자리)
                bridge.append(0)

    return time
