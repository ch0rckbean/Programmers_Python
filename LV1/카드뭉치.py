def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx1 = 0
    idx2 = 0

    for g in goal:
        if idx1 < len(cards1) and g == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and g == cards2[idx2]:
            idx2 += 1
        else:
            answer = 'No'
            break

    print(answer)
    return answer


solution(["i", "drink", "water"], ["want", "to"],
         ["i", "want", "to", "drink", "water"])

solution(["i", "water", "drink"], ["want", "to"],
         ["i", "want", "to", "drink", "water"])
