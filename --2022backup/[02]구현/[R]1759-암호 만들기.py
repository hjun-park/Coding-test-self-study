import sys

input = sys.stdin.readline

L, C = map(int, input().split())  # L 길이 C 문자 수
words = list(map(str, input().split()))
words.sort()
graph = []
visited = [False] * C

# https://velog.io/@kimdukbae/BOJ-1759-%EC%95%94%ED%98%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python


# 문자열을 체크하여 모음의 개수를 반환
def check_m(string):
    count = 0

    for s in string:
        if s in 'aeiou':
            count += 1

    return count


def dfs(graph, v, idx):
    # 기능 1) 자음 2개 이상, 모음 1개 이상 여부 체크하여 출력
    if v == L:
        if check_m(graph) >= 1 and len(graph) - check_m(graph) >= 2:
            print(''.join(graph))
            return

    # 기능 2) dfs 백트래킹 순회
    for i in range(C):
        if idx < i:
            if not visited[i]:
                graph.append(words[i])
                dfs(graph, v + 1, i)
                # 방문 완료 후 해체 처리
                visited[i] = False
                graph.pop()

dfs([], 0, -1)
