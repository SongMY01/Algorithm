def solution(arr1, arr2):
    result = []  # 결과 행렬

    # 각 행(row1, row2)끼리 묶어서 반복
    for row1, row2 in zip(arr1, arr2):
        new_row = []  # 더한 결과를 담을 새로운 행

        # 각 행의 같은 열(a, b)끼리 더함
        for a, b in zip(row1, row2):
            new_row.append(a + b)

        result.append(new_row)  # 완성된 행을 전체 결과에 추가

    return result
