def solution(numbers, hand):
    answer = ''
    touch = ''
    # 현재 손가락 위치 :맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 #
    curL = 10
    curR = 12
    left = [1, 4, 7]
    right = [3, 6, 9]
    middle = [2, 5, 8, 0]

    # 번호별 좌표
    pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    for num in numbers:
        if num in left:
            touch += 'L'
            curL = num
        elif num in right:
            touch += 'R'
            curR = num
        else:
            # 0일 때 딕셔너리 기준 치환
            if curL == 0:
                curL == 11
            elif curR == 0:
                curR == 11

            # 딕셔너리에서 가져온 좌표
            leftPos = pos[curL]
            rightPos = pos[curR]
            numPos = pos[num]  # 목표 키패드

            # 맨해튼 거리 계산
            distL = abs(leftPos[0]-numPos[0]) + abs(leftPos[1]-numPos[1])
            distR = abs(rightPos[0]-numPos[0]) + abs(rightPos[1]-numPos[1])

            if distL < distR:
                touch += 'L'
                curL = num
            elif distR < distL:
                touch += 'R'
                curR = num
            elif distL == distR:
                touch += hand[:1].upper()
    print(answer, touch)
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
