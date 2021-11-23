import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(N)]

check = min(N, M)  # 정사각형은 가로세로가 같기 때문에 길이는 최솟값으로 지정

'''
    1) 행에 해당하는 N을 순회
    2) 열에 해당하는 M을 순회
    3) 정사각형의 사이즈 ( 행,열이 0부터 시작하듯이 정사각형 K도 0부터 시작)
    4) 조건체크:  
      4-1) 범위체크: i + k < N and j + k < M 
      4-2) 꼭짓점 체크: graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]
    5) 조건에 만족한다면 정답과 최댓값 비교 후 (K+1)^2 크기를 넣어줌 (K가 0부터 시작하므로) 
'''

answer = 0
for i in range(N):
    for j in range(M):
        for k in range(check):
            if (i + k) < N and (j + k) < M and (
                    graph[i][j] == graph[i][j + k] == graph[i + k][j] == graph[i + k][j + k]):
                answer = max(answer, (k + 1) ** 2)

print(answer)
