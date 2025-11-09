def solution(s):
    nums = list(map(int, s.split()))
    print(nums)
    return f"{min(nums)} {max(nums)}"