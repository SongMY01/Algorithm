def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    for i, c in enumerate(citations):
        if c < i + 1:
            return i
    return len(citations)  # 전부 조건 만족할 경우