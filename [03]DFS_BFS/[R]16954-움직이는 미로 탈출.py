import sys
from collections import deque

input = sys.stdin.readline

# block = []
moves = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1)]
graph = [list(input().rstrip()) for _ in range(8)]

'''
    https://devlibrary00108.tistory.com/310
'''


# for i in range(8):
#     graph.append(list(map(str, input().rstrip())))
#     for j in range(8):
# if graph[i][j] == '#':
#     block.append((i, j))

def bfs(start_x, start_y, time):
    q = deque()
    q.append((start_x, start_y, time))

    while q:
        x, y, time = q.popleft()

        # if x == 0 and y == 7:
        #     return 1

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 8 and 0 <= ny < 8:
                # 해당 초 이후의 위치에서 #을 만나지 않는지 체크하고
                # 해당 초 +1 이후의 위치에서 #을 만나지 않는지 체크
                if not graph[nx - time][ny] == '#' and not graph[nx - time - 1][ny] == '#':

                    # 해당 time 이후 X행 위치가 0보다 작으면 도착한 것으로 간주
                    if nx - time < 0:
                        return 1

                    q.append([nx, ny, time + 1])

    return 0


print(bfs(7, 0, 0))
