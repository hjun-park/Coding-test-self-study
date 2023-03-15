import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))
M = int(input().rstrip())
B = list(map(int, input().split()))

'''
  [구하고자 하는 것]
  B 리스트 값이 A 리스트에 존재하는지 확인
'''

for b in B:
    try:
        A.index(b)
        print(1)
    except ValueError:
        print(0)
        continue
