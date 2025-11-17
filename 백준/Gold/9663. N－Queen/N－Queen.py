import sys
input = sys.stdin.readline

N = int(input())

# 열, ↘대각선, ↙대각선 사용 여부 체크
col = [False] * N
diag1 = [False] * (2*N - 1)     # row + col
diag2 = [False] * (2*N - 1)     # row - col + (N-1)

answer = 0

def dfs(row):
    global answer
    
    if row == N:
        answer += 1
        return
    
    for c in range(N):
        d1 = row + c
        d2 = row - c + (N - 1)
        
        # 이미 사용한 열/대각선이면 skip
        if col[c] or diag1[d1] or diag2[d2]:
            continue
        
        # 사용 표시
        col[c] = diag1[d1] = diag2[d2] = True
        
        dfs(row + 1)
        
        # 백트래킹 (원상복귀)
        col[c] = diag1[d1] = diag2[d2] = False

dfs(0)

print(answer)
