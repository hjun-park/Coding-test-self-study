import sys
from collections import deque

input = sys.stdin.readline

''' 참고: https://tmdrl5779.tistory.com/147
  봄:
    1) 나무가 자신 나이만큼 양분먹고 나이 1 증가
    1-1) 나이가 어린 나무부터 양분을 먹으며 양분이 부족하면 죽는다.

    내용:
      - 해당 좌표의 나무 총 개수만큼 반복하면서 양분을 비교한다.
      - 만약 양분보다 나무 나이가 더 많은 경우라면 그 이후것들 모두 dead_tree에 해당 나무를 추가한다.
      - 양분이 나무 나이를 수용할 수 있다면 양분을 나무 나이만큼 빼주고 나무 나이를 +1 증가시킨다. 
       
  여름:
    2) 죽은 나무가 양분으로 변한다 ( 죽은 나무마다 나이를 2로 나눈 값을 추가 )
    
    내용:
      - dead_tree 리스트를 while로 순회하면서 양분graph에 하나씩(pop) //2 한 값을 뽑아서 더해준다.

  가을:
    3) 5의 배수의 나이를 가진 나무가 번식한다. 인접한 8칸에 나이 1인 나무 생성
      - 각 좌표의 나무 개수만큼 순회하면서 5의 배수를 가지면
      - 8번의 dx dy 확인 후 appendleft로 나이 1인 나무 생성 ( 1살이 최소니까 appendleft 사용 )
  
   겨울:
     4) 입력받은 양분 배열만큼 각 칸에 추가한다. 
      - graph에 a를 더한다. 

   구하려는 것: K년이 지난 후 살아 있는 나무 개수
'''

N, M, K = map(int, input().split())

# 겨울에 주는 양분
A = [list(map(int, input().split())) for _ in range(N)]

# 가장 처음에는 양분이 5만큼 있다. (양분의 정보)
graph = [[5] * N for _ in range(N)]

# 그래프에 그냥 나무와 죽은 나무들을 여러 개 담고 싶을 때 통째로 넣어줌
trees = [[deque() for _ in range(N)] for _ in range(N)]
dead_trees = [[list() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def spring_and_summer():
    # 봄
    for i in range(N):
        for j in range(N):
            _len = len(trees[i][j])
            for k in range(_len):
                # 양분보다 나무의 나이가 더 큰 경우는 나무가 죽음
                if graph[i][j] < trees[i][j][k]:
                    for _ in range(k, _len):
                        dead_trees[i][j].append(trees[i][j].pop())
                    break  # 이미 for문으로 끝까지 돌았기 때문에 다음 영역으로 탈출
                else:  # 양분이 나무 나이 수용이 가능하다면 양분 뺀 후에 나이 추가
                    graph[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1

    # 여름
    for i in range(N):
        for j in range(N):
            while dead_trees[i][j]:
                graph[i][j] += dead_trees[i][j].pop() // 2


def fall_and_winter():
    # 가을
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue

                        trees[nx][ny].appendleft(1)

            # 겨울
            graph[i][j] += A[i][j]


for i in range(K):
    spring_and_summer()
    fall_and_winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)
