import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

# 요소가 0부터 시작함
parent = [i for i in range(n + 1)]


def union(a, b):
    a = find(a)
    b = find(b)

    # 집합의 여부만 구분하기 때문에 부등호가 바뀌어도 상관 없음
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find(x):
    if x == parent[x]:  # 자신 값이 부모라면 그대로 반환
        return x

    # 경로 압축법
    parent[x] = find(parent[x])
    return parent[x]


for _ in range(m):
    flag, x, y = map(int, input().split())

    if flag:
        if find(x) == find(y):
            print("YES")
        else:
            print("NO")
    else:
        union(x, y)
