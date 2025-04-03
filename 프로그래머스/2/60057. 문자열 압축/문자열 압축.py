def solution(s):
    min_len = len(s)  # 최소 압축 길이를 저장할 변수 (초기값: 원래 길이)

    for step in range(1, len(s) // 2 + 1):  # 압축 단위: 1부터 절반까지
        compressed = ""
        prev = s[0:step]  # 첫 덩어리
        count = 1

        # step 단위로 자르기
        for i in range(step, len(s), step):
            # 현재 덩어리와 이전 덩어리가 같으면 count 증가
            if prev == s[i:i + step]:
                count += 1
            else:
                # 다르면 지금까지 세었던 걸 압축에 추가
                if count > 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                # 새로운 덩어리로 초기화
                prev = s[i:i + step]
                count = 1

        # 마지막 남은 것 처리
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        # 최소 길이 갱신
        min_len = min(min_len, len(compressed))

    return min_len
