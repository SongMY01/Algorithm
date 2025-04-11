import sys
input = sys.stdin.readline

n = int(input())
target = [int(input()) for _ in range(n)]

stack = []
result = []
cur = 1  # 현재 push할 숫자

for num in target:
    while cur <= num: # 목표 숫자까지 push
        stack.append(cur)
        result.append('+')
        cur += 1
    if stack[-1] == num: # 원하는 숫자가 stack top이면 pop
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit()
        
print('\n'.join(result))