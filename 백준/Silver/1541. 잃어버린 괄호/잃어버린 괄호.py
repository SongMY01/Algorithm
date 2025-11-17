import sys
input = sys.stdin.readline

expr = input().strip()

# '-' 기준으로 나누기
parts = expr.split('-')

def calc(part):
    # '+' 기준으로 쪼개서 전부 더함
    return sum(map(int, part.split('+')))

# 첫 번째 부분은 그대로 더하고
result = calc(parts[0])

# 두 번째 부분부터는 전부 빼기
for p in parts[1:]:
    result -= calc(p)

print(result)