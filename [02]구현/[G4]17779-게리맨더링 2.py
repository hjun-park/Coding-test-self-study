import sys

input = sys.stdin.readline

''' 출처 : https://dirmathfl.tistory.com/385?category=825041
    1) 브루트포스 문제, 조건 그대로 코드로 옮기면 되는 문제
    2) 조건을 생각하면서 코드로 옮기는 실력이 중요
    
'''


def calculate(row, col, d1, d2):
    global total, answer
    zone = [0] * 5
    # 인덱스에 맞게 1씩 추가
    temp = [[0] * (N + 1) for _ in range(N + 1)]
    temp[row][col] = 5
    # d1 = 2 d2 = 2
    for i in range(1, d1 + 1):
        # (2) 1. 경계 : (x, y), (x+1, y-1), ..., (x+d1, y-d1)
        temp[row + i][col - i] = 5
        # (2) 3번 경계 : (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
        temp[row + i + d2][col - i + d2] = 5

    for i in range(1, d2 + 1):
        # (2) 2번 경계 : (x, y), (x+1, y+1), ..., (x+d2, y+d2)
        temp[row + i][col + i] = 5
        # (2) 4. 경계 : (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
        temp[row + i + d1][col + i - d1] = 5

    # (4) 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    for r in range(1, row + d1):
        for c in range(1, col + 1):
            if temp[r][c] == 5:
                break
            zone[0] += board[r][c]

    # (4) 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    for r in range(1, row + d2 + 1):
        for c in range(N, col, -1):
            if temp[r][c] == 5:
                break
            zone[1] += board[r][c]

    # (4) 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    for r in range(row + d1, N + 1):
        for c in range(1, col - d1 + d2):
            if temp[r][c] == 5:
                break
            zone[2] += board[r][c]

    # (4) 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    for r in range(row + d2 + 1, N + 1):
        for c in range(N, col - d1 + d2 - 1, -1):
            if temp[r][c] == 5:
                break
            zone[3] += board[r][c]

    # (4) 5번 선거구는 전체에서 1-4 선거구를 뺀 값
    zone[4] = total - sum(zone)

    return max(zone) - min(zone)


if __name__ == '__main__':
    N = int(input())
    board = [[]]

    # 인덱스에 맞게 1씩 추가
    # 문제에서의 첫 시작점은 (1, 1)이다.
    for _ in range(N):
        board.append([0] + list(map(int, input().split())))

    # 전체 인구 수를 구한다.
    total = sum(sum(board, []))

    answer = int(1e9)

    # (1)번 조건: 기준점 (x, y)와 경계의 길이 d1, d2를 정한다.
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            for d1 in range(1, N + 1):
                for d2 in range(1, N + 1):
                    # 1번 조건의 조건문 표현 (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
                    # 이외는 for 문에서 필터링된다.
                    if r + d1 + d2 > N:
                        continue
                    if 1 > c - d1:
                        continue
                    if c + d2 > N:
                        continue

                    answer = min(answer, calculate(r, c, d1, d2))

    print(answer)
