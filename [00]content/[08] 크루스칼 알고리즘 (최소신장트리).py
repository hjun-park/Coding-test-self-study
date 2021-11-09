import sys

input = sys.stdin.readline

'''
    크루스칼 알고리즘이란 ?  ( https://velog.io/@kimdukbae/%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Kruskal-Algorithm )
     - 하나의 그래프가 있을 때 모든 노드를 포함하면서도 '사이클'이 존재하지 않아야 함
     - 그래프에서 '사이클'이 존재하지 않는 것은 '트리'의 성립 조건이기도 함
     - 즉, 최소 신장 트리(크루스칼)란 사이클이 존재하지 않으며 비용이 최소인 트리를 말한다.
     
     크루스칼 알고리즘 동작과정
      1) 간선 데이터를 비용에 따라 오름차순 정렬
      2) 간선을 하나씩 확인하면서 사이클을 발생시키는지 확인
        2-1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
        2-2) 사이클이 발생하는 경우 최소 신장 트리 포함 X
      3) 모든 간선에 대해서 2번의 과정을 반복
    
'''

# sample input
# 7 9
# 1 2 29
# 1 6 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25


# 특정 원소가 속한 집합(부모)를 찾기
def find(parent, x):
    if parent[x] == x:  # 자신이 부모라면
        return x
    parent[x] = find(parent, parent[x]) # 부모의 부모를 거치면서 찾음
    return parent[x]


# 두 원소가 속한 집합을 합치기 (간선 연결한다고 생각)
def union(parent, a, b):
    rootA = find(parent, a)    # 이어진 곳의 부모를 찾음
    rootB = find(parent, b)    # 이어진 곳의 부모를 찾음

    # 비용이 가장 적은 쪽이 부모가 되어 연결을 해 줌
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    # 서로 부모가 달라야 사이클이 발생하지 않음
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
