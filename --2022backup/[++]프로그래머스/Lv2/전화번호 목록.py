def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        _len = len(phone_book[i])  # 접두사만 확인하기 위함
        if phone_book[i] in phone_book[i + 1][0:_len]:
            answer = False
            break

    return answer


print(solution(["12", "123", "1235", "567", "88"]))
