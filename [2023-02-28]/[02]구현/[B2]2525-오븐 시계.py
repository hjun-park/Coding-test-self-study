import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input().rstrip())

# 오븐 시간을 60으로 나눔 ( 시와 분으로 분리하기 위해 )
H, M = divmod(C, 60)

A += H  # 오븐 시간에서 '시'는 A에 더함
B += M  # 오븐 시간에서 '분'은 B에 더함

# B는 59를 넘어가면 안 된다.
q, B = divmod(B, 60)
A += q

# A는 23을 초과하면 안 된다.
A %= 24

print(A, B)
