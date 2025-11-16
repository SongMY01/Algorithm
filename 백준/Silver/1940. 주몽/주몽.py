import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()

start = 0
end = n - 1
count = 0

while start < end:
    s = arr[start] + arr[end]

    if s == m:
        count += 1
        start += 1
        end -= 1
    elif s < m:
        start += 1
    else:
        end -= 1

print(count)
