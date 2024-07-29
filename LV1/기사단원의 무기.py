def solution(number, limit, power):
    answer = 0
    cntArr = []  # 약수 개수 리스트

    # 1. number까지의 수들의 약수 개수 구하기 : 시간 초과 주의
    for i in range(1, number+1):
        divisorsArr = []  # 약수 리스트 매번 초기화
        for j in range(1, int(number**(1/2))+1):  # 공약수
            if i % j == 0:
                # 약수 한번에 삽입
                divisorsArr.append(i//j)
                divisorsArr.append(j)
        num = len(set(divisorsArr))  # 약수 개수에 들어갈 cnt(중복 제거)

    # 2. limit와 약수 개수 최대값 비교
        if num > limit:
            # 3. limit에 걸리는 약수 개수를 power로 교체
            cntArr.append(power)
        else:
            cntArr.append(num)
    print(cntArr)

    answer = sum(cntArr)
    print(answer)
    return answer


solution(5, 3, 2)  # 10
solution(10, 3, 2)  # 21
