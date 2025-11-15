n = int(input())
nums = list(map(int,input().split()))

result = 0
m = max(nums)
for num in nums:
    result += num/m*100
result = result/n
print(result)