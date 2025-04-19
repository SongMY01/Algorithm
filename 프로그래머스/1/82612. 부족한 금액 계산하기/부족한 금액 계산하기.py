def solution(price, money, count):
    answer = -1
    fee = price
    total = 0
    for i in range(1,count+1):
        total += price*i

    if money >= total:
        return 0
    answer = total - money
    return answer