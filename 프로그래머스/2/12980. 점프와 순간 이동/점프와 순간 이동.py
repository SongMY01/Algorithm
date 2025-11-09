def solution(n):
    battery = 0
    while n > 0:
        if n % 2 == 0:     # 짝수 → 순간이동
            n //= 2
        else:              # 홀수 → 점프 (1칸 줄이기)
            n -= 1
            battery += 1
    return battery
