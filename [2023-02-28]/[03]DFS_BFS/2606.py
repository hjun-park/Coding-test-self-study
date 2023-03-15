from collections import deque


'''
    DFS (재귀)로 푼 문제
    출처 : https://dojinkimm.github.io/problem_solving/2019/11/15/boj-2606-virus.html

    import sys
    r = sys.stdin.readline
    
    # 시작점 / 엣지(인접리스트) / 방문리스트
    def dfs(v, egs, ans):
        for i in egs[v]:        # 해당 점의 인접리스트
            if i not in ans:    # 해당 점 방문하지 않았다면
                ans.append(i)   # 방문리스트 추가
                dfs(i, egs, ans) # 해당 점 / 인접리스트 / 방문리스트 재귀
        return ans
    
    
    N = int(r())
    edges = [[] for _ in range(N+1)]
    for _ in range(1, int(r())+1):
        e1, e2 = map(int, r().split())
        edges[e1].append(e2)
        edges[e2].append(e1)
    
    # 시작점 / 엣지(인접리스트) / 방문리스트
    print(len(dfs(1, edges, [1]))-1)    
    
'''

def bfs(graph):
    answer = 0
    visited = {}
    queue = deque([1])  # 1부터 시작

    while queue:
        n = queue.popleft()
        if n not in visited:  # 방문하지 않았다면
            visited.setdefault(n)  # 해당 노드 방문처리
            queue += graph[n]  # 해당 노드와 인접한 행렬들을 모두 큐잉
            answer += 1  # 감염

    # 빠져나왔다면 큐가 비어있는 상태이고 모든 노드를 다 순회했단 얘기
    # return visited, answer    # for debug
    return answer - 1


def dfs(graph):
    answer = 0
    visited = {}

    # 시작점 넣고 시작
    stack = [1]

    while stack:
        n = stack.pop()  # 1. 꺼내고 방문처리 확인
        if n not in visited:  # 2. 방문하지 않았다면 방문리스트 추가 후에 인접한 리스트 모두 push
            visited.setdefault(n)
            print(f"graph {n} : {graph[n]}")
            stack += reversed(graph[n])  # 3. 재귀를 사용하는 방법도 있겠지만 거꾸로 스택에 집어넣으면 간단하게 가능
            answer += 1
    return answer - 1


def func():
    # input
    n = int(input())
    pair = int(input())
    # n, pair = map(int, input().splitlines())
    graph = {i: [] for i in range(1, n + 1)}

    # print(graph)

    for i in range(pair):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    # sorting
    for key in graph:
        graph[key].sort()

    answer = dfs(graph)
    print(answer)


if __name__ == '__main__':
    func()
