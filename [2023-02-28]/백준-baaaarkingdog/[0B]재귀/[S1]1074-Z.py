import sys

n, r, c = map(int, sys.stdin.readline().split())
answer = 0

while n >= 1:
    # NxN 을 2x2로 줄이는 과정
    temp = 2 ** (n - 1)

    if n == 1:
        if (r == 0) and (c == 1):  # 제 2사분면
            answer += 1
        elif (r == 1) and (c == 0):  # 제 3사분면
            answer += 2
        elif (r == 1) and (c == 1):  # 제 4사분면
            answer += 3
        break

    if r < temp <= c:  # 제 2사분면
        answer += temp ** 2
        c -= temp
    elif c < temp <= r:  # 제 3사분면
        answer += (temp ** 2) * 2
        r -= temp
    elif temp <= r and temp <= c:  # 제 4사분면
        answer += (temp ** 2) * 3
        r -= temp
        c -= temp

    n -= 1

print(answer)