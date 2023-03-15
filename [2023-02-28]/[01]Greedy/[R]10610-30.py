import sys

input = sys.stdin.readline

N = list(input().rstrip())
N.sort(reverse=True)
sum = 0

for i in N:
    sum += int(i)   # 각 자리 수를 더함

if sum % 3 != 0 or "0" not in N:    # 3으로 나누어 떨어지지 않거나 0이 없으면
    print(-1)   # 불가능
else:
    print(''.join(N))
