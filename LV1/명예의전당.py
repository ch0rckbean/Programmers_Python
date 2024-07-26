def solution(k, score):
    answer = []
    rank = []

    for i in range(len(score)):
        rank.append(score[0])
        score.remove(score[0])
        if (len(rank) == k+1):
            rank.remove(min(rank))
        answer.append(min(rank))
        print('rank', rank)
        print('score', score)
        print('answer', answer)
        print('------------')

    answer = answer+score
    print(answer)
    return answer


solution(3, [10, 100, 20, 150, 1, 100, 200])
