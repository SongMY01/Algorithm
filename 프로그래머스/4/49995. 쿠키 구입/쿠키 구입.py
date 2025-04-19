def solution(cookie):
    answer = 0
    n = len(cookie)

    for m in range(n - 1):  # m: 중간 기준점 (왼쪽 끝 ~ 오른쪽 시작-1)
        left = m
        right = m + 1
        left_sum = cookie[left]
        right_sum = cookie[right]

        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)

            if left > 0 and left_sum <= right_sum:
                left -= 1
                left_sum += cookie[left]
            elif right < n - 1 and right_sum <= left_sum:
                right += 1
                right_sum += cookie[right]
            else:
                break

    return answer
