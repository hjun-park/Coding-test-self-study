import sys

input = sys.stdin.readline

N = int(input().rstrip())

dates = [list(map(int, input().split())) for _ in range(N)]

# 0) 두 조건을 만족하는지 체크한다.



