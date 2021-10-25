import sys

input = sys.stdin.readline

'''
    메모리초과
     -> https://claude-u.tistory.com/449 // 해당 솔루션
'''


N = int(input())
k = int(input())
graph = [[i * j for j in range(1, N + 1)] for i in range(1, N + 1)]
sorted_graph = []

for i in range(N):
    for j in range(N):
        sorted_graph.append(graph[i][j])


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if mid == target:
            print(sorted_graph[mid])
            return
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1


binary_search(1, N**2, k)
