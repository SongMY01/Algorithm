n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

visited = set()
count = 0

for num in numbers:
    if x - num in visited:
        count += 1
    visited.add(num)

print(count)
