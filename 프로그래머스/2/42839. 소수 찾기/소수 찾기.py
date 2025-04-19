from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    possible = set()

    # 1자리 ~ len(numbers) 자리 순열 생성
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            possible.add(num)

    # 소수만 필터링
    count = sum(1 for num in possible if is_prime(num))
    return count
