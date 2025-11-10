import sys
sys.setrecursionlimit(3000)

def solution(n, m, x, y, r, c, k):
    # 방향 설정 (사전순: d < l < r < u)
    dirs = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

    # 맨해튼 거리 계산
    dist = abs(x - r) + abs(y - c)
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    path = []
    found = [False]  # 첫 해답만 찾고 종료하기 위한 플래그

    def dfs(cx, cy, step):
        # 이미 해답 찾았으면 중단
        if found[0]:
            return

        # 남은 거리보다 최소 거리 더 크면 가지치기
        remain = k - step
        if abs(cx - r) + abs(cy - c) > remain:
            return

        # 목표 도착 + 거리 정확히 k면 정답
        if step == k and cx == r and cy == c:
            found[0] = True
            return

        # 4방향 탐색 (사전순)
        for d, dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 1 <= nx <= n and 1 <= ny <= m:  # 격자 범위 내
                path.append(d)
                dfs(nx, ny, step + 1)
                if found[0]:
                    return
                path.pop()

    dfs(x, y, 0)
    return ''.join(path) if found[0] else "impossible"
