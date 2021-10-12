import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input().rstrip())

# DP로 접근하는 것이 아닌, 파사노 주기를 이용해서 푸는 문제
