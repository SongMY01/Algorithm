T = int(input())  # 테스트 케이스 수

# 최대 40까지 미리 계산
MAX = 41
count_0 = [0] * MAX
count_1 = [0] * MAX

# 초기값
count_0[0] = 1
count_1[0] = 0
count_0[1] = 0
count_1[1] = 1

# DP로 계산
for i in range(2, MAX):
    count_0[i] = count_0[i - 1] + count_0[i - 2]
    count_1[i] = count_1[i - 1] + count_1[i - 2]

# 테스트 케이스 출력
for _ in range(T):
    n = int(input())
    print(count_0[n], count_1[n])
