# 좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
moves = {
    'L': 0,
    'U': 1,
    'R': 2,
    'D': 3
}


def solution(dirs):
    x, y = 5, 5
    road = set()

    for d in dirs:
        nx = x + dx[moves[d]]
        ny = y + dy[moves[d]]

        if 0 <= nx < 11 and 0 <= ny < 11:
            road.add((x, y, nx, ny))
            road.add((nx, ny, x, y))  # 출발도착 반대여도 같은 간선이므로 예외처리 위해 집어넣음
            x, y = nx, ny

    return len(road) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
