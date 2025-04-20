def solution(n):
    count = 0
    k = 1  # 연속된 숫자의 개수

    while True:
        temp = n - (k * (k - 1)) // 2
        if temp <= 0:
            break
        if temp % k == 0:
            count += 1
        k += 1

    return count
