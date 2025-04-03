def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        tmp = ''
        for j in i:
            if j in skill:
                tmp += j
        
        if tmp == skill[:len(tmp)]:
        	answer+=1
            
    return answer