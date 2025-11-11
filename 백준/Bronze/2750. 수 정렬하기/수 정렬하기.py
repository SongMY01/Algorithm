n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()  # 오름차순 정렬

for x in arr:
    print(x)
