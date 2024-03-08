def solution(d, budget):
    answer = 0  # 지원 가능 팀 개수 변수
    sum = 0  # 예산 더할 변수

    d.sort()  # 순서 상관 없이 지원 해줘야 하므로
    for i in d:
        sum += i
        while sum <= budget:
            answer += 1
            break
    print(answer)
    print(sum)
    return answer


solution([1, 3, 2, 5, 4], 9)
solution([2, 2, 3, 3], 10)
