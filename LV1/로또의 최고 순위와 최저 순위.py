def solution(lottos, win_nums):
    answer = []
    win = 0  # 일치 개수
    zero = lottos.count(0)

    for i in range(len(lottos)):
        if lottos[i] in win_nums:  # 일치 번호
            # lottos.pop(lottos[i])
            # win_nums.pop(win_nums[i])
            win += 1
            print(lottos, win_nums, win)

    # 일치 개수에 따른 순위 : 6,5,4,3,2,그 외(6)
    def cntRank(win):
        rank = 0
        if win == 6:
            rank = 1
        if win == 5:
            rank = 2
        if win == 4:
            rank = 3
        if win == 3:
            rank = 4
        if win == 2:
            rank = 5
        if win == 1 or win == 0:
            rank = 6
        return rank  # 안 하면 None

    answer.append(cntRank(win+zero))
    answer.append(cntRank(win))

    print(answer)
    return answer


solution([44, 1, 0, 0, 31, 25], 	[31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])  # 1, 6
