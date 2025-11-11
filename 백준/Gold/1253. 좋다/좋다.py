import sys
input = sys.stdin.readline

n = int(input())
result = 0
arr = list(map(int, input().split()))
arr.sort()    
    
for k in range(n):
    find = arr[k]
    i=0
    j=n-1
    while i<j:
        if arr[i] + arr[j] == find:
            if i!=k and j!=k:
                result += 1
                break
            elif i==k:
                i += 1
            elif j==k:
                j -= 1
        elif arr[i] + arr[j] < find:
            i += 1
        else:
            j -= 1
print(result)