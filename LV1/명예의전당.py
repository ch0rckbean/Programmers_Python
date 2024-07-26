def solution(k, score):
    answer = []
    rank = []

    for _ in range(len(score)):
        rank.append(score[0])  # 명예의 전당에 1명씩 추가
        score.remove(score[0])  # 점수 배열에서 추가된 사람 제거

        if (len(rank) == k+1):  # k번째 가수 이상 되면
            rank.remove(min(rank))  # k명 맞추기 위해 제거
        answer.append(min(rank))  # 최하위 점수 가리기

        print('rank', rank)
        print('score', score)
        print('answer', answer)
        print('------------')

    answer = answer+score  # 최하위 점수 + 안 추가되고 남은 점수
    print(answer)
    return answer


solution(3, [10, 100, 20, 150, 1, 100, 200])
