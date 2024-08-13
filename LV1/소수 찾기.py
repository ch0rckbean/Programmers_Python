def solution(n):
    answer = 0

    if n > 1:  # 1은 소수가 아님
        for j in range(2, n + 1):
            is_prime = True
            for i in range(2, int(j**0.5) + 1):
                if j % i == 0:
                    is_prime = False
                    break
            if is_prime:
                answer += 1

    print(answer)
    return answer


solution(10)
solution(5)
