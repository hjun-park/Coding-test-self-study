import string

tmp = string.digits + string.ascii_lowercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def solution(n):
    n = convert(n, 3)
    n = str(n[::-1])

    return int(n, 3)


print(solution(45))
print(solution(125))

