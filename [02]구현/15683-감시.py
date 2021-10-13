import sys

input = sys.stdin.readline


'''
  1) 각 번호별 이동위치
  2)  
'''


N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]


