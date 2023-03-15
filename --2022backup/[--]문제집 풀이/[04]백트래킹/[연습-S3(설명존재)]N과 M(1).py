import sys

input = sys.stdin.readline

# 해당 문제 시리즈를 풀면 백트래킹 이해에 도움이 됨

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())

is_used = [False] * (N + 1)
arr = [0 for _ in range(M)]


# 백트래킹 (이거 안 쓰면 8중 for문 써야함)
# 백트래킹은 재귀와 같게 base condition이 있어야 한다.
# 이후 재귀 식을 이용하는데, 재귀와 살짝 다른점은 재귀 식에서 다시 자기 자신을 호출한다면
# 그 호출이 끝난 뒤에는 값을 다시 복구해준다.  ( ... (1)참조 )

def logic(k):  # 몇 개 골랐는지
    # base condition
    if k == M:  # M개 전부 고른 경우
        print(' '.join(map(str, arr)))
        return

    # recursion logic
    for i in range(1, N + 1):
        if not is_used[i]:
            # 해당 인덱스에 중복되지 않은 값을 집어넣고 재귀
            arr[k] = i
            is_used[i] = True  # 중복되지 않은 값 중복처리
            logic(k + 1)
            is_used[i] = False  # 다시 복구  ... (1)참조


logic(0)
