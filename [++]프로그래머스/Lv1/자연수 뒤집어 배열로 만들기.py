def solution(n):
    r = []
    for num in str(n)[::-1]:
        r.append(int(num))

    return r
