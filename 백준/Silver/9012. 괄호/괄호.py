def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"


# 입력 받기
T = int(input())
for _ in range(T):
    ps = input().strip()
    print(is_vps(ps))
