def solution(a, b, n):  # a병 가져가서 b병 받구 n 병 갖구 있음
    answer = 0
    tmp = 0

    while n >= a:
        new = n//a * b  # 새로 받는 병
        rem = n % a  # 남는 병
        n = new+rem  # 전체 병
        answer += new

    print(answer)
    return answer


solution(2, 1, 20)
solution(3, 2, 20)
