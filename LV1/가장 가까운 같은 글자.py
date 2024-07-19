def solution(s):
    answer = []
    di = {}

    for i in range(len(s)):
        if s[:i+1].count(s[i]) == 1:
            answer.append(-1)
        else:
            answer.append(i-di[s[i]])
        di[s[i]] = i  # 가장 마지막에 나온 인덱스 저장
        # {'b': 0, 'a': 5, 'n': 4} , {'f': 0, 'o': 2, 'b': 3, 'a': 4, 'r': 5}

    print(di, answer)
    return answer


solution("banana")
solution("foobar")
