def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    # 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고

    for b in babbling:
        for c in can:
            if c*2 in b:
                # 연속해서 같은 발음을 하는 것을 어려워합
                break
            b = b.replace(c, ' ')

        if b.strip() == '':  # 문자열 공백 제거
            answer += 1

    print(answer)
    return answer


solution(["aya", "yee", "u", "maa"])
solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"])
