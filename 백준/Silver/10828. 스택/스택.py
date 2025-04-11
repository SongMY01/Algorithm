import sys
input = sys.stdin.readline

n = int(input())  # 명령어 개수 입력
stack = []        # 스택 초기화

for _ in range(n):
    cmd = input().strip()

    if cmd.startswith("push"):
        _, num = cmd.split()
        stack.append(int(num))

    elif cmd == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif cmd == "size":
        print(len(stack))

    elif cmd == "empty":
        if stack:
            print(0)
        else:
            print(1)

    elif cmd == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
