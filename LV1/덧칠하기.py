def solution(n, m, section):
    answer = 0
    curPos = 0

    for start in section:
        if start > curPos:
            answer += 1
            curPos = start+m-1
            print(curPos)
    print(answer)
    return answer


solution(8, 4, [2, 3,  6])
