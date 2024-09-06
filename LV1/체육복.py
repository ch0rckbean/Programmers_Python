def solution(n, lost, reserve):
    answer = 0
    # 차집합
    res_set = set(reserve) - set(lost)  # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
    los_set = set(lost)-set(reserve)  # 진짜 잃어버린 사람

    for r in res_set:
        if r-1 in los_set:
            los_set.remove(r-1)
        elif r+1 in los_set:
            los_set.remove(r+1)
    answer = n-len(los_set)
    # for i in (reserve):
    #     for j in lost:
    #         if i - 1 == j or i+1 == j:
    #             reserve.pop(reserve.index(i))
    #             lost.pop(lost.index(j))
    #             answer = n-len(lost)
    print(answer)
    return answer


solution(5, [2, 4], [1, 3, 5])
