def solution(keymap, targets):
    answer = []
    key_dict = {}  # 알파벳: 눌린 횟수 딕셔너리

    for i in range(len(keymap)):
        for j in range(len(keymap[i])):  # 한 문자열
            char = keymap[i][j]  # 한 문자

            if char not in key_dict:  # 문자가 키 딕셔너리에 없으면
                key_dict[char] = j+1  # 문자 키 : 인덱스 +1 값으로 추가
            else:  # 있으면
                # 기존 값, 키맵의 인덱스 비교 => 최소값 추출
                key_dict[char] = min(key_dict[char], j+1)

    for target in targets:
        sum = 0
        for t in target:
            if t in key_dict:
                sum += key_dict[t]  # 눌린 횟수 더하기
            else:  # 만들 수 없으면
                sum = -1
                break
        answer.append(sum)

    print(answer)
    return answer


solution(["ABACD", "BCEFD"], ["ABCD", "AABB"])  # [9,4]
