import sys

input = sys.stdin.readline

N, M = map(int, input().split())
is_used = [False] * (N + 1)
arr = [0 for _ in range(M)]


def logic(k):
    if k == M:
        print(' '.join(map(str, arr)))
        return

    start = 1
    if k != 0:  # k가 0이 아니라면 그 다음값으로 갱신 ( 중복되는 값 제거 위함 )
        start = arr[k - 1]

    # (2)문제와 유사하지만 여기서는 is_used 체크 안 함으로써 끝 값 중복 가능
    for i in range(start, N + 1):
        arr[k] = i
        logic(k + 1)


logic(0)
