import sys

input = sys.stdin.readline

N = int(input().rstrip())

'''
1. dp 함수 정의

2. 점화식 추론

'''

d = [0] * (N + 2)
trace = []

def logic():
    for i in range(2, N + 1):
        d[i] = d[i - 1] + 1
        trace.append(i-1)

        if i % 3 == 0:
            d[i] = min(d[i // 3] + 1, d[i])
            trace.pop()
            trace.append(i//3)
        if i % 2 == 0:
            d[i] = min(d[i // 2] + 1, d[i])
            trace.pop()
            trace.append(i//2)


logic()
print(d[N])
print(*trace)
