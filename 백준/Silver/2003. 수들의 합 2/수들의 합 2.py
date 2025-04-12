
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
count = 0

while True:
    if total >= m:
        total -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        total += arr[end]
        end += 1

    if total == m:
        count += 1

print(count)
