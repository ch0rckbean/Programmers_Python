import string


def solution(s, skip, index):
    lower = [i for i in string.ascii_lowercase]
    lower = [ch for ch in lower if ch not in skip]  # skip의 문자 제거
    answer = ''
    s = list(s)

    for i in range(len(s)):
        idx = lower.index(s[i])
        # 각 문자를 인덱스만큼 민 알파벳 매치 : 나머지를 잘 활용하자
        s[i] = lower[(idx+index) % len(lower)]
        answer += s[i]
    print(answer, s)
    return answer


solution("aukks", "wbqd", 5)
