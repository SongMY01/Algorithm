def solution(today, terms, privacies):
    answer = []

    # 날짜를 '일'로 변환하는 함수
    def to_days(date_str):
        y, m, d = map(int, date_str.split("."))
        return y * 12 * 28 + m * 28 + d

    # 약관 딕셔너리 생성
    term_dict = {}
    for t in terms:
        name, months = t.split()
        term_dict[name] = int(months)

    today_days = to_days(today)

    # 개인정보별 파기 여부 확인
    for idx, privacy in enumerate(privacies):
        date_str, term_type = privacy.split()
        start_days = to_days(date_str)
        expire_days = start_days + term_dict[term_type] * 28

        if expire_days <= today_days:
            answer.append(idx + 1)  # 번호는 1부터 시작

    return answer
