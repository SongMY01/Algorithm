import sys
input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    cmd = input().strip()

    if cmd.startswith("push"):
        _, num = cmd.split()
        queue.append(int(num))

    elif cmd == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

    elif cmd == "size":
        print(len(queue))

    elif cmd == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif cmd == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif cmd == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
