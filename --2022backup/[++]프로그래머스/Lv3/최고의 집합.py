def solution(n, s):
    if s < n:
        return [-1]

    dividend = s // n
    remainder = s % n

    result = [dividend] * n

    for i in range(remainder):
        result[i] += 1

    return sorted(result)
