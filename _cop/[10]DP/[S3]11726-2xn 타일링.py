import sys

input = sys.stdin.readline

n = int(input().rstrip())

'''
1) dp 함수
d[i] = N
    - 2xi 크기에 1x2, 2x1 타일로 채우는 경우의 수
2) 점화식 설정
d[0] = 0
d[1] = 1 (2x1)
d[2] = 2 (1x2 2 // 2x1 2) 
d[3] = 3 (1x2 1x2 2x1)
d[4] = 5
d[5] = 8

d[i] = (d[i-1] + d[i-2] % 10_007
'''
d = [0] * (n + 2)

d[1] = 1
d[2] = 2


def logic():
    if n < 2:
        return

    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 10_007


logic()
print(d[n])
