def solution(ingredient):
    # 1: 빵 2: 야채 3: 고기 1-2-3-1 순서대로만 만들 수 있음!
    answer = 0
    s = []
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                s.pop()  # 맨 마지막 요소 제거 (다 만든 햄버거)

    print(answer)
    return answer


solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
solution([1, 3, 2, 1, 2, 1, 3, 1, 2])
