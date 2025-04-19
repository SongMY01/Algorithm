import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 리스트를 최소 힙으로 변환
    answer = 0

    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)      # 가장 맵기 낮은 음식
        second = heapq.heappop(scoville)     # 두 번째 낮은 음식
        new = first + (second * 2)

        heapq.heappush(scoville, new)        # 새로운 음식 삽입
        answer += 1

    # 모든 음식의 스코빌 지수가 K 이상인지 확인
    return answer if scoville[0] >= K else -1
