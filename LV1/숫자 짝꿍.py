def solution(X, Y):
    answer = ''
    xCnt = {str(i): 0 for i in range(10)}
    yCnt = {str(i): 0 for i in range(10)}

    X = list(X)
    Y = list(Y)

    for i in X:
        xCnt[i] += 1
    for i in Y:
        yCnt[i] += 1

    for i in range(9, -1, -1):
        i = str(i)
        iterNum = min(xCnt[i], yCnt[i])

        if answer == '' and i == '0' and iterNum > 0:
            return "0"
        answer += i * iterNum

    if answer == '':
        return "-1"
    else:
        return answer


print(solution("12321", "42531"))
