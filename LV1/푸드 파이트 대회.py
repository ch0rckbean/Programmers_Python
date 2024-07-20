def solution(food):
    answer = ''

    for i in range(len(food)-1):
        if food[i+1] > 1:
            answer += str(i+1)*(food[i+1]//2)  # 0 기준 앞쪽만 추가
        else:  # 남는 음식
            answer += ''
    answer += '0'  # 물 추가

    # 대칭 처리
    answer += answer[::-1]
    answer = answer.replace('0', '', 1)  # 0 1개 제거
    print(answer)
    return answer


solution([1, 3, 4, 6])
solution([1, 7, 1, 2])
