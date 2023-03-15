moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def logic(place):
    for i in range(len(place)):
        place[i] = list(place[i])

    for x in range(5):
        for y in range(5):
            # 1) 자기 자신 원소가 P일 때 상하좌우에 P가 없다.
            if place[x][y] == 'P':
                for dx, dy in moves:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == 'P':
                            return 0

            # 2) 자기 자신 원소가 O일 때 상하좌우 원소에 P가 1개 이하
            elif place[x][y] == 'O':
                cnt = 0
                for dx, dy in moves:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if place[nx][ny] == 'P':
                            cnt += 1

                if cnt > 1:
                    return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(logic(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
