def solution(str):
    answer = ''
    arr = str.split('')
    # split()는 공백 여러개여도 하나로 처리
    # split('')는 공백 여러개면 여러개 그대로 처리

    for i in arr:  # 각 단어: try, hello, world
        for j in range(len(i)):  # 각 알파벳의 철자 수: 3, 5, 5
            if j % 2 == 0:  # 짝수일 때
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '  # 한 단어가 돌 때마다 공백 추가
    return answer[:-1]  # 마지막 공백 제거


solution('try hello world')
