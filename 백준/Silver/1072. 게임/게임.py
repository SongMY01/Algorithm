X, Y = map(int, input().split())
Z = (Y * 100) // X

# 이미 승률이 99% 이상이면 절대 승률이 오르지 않음
if Z >= 99:
    print(-1)
else:
    start, end = 1, 1_000_000_000
    answer = -1

    while start <= end:
        mid = (start + end) // 2
        new_Z = ((Y + mid) * 100) // (X + mid)

        if new_Z > Z:
            answer = mid
            end = mid - 1  # 더 적은 수로도 가능한지 탐색
        else:
            start = mid + 1

    print(answer)
