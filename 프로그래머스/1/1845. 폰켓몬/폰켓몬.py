def solution(nums):
    answer = 0
    unique = list(set(nums))
    answer = min(len(unique),len(nums)/2)
    return answer