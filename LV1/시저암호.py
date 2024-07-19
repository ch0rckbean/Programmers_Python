import string

strArr1 = string.ascii_lowercase
strArr2 = string.ascii_uppercase
idx = 0


def solution(s, n):
    answer = ''
    for i in s:
        # 대문자일 때
        if i.isupper():
            # if i>='A' and i<='Z'

            # indexErr나므로 +n 여기서 해야 함
            idx = strArr2.find(i)+n
            answer += strArr2[idx % 26]

        # 소문자일 때
        elif i.islower():
            # elif i>='a' and i<='z'
            idx = strArr1.find(i)+n
            print(idx, 'idx')
            # answer += strArr1[idx % 26+n]
            answer += strArr1[idx % 26]

        # 공백 처리
        elif i == " ":
            answer += " "

    print(answer)
    return answer


solution("AB", 1)  # BC
solution("z", 1)  # a
solution("a B z", 4)  # e F d
