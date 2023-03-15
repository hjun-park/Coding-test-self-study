import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

'''
 # 문제 요약
  1) 팀원 수 제한 X, 1개 팀만, 그리고 1인 팀도 가능하다.
  2) 모든 학생은 같이 플젝할 1명만 선택한다.
  3) 혼자 하려면 자기 자신을 선택한다. 
  4) 자기 자신을 가리키거나 혹은 사이클을 형성해야만 팀이 될 수 있다.
  5) 구하려는 것 : 팀에 속하지 않는 학생 수
 
 # 문제의 핵심
  1) 사이클은 DFS를 이용하여 순환되는 graph를 찾을 수 있다.  
  2) 마지막 node와 첫 node가 이어져서 Loop를 이루는 것을 찾는다.
  
 # 로직
   - 학생 수, graph, visited, result(팀을 이룬 학생들) 생성
   - 1번 학생부터 탐색한다. 
   - 방문하지 않은 경우 탐색 진행하고 탐색하는 경로를 지정할 traced 라는 리스트를 만든다.
     - DFS 순환 시작, 순환 시에는 방문처리 후 traced에 경로를 추가한다. 
     - 다음 방문할 정점을 설정한다. (값을 인덱스로 다시 집어넣으면 그게 다음 방문할 점) 
     - 방문할 정점이 방문된 상태이면서 traced에 있다면 해당 정점부터 사이클이 시작된다는 것이다.
       - 따라서 traced에서 해당 정점 index부터 끝까지가 반복되는 부분이며 그 학생들을 result에 집어넣는다.
     - 방문할 정점이 방문 안 된 상태라면 다시 dfs 탐색
'''


def dfs(v):
    global team_students

    # 3) 시작지는 방문처리 및 탐색 중인 경로 추가
    visited[v] = True
    traced.append(v)

    # 4) 다음 방문할 정점을 설정한다. (시작지를 graph 인덱스로 집어넣으면 됨)
    next = graph[v]

    # 5) 방문할 정점이 방문된 상태이면서 traced에 있다면 거기서부터 사이클이 시작된다는 것이다.
    if visited[next]:
        if next in traced:  # 사이클이 시작되는 구간부터 팀을 이룬다.
            team_students += traced[traced.index(next):]
        return  # 아닌 경우라면 모든 곳을 방문했으므로 return
    # 6) 다음 정점이 방문된 상태가 아니라면 다시 dfs를 순회한다.
    else:
        dfs(next)


for _ in range(int(input().rstrip())):
    # 1) 기본적인 정보 생성
    N = int(input().rstrip())

    # 문제에서 index가 1부터 시작하므로 앞에 0을 붙여주거나 개수를 1개 더 추가해주면 편리하다.
    graph = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N
    team_students = []

    for i in range(1, N + 1):
        # 2) 방문하지 않은 경우만 탐색한다.
        if not visited[i]:
            traced = []
            dfs(i)

    # 7) 그렇게 하면 팀으로 구성된 학생들이 나오고 전체 학생 수에서 해당 학생 수를 빼주면 된다.
    print(N - len(team_students))
