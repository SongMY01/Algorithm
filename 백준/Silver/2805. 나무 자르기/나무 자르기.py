
def is_possible(trees, height, m):
    return sum((tree - height) for tree in trees if tree > height) >= m

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2  # 현재 절단기 높이

    total = sum((tree - mid) for tree in trees if tree > mid)

    if total >= m:
        result = mid  # 더 큰 높이도 가능한지 확인
        start = mid + 1
    else:
        end = mid - 1

print(result)
