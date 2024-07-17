from itertools import combinations

def solution(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1

    print(answer)
    return answer


solution([-2, 3, 0, 2, -5])
solution([-1, 1, -1, 1])
