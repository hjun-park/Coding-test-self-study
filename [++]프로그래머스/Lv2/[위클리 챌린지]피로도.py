# 백트래킹
res = -1  # 최대 던전 횟수


def dfs(cnt: int, k: int, dungeons: list, visited: list):  # 던전 들어간 횟수
    global res
    # base condition
    # -> 피로도가 없어지면 return
    if k <= 0:
        return

    # 던전 들어간 횟수 갱신
    res = max(cnt, res)

    # recursion logic
    for i in range(len(dungeons)):
        # 방문하지 않았으며 최소 피로도 만족
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(cnt + 1, k - dungeons[i][1], dungeons, visited)
            visited[i] = False


def solution(k, dungeons):
    visited = [False] * len(dungeons)

    dfs(0, k, dungeons, visited)

    return res


if __name__ == "__main__":
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))
