def solution(s):
    answer = ''
    flag = 1
    for i in range(len(s)):
        if flag == 1:
            answer += s[i].upper()
            flag = 0
        else:
            answer += s[i].lower()
        if s[i] == ' ':
            flag = 1
    return answer
