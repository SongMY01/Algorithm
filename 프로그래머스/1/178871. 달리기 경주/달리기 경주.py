def solution(players, callings):
    # 이름 → 순위 인덱스
    rank_map = {name: i for i, name in enumerate(players)}

    for called in callings:
        idx = rank_map[called]          # 불린 선수의 현재 위치
        front = players[idx - 1]        # 앞 선수 이름

        # 자리 바꾸기
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        # 딕셔너리(위치 정보) 업데이트
        rank_map[called] -= 1
        rank_map[front] += 1

    return players
