import sys

input = sys.stdin.readline

'''
 토너먼트 번호 규칙 ( 2로 나눈 몫을 계속해서 빼준다. )
 8 -> 4 -> 2 -> 1 -> 1
 9 -> 5 -> 3 -> 2 -> 1
'''

N, kim, lim = map(int, input().split())
count = 0

while kim != lim:
    kim = kim - (kim // 2)
    lim -= lim // 2
    count += 1
print(count)
