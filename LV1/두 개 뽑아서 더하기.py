import itertools


def solution(numbers):
    answer = []
    s = list(itertools.combinations(numbers, 2))

    for i in range(len(s)):
        answer.append(sum(s[i]))
    answer = sorted(list(set(answer)))
    print(s, answer)
    return answer


solution([2, 1, 3, 4, 1])
solution([5, 0, 2, 7])
