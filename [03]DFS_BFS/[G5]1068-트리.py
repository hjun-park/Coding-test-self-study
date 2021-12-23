import sys

input = sys.stdin.readline


def dfs(del_num, nodes):
    nodes[del_num] = -2  # -1은 문제에서 root 노드로 쓰이므로 삭제할 노드는 -2로 사용
    for i in range(len(nodes)):  # 리프노드에서는 for문이 돌지 않음
        if del_num == nodes[i]:  # 부모노드 순회, 삭제할 부모노드 찾기
            dfs(i, nodes)  # 배열 전체를 탐색하면서 나머지것들도 지움


N = int(input())
nodes = list(map(int, input().split()))
del_num = int(input())

dfs(del_num, nodes)
count = 0

# 지워지지 않은 리프 노드를 셈
# 리프노드는 nodes에 값으로 존재하지 않음 (부모노드만 존재함)
for i in range(len(nodes)):
    if nodes[i] != -2 and i not in nodes:
        count += 1
print(count)
