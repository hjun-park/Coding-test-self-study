from sys import stdin

input = stdin.readline

A, B, C = map(int, input().split())
D = int(input().rstrip())

# 3600초 = 60분 = 1시간 // 60초 = 1분

C += (D % 3600) % 60
B += (D % 3600) // 60
A += D // 3600


if C >= 60:
    B += 1
    C -= 60

if B >= 60:
    A += 1
    B -= 60

# 이 부분 바꿈
while A >= 24:
    A %= 24


print(A, B, C)
