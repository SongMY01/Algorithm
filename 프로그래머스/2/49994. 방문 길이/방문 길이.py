def solution(dirs):
    x, y = 0, 0
    visited = set()

    direction_map = {
        'U': (0, 1, 1),  # 방향 코드: U=1
        'D': (0, -1, 2), # D=2
        'R': (1, 0, 3),  # R=3
        'L': (-1, 0, 4)  # L=4
    }

    for d in dirs:
        dx, dy, dir_code = direction_map[d]
        nx, ny = x + dx, y + dy

        # 범위 체크
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 현재 위치 + 방향을 저장
            # 또는 반대로도 저장해야 중복 판단 가능
            visited.add((x, y, dir_code))
            # 반대 방향도 함께 저장 (예: 오른쪽은 왼쪽도 저장해야 같은 길로 취급 가능)
            reverse_dir = {1:2, 2:1, 3:4, 4:3}
            visited.add((nx, ny, reverse_dir[dir_code]))

            x, y = nx, ny

    return len(visited) // 2  # 양방향 저장했기 때문에 나누기 2