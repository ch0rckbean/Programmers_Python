def solution(strings, n):
    answer = []
    arr = []
    for i in strings:
        arr.append(i[n]+i)
    arr = sorted(arr)
    print(arr)

    for i in arr:
        answer.append(i[1:])

    print(answer)
    return answer


solution(["sun", "bed", "car"], 1)
solution(["abce", "abcd", "cdx"], 2)
