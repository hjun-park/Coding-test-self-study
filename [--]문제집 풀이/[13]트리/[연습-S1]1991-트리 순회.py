import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())
graph = defaultdict(list)


def pre_order(start):  # BFS 순회
    if start != '.':
        print(start, end='')  # root
        pre_order(graph[start][0])  # left
        pre_order(graph[start][1])  # right


def in_order(start):
    if start != '.':
        in_order(graph[start][0])  # left
        print(start, end='')  # root
        in_order(graph[start][1])  # right


def post_order(start):
    if start != '.':
        post_order(graph[start][0])  # left
        post_order(graph[start][1])  # right
        print(start, end='')  # root


# A가 루트
for _ in range(N):
    root, left, right = input().split()

    # root에 L, R 추가
    graph[root].append(left)
    graph[root].append(right)

pre_order('A')
print()

in_order('A')
print()

post_order('A')
print()
