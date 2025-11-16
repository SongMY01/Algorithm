import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def dfs(num, length):
    if length == N:
        print(num)
        return
    
    for digit in range(1, 10):  # 다음 자리
        new_num = num * 10 + digit
        if is_prime(new_num):   # 소수면 확장
            dfs(new_num, length + 1)

# 시작 숫자는 1자리 소수
for start in [2, 3, 5, 7]:
    dfs(start, 1)
