import sys

input = sys.stdin.readline

'''
1. 7명의 여학생 
    - depth = 7
2. 이다솜파 최소 4명 => 즉, 백트래킹 하며 임도연파가 4명이 되는 순간 컷

[함수 정의]
def func(depth, ycnt, idx)  - depth, y개수, 사용할 숫자 idx

[배운 점] - https://chelseashin.tistory.com/96
1. 함수 2차원보다는 1차원(arr[25])으로 표현하면 인접 체크를 손쉽게 할 수 있음 (코드가 깔끔해짐)
    y = idx//5
    x = idx%5
   위에처럼 인접체크도 가능
   
   

'''

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
graph = [list(input().rstrip()) for _ in range(5)]
arr = []
visited = [[False] * 5 for _ in range(5)]
result = 0

def check(index):
    # index를 x, y 좌표로 변환 필요


def dfs(depth, ycnt, idx):
    # 1) 임도연파가 4명 이상 혹은 7명까지 채우기에 인덱스가 부족하면 ret [가지치기]

    # 2) Base Condition
    # - depth가 7인 경우 DFS를 통해 연결된 좌표인지 확인(check(arr[0]))
    # # - 첫 번째 좌표를 넘겨주는 이유는 arr에 있는 좌표들이 서로 연결됐는지 check 함수에서 확인하기 위함
    # - check 함수 돌면서 visited에 True 체크를 했을텐데 이를 2차원 합계를 구해서 7개 맞는지 체크 맞다면 result += 1
    # - visited 초기화 후 return

    # 3) recursion
    # a) index를 x, y 좌표로 변환해 준다. (idx//5, idx%5) -> c)과정 분기에서 2차원 좌표 매핑해줄 때 사용
    # b) for문 25번 도는 대신에 arr에 index 추가 후 dfs 순회한다.
    # c) 이 때 dfs는 해당 인덱스에 속한 사람이 임도연파인지 아닌지에 따라 분기하여 dfs를 순회한다.
    # d) dfs 순회 후에는 pop을 이용하여 복구한다.

    # 4) 복구 후에는 다음 영역에서 DFS 수행

dfs(0, 0, 0)
