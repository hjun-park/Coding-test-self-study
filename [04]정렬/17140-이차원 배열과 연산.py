import sys
from collections import Counter

input = sys.stdin.readline

r, c, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(4)]


def rc():
    max_len = 0
    len_graph = len(graph)
    for j in range(len_graph):  # 한 행을 순회

        # 0을 배제 후 재 정렬하는 작업
        a = [i for i in graph[j] if i != 0]  # 0의 경우 미리 배제
        a = Counter(a).most_common()  # 배제 후 각 숫자가 몇 개 있는지 센다 (리턴: 딕셔너리)
        a.sort(key=lambda x: (x[1], x[0]))  # 딕셔너리를 value먼저 이후 key 기준으로 정렬한다.
        graph[j] = []  # 행을 초기화한다.

        # key는 value개 이런 식으로 집어넣는다.
        for key, value in a:
            graph[j].append(key)
            graph[j].append(value)
        len_a = len(a)
        # 길이가 가장 큰 가로길이를 구한다. ( key, value 쌍이기 때문에 2를 곱했나 ? - 더 크게해도 통과된다. )
        if max_len < len_a * 2:
            max_len = len_a * 2

    # 가장 길이가 큰 행에 맞춰주기 위해 비어있는 부분은 0을 채워준다.
    # 100을 넘어가는 경우 100까지만 표기한다.
    for j in range(len_graph):
        for k in range(max_len - len(graph[j])):
            graph[j].append(0)
        graph[j] = graph[j][:100]


for i in range(101):
    try:
        if graph[r - 1][c - 1] == k:
            print(i)
            break
    except:
        pass

    # 열의 크기가 더 큰 경우는 행열을 바꿔서 진행
    if len(graph) < len(graph[0]):
        graph = list(zip(*graph))  # zip을 이용하면 행과 열 바꿀 수 있음
        rc()
        graph = list(zip(*graph))
    else:
        rc()

else:  # for문 바로 아래 if에 대한 else
    print(-1)
