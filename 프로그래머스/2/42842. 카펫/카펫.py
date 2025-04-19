def solution(brown, yellow):
    total = brown + yellow  # 전체 격자 수

    for h in range(3, total):  # 최소 세로는 3 이상
        if total % h == 0:
            w = total // h
            if (w - 2) * (h - 2) == yellow:
                return [w, h]
