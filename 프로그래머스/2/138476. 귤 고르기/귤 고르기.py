from collections import Counter

def solution(k, tangerine):
    # 크기별 개수 세기
    counter = Counter(tangerine)

    # 개수가 많은 순으로 정렬
    counts = sorted(counter.values(), reverse=True)

    # 누적합으로 k개 채울 때까지 종류 세기
    total = 0
    kinds = 0
    for c in counts:
        total += c
        kinds += 1
        if total >= k:
            break
    return kinds
