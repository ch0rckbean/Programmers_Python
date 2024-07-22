def binary(n, arr):
    arr3 = []
    for i in arr:
        tmp = format(i, 'b')
        if len(tmp) != n:  # n자리수 아니면 0 넣기
            tmp = '0'*(n-len(tmp)) + str(tmp)
        arr3.append(tmp)
    print('arr: ', arr3)
    return arr3


def solution(n, arr1, arr2):
    answer = []
    tmpArr1 = []
    tmpArr2 = []
    tmpArr3 = []

    tmpArr1 = (binary(n, arr1))
    tmpArr2 = (binary(n, arr2))

    for i in range(len(tmpArr1)):
        tmpArr3.append((int(tmpArr1[i]) or int(tmpArr2[i])))

    for j in tmpArr3:
        j = str(j)
        j.replace('1', '#')
        j.replace('0', ' ')
        answer.append(j)
    print(answer)
    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
