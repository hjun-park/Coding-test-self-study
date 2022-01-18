import sys

input = sys.stdin.readline

# 좌 -> 우 -> 상 -> 하
# query(d, dx)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

'''
    완전탐색, BFS, DP로도 먹히지 않는 문제
    1) 해설: https://blog.naver.com/PostView.naver?blogId=adamdoha&logNo=222539285810&parentCategoryNo=&categoryNo=60&viewDate=&isShowPopularPosts=true&from=search
    2) 코드: https://comdoc.tistory.com/488
'''


def solution(n, m, x, y, queries):
    # 상 / 좌 / 우 / 하
    top = bottom = x
    left = right = y

    # 공을 거꾸로 돌려 가능한 시작점의 범위를 구하면 된다.
    for d, dx in queries[::-1]:
        if d == 0:  # 열 감소, 거꾸로 생각하면 열 증가
            '''
                left != 0의 이유
                 - left 증가 후 right 증가하는 형태로 되어 있는데 
                 - left가 0이라면 right가 증가하면서 영역이 회복된다.
                 - 다른 d에서도 마찬가지다.
                 
                 - 무슨 말이지? 
                 -  d==0 이라면 왼쪽으로 이동 시 판단기준 벽은 0인 상황
                 -  만약 left가 0이라면 즉, left가 벽에 부딪힌 상황이라면
                 -  상대방 변 (left기준은 right)인 right 하나만 움직이면 된다.
            '''
            if left != 0:
                left += dx  # 왼쪽 라인은 dx만큼 오른쪽 이동
                if left > m - 1:  # 왼쪽 라인이 최대치를 벗어난 경우 left는 m-1
                    left = m - 1

            right += dx  # 오른쪽 라인도 마찬가지로 증가
            if right > m - 1:  # 증가 하는데 최대치를 벗어난 경우 right는 m-1
                right = m - 1

        elif d == 1:  # 열 증가, 거꾸로 생각하면 열 감소
            left -= dx    # 열 감소이므로 왼쪽 라인은 dx만큼 왼쪽으로 이동
            if left < 0:  # 왼쪽 라인이 0보다 작게 이동한 경우 left는 0
                left = 0

            if right != m - 1:  # right
                right -= dx    # 오른쪽 라인은 dx만큼 왼쪽으로 이동 (열 감소)
                if right < 0:  # 오른쪽 라인이 0보다 작게 이동한 경우 right는 0
                    right = 0

        elif d == 2:  # 행 감소, 거꾸로 생각하면 행 증가
            if top != 0:  # top이 0이 아니라면 top을 감소
                top += dx
                if top > n - 1:  # 행을 벗어나면
                    top = n - 1

            bottom += dx  # bottom은 증가
            if bottom > n - 1:  # bottom이 행을 넘어서면
                bottom = n - 1

        elif d == 3:  # 행 증가, 거꾸로 생각하면 행 감소
            top -= dx
            if top < 0:
                top = 0
            if bottom != n - 1:
                bottom -= dx
                if bottom < 0:
                    top = 0

        # 각 좌표마다 놓은 공을 모두 떨어트리면 끝
        # 만약 벽을 뚫고 나가버리면 return 0
        if top > n - 1 or bottom < 0 or left > m - 1 or right < 0:
            return 0

    # 그 면적의 개수가 공이 생존 가능한 영역이다.
    return (bottom - top + 1) * (right - left + 1)


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
