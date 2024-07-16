def solution(t, p):
    answer = 0
    tLength = len(t)  # 12
    pLength = len(p)  # 1
    arr = []
    for i in range(tLength-pLength+1):  # 간격 수 만큼
        arr.append(int(t[i:pLength+i]))
        if (int(p) >= arr[i]):
            answer += 1
    print(arr, answer)

    return answer


solution("500220839878", "7")
solution("10203", "15")
