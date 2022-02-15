import sys

input = sys.stdin.readline

N, M = map(int, input().split())
is_used = [False] * (N + 1)
arr = [0 for _ in range(M)]

'''
 백트래킹 로직 - 중복 없이
 
1) def logic(n)

2) base condition
if n == M:
    print(' '.join(map(str, arr))
    
    
3) logic

'''


def logic(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    start = 1   # 시작지점 존재
    if k != 0:
        start = arr[k-1]+1

    for i in range(start, N + 1):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            logic(k + 1)
            is_used[i] = False


logic(0)
