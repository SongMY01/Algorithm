def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]  # 요일 순서
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 각 월의 일 수 (2016년은 윤년이니까 2월 29일!)

    # 1월 1일부터 (a월 b일)까지 며칠 지났는지 계산!
    total_days = sum(month_days[:a - 1]) + (b - 1)

    # 며칠 지났는지 7로 나눠서 요일 찾기
    return days[total_days % 7]
