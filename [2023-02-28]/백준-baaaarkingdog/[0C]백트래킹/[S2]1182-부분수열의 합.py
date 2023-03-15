import sys

# sys.setrecursionlimit(10 ** 6)    # 일부의 경우 메모리 초과가 날 수 있다.

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

# 백트래킹 이용
'''
 - 원소의 개수가 N개인 리스트의 부분집합 개수는 2^N,
 - 공집합 빼면 2^N-1개의 부분집합에 대해 합이 S와 일치 하는지 확인
 
1) 함수의 정의 : func(cur, total): 
  - 현재 부분집합의 개수 cur, 현재까지의 전체 합 total
2) base condition
  if cur == N: # 현재 개수가 리스트의 최대 개수라면
    if total == S:  # 부분집합의 합이 S 라면
        cnt += 1
    return
3) recursion logic (거꾸로 더한다. (부분집합 모두 구한 후에 (백트래킹 복구 시) 마지막 수부터 더함)
  func(cur + 1  , total)  # 부분집합의 개수만 증가시킴
  func(cur + 1, total + nums[cur]) # 마지막 수 복구 시에 더해줌

'''

cnt = 0


def func(cur, total):
    global cnt
    if cur == N:
        if total == S:
            cnt += 1
        return

    func(cur + 1, total)    # 수를 더하지 않는 경우
    func(cur + 1, total + nums[cur])    # 수를 더하는 경우 (거꾸로 더해 나감)



func(0, 0)
# 공집합도 합은 0이므로 합이 0을 구하라는 경우에는 1을 빼준다.
print(cnt if S != 0 else cnt - 1)
