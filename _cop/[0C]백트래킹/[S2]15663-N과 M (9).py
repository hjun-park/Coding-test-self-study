import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
nums = sorted(list(map(int, input().split())))
is_used = [False] * N


def func(k):
    if len(arr) == M:
        print(*arr)
        return

    before = 0
    for i in range(N):  # 인덱스로 수 접근
        if not is_used[i] and before != nums[i]:  # 이전 수와 지금 수가 같으면 중복
            is_used[i] = True
            arr.append(nums[i])
            before = nums[i]  # 중복된 수열 출력을 막기 위해 이전 수 저장
            func(i)
            arr.pop()
            is_used[i] = False


func(0)
