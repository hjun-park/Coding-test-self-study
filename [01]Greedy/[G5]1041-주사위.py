import sys

input = sys.stdin.readline

N = int(input().rstrip())
dices = list(map(int, input().split()))

rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}



