def solution(N, stages):
    answer = []
    ratio = {}  # sorting 위해
    players = len(stages)  # 도전자 수

    for i in range(1, N+1):
        if players == 0:  # 스테이지에 도달한 유저가 없는 경우
            ratio[i] = 0
        else:
            ratio[i] = stages.count(i)/players  # 꼭 차례대로 셀 필요 없음!
            players -= stages.count(i)

    # 실패율 기준 내림차순 정렬
    answer = sorted(ratio, key=lambda x: ratio[x], reverse=True)
    print(ratio, answer)
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
