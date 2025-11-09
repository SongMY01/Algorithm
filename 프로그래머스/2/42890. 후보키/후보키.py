from itertools import combinations

def solution(relation):
    n_cols = len(relation[0])
    n_rows = len(relation)
    
    candidates = []  # 후보키 리스트

    # 가능한 모든 조합 탐색
    for r in range(1, n_cols + 1):
        for comb in combinations(range(n_cols), r):
            
            # 유일성 검사
            projection = [tuple(row[i] for i in comb) for row in relation]
            if len(set(projection)) != n_rows:
                continue
        
            # 최소성 검사
            if any(set(cand).issubset(comb) for cand in candidates):
                continue
            
            # 두 조건 만족 → 후보키로 등록
            candidates.append(comb)

    return len(candidates)
