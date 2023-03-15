import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = []

# 핵심 : 삼각형 세 변 길이 조건 생각
# 가장 긴 변의 길이는 두 변의 합보다 같거나 작아야 한다.
# C < A + B

for _ in range(N):
    graph.append(int(input().rstrip()))

graph.sort(reverse=True)

flag = False
for i in range(len(graph) - 2):
    if graph[i] < graph[i + 1] + graph[i + 2]:
        print(graph[i] + graph[i + 1] + graph[i + 2])
        flag = True
        break

if not flag:
    print(-1)
