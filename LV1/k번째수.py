def solution(array, commands):
    answer = []
    arr = []

    for i in commands:
        # for command in commands:
        # i,j,k = command
        arr = array[i[0]-1:i[1]]  # sort()는 정렬 후 None 반환
        arr = sorted(arr)  # sorted()는 정렬 결과 반환
        answer.append(arr[i[2]-1])
    print(answer)
    return answer


solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
