import sys

input = sys.stdin.readline

G = int(input().rstrip())
P = int(input().rstrip())

graph = [int(input().rstrip()) for _ in range(P)]

'''
    https://mygumi.tistory.com/246
    1) 크루스칼 알고리즘과 비슷함 그 중에서도 union-find
     - union-find: 두 노드가 같은 집합에 있는지 판별
     - 노드 간 간선을 이어준다고 생각
'''

parent_gate = [x for x in range(G + 1)]


def find(g):
    if parent_gate[g] == g:
        return g

    parent_gate[g] = find(parent_gate[g])
    return parent_gate[g]


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parent_gate[rootB] = rootA
    else:
        parent_gate[rootA] = rootB


answer = 0
for g in graph:
    find_g = find(g)  # 도킹하려는 게이트의 부모게이트를 찾음
    if find_g == 0:  # 0이라면 최고 부모 게이트이므로 더 올라갈 곳이 없음
        break

    answer += 1  # 도킹이 가능하기 때문에 +1
    union(find_g - 1, find_g)  # 그 다음 도킹할 다음 순서게이트인 find_g-1 과 연결

print(answer)
