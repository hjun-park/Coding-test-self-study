import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(input().split()) for _ in range(N)]

dic = {"-1": 0, "0": 0, "1": 0}


def logic(r, c, n):
    if n == 1:
        dic[graph[r][c]] += 1
        return

    # 전체 탐색하면서 다른게 나오는 순간 9개로 쪼개기
    for i in range(r, r + n):
        for j in range(c, c + n):
            if graph[r][c] != graph[i][j]:
                logic(r, c, n // 3)
                logic(r, c + n // 3, n // 3)
                logic(r, c + (n // 3 * 2), n // 3)
                logic(r + n // 3, c, n // 3)
                logic(r + n // 3, c + n // 3, n // 3)
                logic(r + n // 3, c + (n // 3 * 2), n // 3)
                logic(r + (n // 3 * 2), c, n // 3)
                logic(r + (n // 3 * 2), c + n // 3, n // 3)
                logic(r + (n // 3 * 2), c + (n // 3 * 2), n // 3)
                return

    # 모두 다 같은 종이라면 첫 시작지 값에 해당하는 종이만 += 1
    dic[graph[r][c]] += 1
    return


logic(0, 0, N)

print(dic["-1"])
print(dic["0"])
print(dic["1"])
