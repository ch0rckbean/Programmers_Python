def solution(name, yearning, photo):
    answer = []
    book = {}
    score = 0

    for i in range(len(name)):  # 이름과 점수 대응
        book[name[i]] = yearning[i]
    print(book)

    for i in photo:
        for j in i:
            if j in book.keys():
                score += book[j]
            else:
                score += 0
        answer.append(score)
        score = 0

    print(answer)
    return answer


solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain",
         "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
