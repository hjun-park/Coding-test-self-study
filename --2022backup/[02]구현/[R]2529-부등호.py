import sys

input = sys.stdin.readline

'''
    https://titanumm.tistory.com/92
    기능 1) 부등호 비교
    기능 2) 백트래킹
'''

min_value = ""
max_value = ""

k = int(input())
A = list(map(str, input().split()))
visited = [False] * 10


def check_ineq(i, j, k):
    if k == '<':
        return i < j
    elif k == '>':
        return i > j


# s: 백트래킹할 문자열
# 1 -> 12 -> 123 이런 순서로 붙음
def bt(depth, s):
    global min_value
    global max_value

    if depth > k:
        if len(min_value) == 0:  # 0이면 값이 없는 상태
            min_value = s
            # print(min_value)
        else:
            max_value = s
        return
    for i in range(10):
        if not visited[i]:
            # 직전에 들어간 값과 앞으로 들어갈 값을 비교
            if depth == 0 or check_ineq(s[-1], str(i), A[depth - 1]):
                visited[i] = True
                bt(depth + 1, s + str(i))
                visited[i] = False


bt(0, '')
print(max_value)
print(min_value)
