def solution(n, arr1, arr2):
    answer = []
    tmpArr = []
    tmpArr2 = []

    # 2진수 or 연산
    for i in range(len(arr1)):
        tmpArr.append(arr1[i] | arr2[i])

    # 2진수 변경
    for tmp in tmpArr:
        tmp = format(tmp, 'b')
        if len(tmp) != n:  # n자리수 아니면 0 넣기
            tmp = '0'*(n-len(tmp)) + str(tmp)
        tmpArr2.append(tmp)

    # #, 0 변경
    for tmp2 in tmpArr2:
        answer.append(tmp2.replace('1', '#').replace('0', ' '))

    print(tmpArr, tmpArr2)
    print(answer)
    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
