import sys

input = sys.stdin.readline

'''
    문제 아이디어: S에서 T를 찾아가기 위해 많은 시간이 걸리지만,
                T에서 S를 찾아가는 데에는 적은 시간이 걸린다.
'''

S = list(input().rstrip())
T = list(input().rstrip())

while len(S) != len(T):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)
