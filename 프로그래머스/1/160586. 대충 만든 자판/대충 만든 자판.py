def solution(keymap, targets):
    answer = []
    key_dict = {}

    # 1. 문자별 최소 누름 수 저장
    for key in keymap:
        for idx, char in enumerate(key):
            # 이미 있으면 더 작은 값으로 갱신
            if char in key_dict:
                key_dict[char] = min(key_dict[char], idx + 1)
            else:
                key_dict[char] = idx + 1

    # 2. 각 target에 대해 최소 누름 수 합산
    for word in targets:
        total = 0
        for ch in word:
            if ch in key_dict:
                total += key_dict[ch]
            else:
                total = -1
                break
        answer.append(total)

    return answer
