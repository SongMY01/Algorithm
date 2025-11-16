import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = input().rstrip()  # \n 제거

check = list(map(int,input().split()))
cnt = [0, 0, 0, 0]  # 현재 윈도우의 A C G T 개수

# 함수: 문자 → index 매핑
def idx(c):
    if c == 'A': return 0
    if c == 'C': return 1
    if c == 'G': return 2
    return 3

# 첫 윈도우 초기화
for i in range(m):
    cnt[idx(arr[i])] += 1

result = 0
if all(cnt[i] >= check[i] for i in range(4)):
    result += 1

# 슬라이딩 윈도우 이동
for i in range(m, n):
    cnt[idx(arr[i])] += 1        # 새로 들어온 문자
    cnt[idx(arr[i-m])] -= 1      # 빠져나간 문자

    if all(cnt[j] >= check[j] for j in range(4)):
        result += 1

print(result)
