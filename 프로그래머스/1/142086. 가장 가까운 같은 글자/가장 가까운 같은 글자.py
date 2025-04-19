def solution(s):
    answer = []
    stack = []
    indexs = {}
    for x,y in enumerate(s):
        if y not in stack:
            stack.append(y)
            indexs[y]=x
            answer.append(-1)
        else:
            answer.append(x-indexs[y])
            stack.append(y)
            indexs[y]=x

    return answer