from itertools import combinations


def find_prime_number(N):
    arr = [True] * (N + 1)

    for i in range(2, len(arr) // 2 + 1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False

    return [x for x in range(2, N+1) if arr[x]]


def solution(nums):
    _sum = sum(nums)
    _len = len(nums)

    primes = find_prime_number(_sum)

    cnt = 0
    for p in list(combinations(nums, 3)):
        if sum(p) in primes:
            cnt += 1

    return cnt


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
print(solution([0, 1, 2]))
