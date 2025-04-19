def solution(board, moves):
    basket = []
    answer = 0

    for move in moves:
        col = move - 1  # 인덱스는 0부터 시작하니까 하나 빼줌
        for row in range(len(board)):
            if board[row][col] != 0:  # 인형이 있다면
                doll = board[row][col]  # 인형 꺼내고
                board[row][col] = 0     # 그 자리는 비워줌

                if basket and basket[-1] == doll:  # 바구니 맨 위랑 같으면
                    basket.pop()  # 바구니에서 꺼내고
                    answer += 2   # 두 개 터졌으니까 +2
                else:
                    basket.append(doll)  # 같지 않으면 바구니에 넣기
                break  # 인형 하나만 뽑았으니 그만 찾기

    return answer
