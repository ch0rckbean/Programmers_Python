def solution(answers):
    answer = [0 for i in range(3)]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        ans = answers[i]
        if (s1[i % len(s1)] == ans):
            answer[0] += 1
        if (s2[i % len(s2)] == ans):
            answer[1] += 1
        if (s3[i % len(s3)] == ans):
            answer[2] += 1

    result = []
    for i in range(len(answer)):
        if (answer[i] == max(answer)):
            result.append(i+1)
    result = sorted(result)

    print(result)
    return result


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])
