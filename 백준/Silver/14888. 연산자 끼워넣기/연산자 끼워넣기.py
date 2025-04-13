import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)

def dfs(index, current):
    global max_val, min_val, add, sub, mul, div

    if index == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return

    if add:
        add -= 1
        dfs(index + 1, current + nums[index])
        add += 1
    if sub:
        sub -= 1
        dfs(index + 1, current - nums[index])
        sub += 1
    if mul:
        mul -= 1
        dfs(index + 1, current * nums[index])
        mul += 1
    if div:
        div -= 1
        if current < 0:
            dfs(index + 1, -(-current // nums[index]))
        else:
            dfs(index + 1, current // nums[index])
        div += 1

# 시작은 첫 번째 숫자
dfs(1, nums[0])

print(max_val)
print(min_val)
