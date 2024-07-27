def solution(a, b):
    answer = ''
    arr = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU',]
    # 윤년 = 2월
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0

    total = sum(months[:a-1]) + b - 1
    print(total)
    answer = arr[(total) % 7]

    print(answer)
    return answer


solution(5, 24)
