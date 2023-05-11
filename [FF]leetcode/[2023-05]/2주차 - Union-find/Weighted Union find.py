import sys

input = sys.stdin.readline
'''
첫째 줄에 
$n$, 
$m$이 주어진다. 
$m$은 입력으로 주어지는 연산의 개수이다. 다음 
$m$개의 줄에는 각각의 연산이 주어진다. 합집합은 
$0$ 
$a$ 
$b$의 형태로 입력이 주어진다. 이는 
$a$가 포함되어 있는 집합과, 
$b$가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 
$1$ 
$a$ 
$b$의 형태로 입력이 주어진다. 이는 
$a$와 
$b$가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
'''

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

NO
NO
YES
'''


# x에 대한 부모를 찾는 함수
def find(x):
    # 음수라면 부모노드를 의미
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])  # 경로압축
    return parent[x]


# 두 그래프를 합치는 함수 (같은 부모를 바라보게끔 트리구조를 합친다.)
def merge(a, b):
    # 1. 각각의 부모를 찾는다.
    a = find(a)
    b = find(b)

    # 2. 부모가 같다면 둘은 같은 트리에 속함
    if a == b:
        return

    # 3. 부모가 다를 시 높이가 낮은 트리가 높은 트리 아래로 들어가야 한다. (안 그러면 더 깊어짐)
    if parent[a] < parent[b]:  # 높이는 음수로 표현되기 때문에, 작은 값이 더 높은 트리다.
        parent[a] += parent[b]  # b가 a의 아래로 들어갔기 때문에 a는 b 높이만큼 더 높아진다.
        parent[b] = a  # b의 부모를 a로 설정
    else:
        parent[b] += parent[a]
        parent[a] = b


n, m = map(int, input().split())

# 1. 부모 초기화
parent = [0] * (n + 1)

# 2. 부모 초기화
# # weight union에서 음수는 높이를 표현
# # 양수는 부모 노드가 누군지 표현
# # 즉, 최상위 부모노드는 음수일 것이고 이외 노드는 부모가 존재하므로 양수이다.
for i in range(1, n + 1):
    parent[i] = -1

nodes = [list(map(int, input().split())) for _ in range(m)]

for node in nodes:
    c, a, b = node

    if c == 0:
        merge(a, b)

    elif c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
