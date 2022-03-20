import sys

input = sys.stdin.readline

'''
 1) 게임판을 상하좌우로 기울이기
  - 각 행마다 독립적으로 시행 
 2) 5번 기울이는 각각의 방향을 정하기
  - 
'''

N = int(input().rstrip())
graph1 = [list(map(int, input().split())) for _ in range(N)]  # 원본 보드
graph2 = [[0] * N for _ in range(N)]  # 실제 기울임에 따라 값을 바꾸는 보드

''' 1) 게임판을 상하좌우로 기울이기 
 - 새 배열을 만들기(tilted)
   [1] tilted[idx] == 0  -> 비어있는 곳이니 새롭게 집어넣음 
   [2] tilted[idx] != 0 && tilted[idx] == arr[i]  
     -> 비어있지 않으면서도 밀어넣으려는 것과 동일 (=합치기 가능), 2배로 불린다.
   [3] tilted[idx] != 0 && tilted[idx] == arr[i]
     -> 비어있지 않지만 밀어넣는 수와는 다름 (=합치기 불가), 다음 인덱스에 집어넣는다
     
    index ++ 
'''


# 2) 게임판을 90도 시계방향으로 회전 후 기울임
def tilt(d):
    # 2-1) 0, 90, 180, 270도 게임판을 상하좌우로 회전한다.
    for _ in range(d):
        rotate()
    # while True:
    #     if d == 0:
    #         break
    #     rotate()
    #     d -= 1

    # 2-2) 그 다음 숫자들을 정해진 방향으로 모아준다.
    for i in range(N):
        tilted = [0] * N
        idx = 0
        for j in range(N):
            if graph2[i][j] == 0:  # 비어있으면 continue
                continue
            if tilted[idx] == 0:  # 집어넣기 가능
                tilted[idx] = graph2[i][j]
            elif tilted[idx] == graph2[i][j]:  # 집어넣기 && 합치기 가능
                tilted[idx] *= 2
                idx += 1
            else:  # 집어넣기 가능 but 합치기 불가
                idx += 1
                tilted[idx] = graph2[i][j]

        # 2-3) 모은 결과를 반영한다.
        for j in range(N):
            graph2[i][j] = tilted[j]


def rotate():
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = graph2[i][j]

    for i in range(N):
        for j in range(N):
            graph2[i][j] = tmp[N - 1 - j][i]


max_block = 0

for t in range(1024):
    # 1-1) 매번 시행 시마다 보드를 복사함
    for i in range(N):
        for j in range(N):
            graph2[i][j] = graph1[i][j]

    # 1-2) 5번 기울이기 (즉, 기울이다 = 한쪽으로 몰아서 합치는 과정을 말함)
    brute = t
    for i in range(5):
        direction = brute % 4
        brute //= 4
        tilt(direction)

    # 3) 가장 큰 블록이 무엇인가 찾음
    for i in range(N):
        for j in range(N):
            max_block = max(max_block, graph2[i][j])

print(max_block)
