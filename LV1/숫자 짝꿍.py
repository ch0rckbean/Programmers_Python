def solution(X, Y):
    answer = ''
    # 횟수 셀 딕셔너리
    xCnt = {str(i): 0 for i in range(10)}
    yCnt = {str(i): 0 for i in range(10)}

    # 문자열 분리
    X = list(X)
    Y = list(Y)

    # 횟수 카운트
    for i in X:
        xCnt[i] += 1
    for i in Y:
        yCnt[i] += 1

    # 짝꿍 이룰 수 있는 수 추출: 9부터 하는 이유는 sort 대신 쓰려고
    for i in range(9, -1, -1):
        i = str(i)
        iterNum = min(xCnt[i], yCnt[i])

        # 0이 여러개면
        if answer == '' and i == '0' and iterNum > 0:
            return "0"

        # sort 대신 큰 수 만들 수 있음
        answer += i * iterNum

    if answer == '':  # 짝꿍 아니면
        return "-1"
    else:
        return answer


print(solution("12321", "42531"))
