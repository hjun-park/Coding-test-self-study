import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

# 무한으로 초기화
graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

# 자기 자신 지나가는 루프는 0으로 변경 ( 플로이드 돌면서 갱신되지 않게 위함 )
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 문제의 핵심, 중복된 경로에서 짧은 경우가 입력받을 수 있어서
# 조건체크 후 갱신할 지 말지를 결정해야 한다.
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 플로이드-워셜 알고리즘

# 1) 1번부터 N번까지 대입하면서 중간에 거치게 함
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=' ')
    print()
