import sys
from collections import deque

input = sys.stdin.readline

'''
 핵심: 이분탐색으로 중량 mid값 찾은 후 해당 값으로 start -> end 갈 수 있는지 체크
 1) 인접행렬 생성
 2) start, end, min, max 정하기 (문제에 나와있음)
 3) 이분탐색 진행 (중간 mid값을 BFS에 집어넣고 시작)
 4) BFS 통해서 end까지 갈 수 있는지 확인 ( 갈 수 있으면서 무게제한에 걸리지 말아야 함)
 5) 만약 BFS로 갈 수 있다면 True 리턴, 아니라면 False
 6) 이분탐색 BFS에서 True결과가 나오면 max_weight에 mid값을 반영, 아니라면 반영하지 않음
     -> 반영을 했다면 start = mid + 1
     -> 반영을 하지 않았다면 end = mid -1
'''

N, M = map(int, input().split())  # 섬의 개수, 다리 개수
bridge = [[] for _ in range(N+1)]

for _ in range(M):  
    A, B, C = list(map(int, input().split()))
    bridge[A].append([B, C])
    bridge[B].append([A, C])

# bridge = [list(map(int, input().split())) for _ in range(M)]    # A, B 섬 사이 중량 C인 다리
start, end = map(int, input().split())


result = -1

min_weight = 1
max_weight = 1000000000


def bfs(weight):
    visited = [False] * (N + 1) # 여러번 탐색할 경우 안에다 만들어주기
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        x = q.popleft()

        if x == end:
            return True

        for y, w in bridge[x]:
            if not visited[y] and weight <= w:
                q.append(y)
                visited[y] = True

    return False


def binary_search(start, end):
    global result

    while start <= end:
        mid = (start + end) // 2

        if bfs(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1


binary_search(min_weight, max_weight)
print(result)
