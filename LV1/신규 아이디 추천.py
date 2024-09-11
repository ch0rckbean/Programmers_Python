import string


def solution(new_id):
    answer = ''
    apb = string.ascii_lowercase
    characters = ['-', '_', '.']
    nums = [str(i) for i in range(10)]  # 숫자를 문자열로 변환
    valid_chars = set(apb+''.join(characters)+''.join(nums))  # 유효한 문자 집합
    print(valid_chars)

    new_id = new_id.lower()
    new_id = ''.join([ch for ch in new_id if ch in valid_chars])

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')

    if new_id == '':
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    while len(new_id) < 3:
        new_id += new_id[-1]

    answer = new_id
    print(answer)
    return answer


solution("...!@BaT#*..y.abcdefghijklm")
solution("z-+.^.")
