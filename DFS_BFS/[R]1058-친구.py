import sys
from collections import deque

'''
  2-친구
  - 서로 친구인 경우
  - 제 3자가 있는데 A의 친구이면서 B의 친구여야 함

  # 플로이드 워셜 알고리즘이 필요 ( O(N^3) )
  1) N과 그래프를 입력받은 후, 0으로 구성된 2차원 방문리스트 생성
  2) N을 3번 돈다. (i, j, k)
  3) j와 k가 같다면 continue ( 동일인물은 서로 친구가 될 수 없음 ) 
  4) [j][k]가 친구(Y)이거나 [i][j], [i][k] 한 번 건너가 서로 친구라면
    방문리스트 값을 1로 셋팅

  result = 0     # 결과값
  5) 루프 탈출 후 visited(2차원)를 돌면서 1차원 행 총값의 최댓값 찾음
   
'''

N = int(input())
graph = []
visited = [[0] * N for _ in range(N)]

for _ in range(N):
    graph.append(list(map(str, input())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue

            if graph[j][k] == 'Y' or (graph[i][j] == 'Y' or graph[i][k] == 'Y'):
                visited[j][k] = 1   # 둘은 친구


result = 0

for visit in visited:
    result = max(result, sum(visit))

print(result)
