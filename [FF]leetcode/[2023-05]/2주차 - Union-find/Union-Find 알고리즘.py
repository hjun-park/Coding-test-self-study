# union-find
import sys

input = sys.stdin.readline

# 노드, 간선
v, e = map(int, input().split())


# 4. find 연산
def find(x):
    # 1. 루트 노드가 아니라면 계속해서 찾는다.
    if x != parent[x]:
        # 1. 경로 압축하여 시간복잡도 단축
        parent[x] = find(parent[x])
    return parent[x]


# 3. union 연산
## 두 원소가 속한 집합을 합친다.
def union(x, y):
    # 1. 각 노드의 부모를 찾음
    x = find(x)
    y = find(y)

    # 2. x와 y 중에 더 큰 루트노드가 더 작은 노드를 가리키게 한다.
    # # x보다 y가 더 크다면 y의 부모를 x의 부모로 설정한다.
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 1. 초기화
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

# 2. 간선의 개수만큼 union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union(a, b)

# 5. 각 원소가 속한 집합
for i in range(1, v + 1):
    print(find(i), end=' ')

print()

# 6. 부모 테이블 내용 출력
for i in range(1, v + 1):
    print(parent[i], end=' ')

