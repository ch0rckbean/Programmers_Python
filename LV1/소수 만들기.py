from itertools import combinations


def solution(nums):
    answer = 0
    sumList = []  # 3개 수의 합 들어갈 리스트
# 모든 경우의 3개 수 뽑아 리스트로 만들기
    arr = list(combinations(nums, 3))

    # 리스트 내 3개 값들의 합 구하기
    sumList = [sum(i) for i in arr]
    print('sumList', sumList)

    # 소수 판별
    for summ in sumList:
        is_prime = True
        # 소수가 아닌 경우
        if summ < 2:  # 1. 1일 때
            is_prime = False
        else:
            for i in range(2, int(summ**0.5) + 1):  # 제곱근까지만 확인
                if summ % i == 0:  # 2. 1과 자기 자신 외에 다른 수로 나눠진다면
                    is_prime = False
                    break

        if is_prime:
            answer += 1
    print(answer)
    return answer


solution([1, 2, 3, 4])
solution([1, 2, 7, 6, 4])
