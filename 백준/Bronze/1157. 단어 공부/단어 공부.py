from collections import Counter

word = input().strip().upper()  # 대문자로 변환
counter = Counter(word)         # 문자 빈도수 세기

most_common = counter.most_common()  # 빈도수 높은 순 정렬된 리스트
max_count = most_common[0][1]        # 가장 높은 빈도수

# 동일한 최대 빈도수가 2개 이상인지 확인
candidates = [char for char, cnt in most_common if cnt == max_count]

if len(candidates) > 1:
    print("?")
else:
    print(candidates[0])
