# import sys
# from math import sqrt

# # # 가로 >= 세로
# # 노랑 1개 -> 8개 ( 가로 3, 세로 3 )
# # 노랑 2개 -> 10개 ( 가로 4, 세로 3 )
# # 노랑 3개 -> 12개 ( 가로 5, 세로 3 )
# # 노랑 4개 -> 12개 ( 가로 4, 세로 4 )


# # (가로 * 세로 = brown + yellow) 5x2 = 10 (브라운)
# # 1) brown + yello를 더한 수를 구한다. ( 12 )
# # 2) 12의 약수를 구한다. ( 1, 12, 2, 3, 4, 6 )
# # 3) 자기 자신을 제외하고 다음의 수를 가지고 brown + yellow를 더한 수를 나눈 나머지를 구한다. 중간수
#     # 3-1) 48 ( 1 2 24 48 )

# def get_divisor(n):
#     n = int(n)
#     divisors = []

#     for i in range(1, n + 1):
#         if (n % i == 0):
#             divisors.append(i)

#     return divisors

# def solution(brown, yellow):
#     divisors = []
#     by_sum = brown + yellow
#     # 약수 구하기
#     divisors = get_divisor(by_sum)

#     # 약수의 중간 인덱스
#     index_a = len(divisors)//2

#     if len(divisors) % 2 == 0:
#         index_b = len(divisors)//2-1
#     else:
#         index_b = index_a

#     answer = [divisors[index_a], divisors[index_b]]


#     return answer


# i = 가로  a = 세로
def solution(brown, yellow):
    s = brown + yellow
    for i in range(s, 2, -1):  # 끝에서부터 가로 길이를 찾음
        if s % i == 0:  # 적절한 i 예상값이 나오면
            a = s // i  # 나눠진 몫(세로)를 구해봄

            # yellow 가로세로 사이즈는 brown에서
            # 가로세로에서 2를 뺀 값과 같아야 함
            # 그럴 경우 정답으로 처리 이외에는 continue
            if yellow == (i - 2) * (a - 2):
                return [i, a]
