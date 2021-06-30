import sys

def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        # 정렬하고 다음꺼하고 같으면 False로 기록
        if phone_book[i] in phone_book[i + 1]:
            answer = False
            break

    return answer


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
