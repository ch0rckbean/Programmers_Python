def solution(s):
    answer = 0
    same = 0
    dif = 0

    for i in range(len(s)):
        if same == dif:
            answer += 1
            x = s[i]  # 시작 문자 변경
            same, dif = 0, 0  # 같은, 다른 수 초기화

        if x == s[i]:  # 초기 문자와 다음 문자가 같으면
            same += 1
        else:
            dif += 1

    print(answer)
    return answer


solution('banana')
solution('bbanana')
