import math

def solution(n, k):
    people = list(range(1, n + 1))  # [1, 2, ..., n]
    answer = []

    k -= 1  # 0-indexed로 만들기

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        idx = k // fact
        answer.append(people.pop(idx))
        k %= fact

    return answer
