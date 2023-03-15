# import sys
# from math import sqrt
# from itertools import permutations

# # 1) 에라토스테네스의 체
# def is_prime_number(n):
#     # 리스트 초기화
#     array = [True for _ in range(n+1)]

#     # 제곱근까지만 순회
#     for i in range(2, int(sqrt(n))+1):
#         if array[i]:    # 만약 소수라면
#             j = 2
#             while j * i <= n:   # n이 될 때까지
#                 array[j*i] = False  # 소수의 배수는 소수가 아님
#                 j += 1 
#     return array[n]


# def solution(numbers):
#     answer = 0
#     num_list = list(numbers)
#     per = []

#     for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
#         per += list(permutations(num_list, i))        # i개씩 순열조합

#     new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환
#     new_nums = list(set(new_nums))
#     # print(new_nums) # 만들 수 있는 모든 수가 출력됨

#     for num in new_nums:
#         if num < 2:
#             continue
#         if is_prime_number(num):
#             answer += 1

#     return answer

from itertools import permutations


def solution(numbers):
    answer = []
    nums = [n for n in numbers]  # numbers를 하나씩 자른 것
    per = []
    for i in range(1, len(numbers) + 1):  # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))  # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]  # 각 순열조합을 하나의 int형 숫자로 변환

    for n in new_nums:  # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:  # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True
        for i in range(2, int(n ** 0.5) + 1):  # n의 제곱근 보다 작은 숫자까지만 나눗셈
            if n % i == 0:  # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)  # 소수일경우 answer 배열에 추가

    return len(set(answer))  # set을 통해 중복 제거 후 반환
