import sys

input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
arr = [0 for _ in range(M)]
is_used = [False] * (N + 1)


def logic(k):
    # 출력할 땐 nuber에서 출력한다.
    if k == M:
        for i in range(M):
            print(number[arr[i]], end=' ')
        print()
        return

    # 연산은 arr에서 인덱스로 select 하고
    for i in range(N):
        if not is_used[i]:
            arr[k] = i
            is_used[i] = True
            logic(k + 1)
            is_used[i] = False


logic(0)
