def solution(sizes):
    answer = 0
    height = 0
    width = 0
    widthArr = []
    heightArr = []
    arr2 = []

    for i in sizes:  # 배열 정렬
        arr2.append(sorted(i, reverse=True))
        print('arr2', arr2)

    for j in arr2:
        widthArr.append(j[0])  # 가로 배열
        heightArr.append(j[1])  # 세로 배열
        print(widthArr, heightArr, '가로 세로 배열')

        width = max(widthArr)  # 가로 최대값
        height = max(heightArr)  # 세로 최대값
        answer = width*height
        print(width, height, answer)
    return answer


solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])


# 오답
# for i in sizes:
#     widthArr.append(i[0])
#     heightArr.append(i[1])
# # print(widthArr, 'widthArr')
# # print(heightArr, 'heightArr')
# width = max(widthArr)
# height = max(heightArr)

# # print(width, height, '가로 세로 최대')

# for w in widthArr:
#     if w > height:
#         height = w
#     else:
#         height = height
# for h in heightArr:
#     if h > width:
#         width = h
#     else:
#         width = width

# answer = width*height
# print(width, height, answer)
