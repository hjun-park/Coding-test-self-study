import sys
from collections import deque
from math import sqrt

input = sys.stdin.readline

'''
    출처 : https://cijbest.tistory.com/13
'''

# 에라토스테네스의 체
def find_prime(M, N):
    arr = [True for _ in range(N + 1)]

    for i in range(2, int(sqrt(N)) + 1):
        if arr[i]:
            j = 2
            while i * j <= N:
                arr[i * j] = False
                j += 1

    # return [x for x in range(M, N + 1) if arr[x]]
    return arr


def bfs(start, end):
    visited = [False] * 10001
    visited[start] = True

    q = deque()
    q.append((start, 0))

    while q:
        num, cnt = q.popleft()

        if num == end:
            return cnt

        str_num = str(num)

        for i in range(4):  # 4자리 순회
            for j in range(10):  # 0부터 9까지 순회
                temp = int(str_num[:i] + str(j) + str_num[i + 1:])

                if not visited[temp] and prime[temp] and temp >= 1000:
                    visited[temp] = True
                    q.append((temp, cnt + 1))


T = int(input())
# 소수 판별 배열
prime = find_prime(0, 10000)
find_prime(0, 10000)
for _ in range(T):
    start, end = map(int, input().split())

    result = bfs(start, end)

    print(result if result is not None else "Impossible")
