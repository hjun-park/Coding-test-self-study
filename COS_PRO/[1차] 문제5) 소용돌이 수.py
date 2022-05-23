# https://edu.goorm.io/learn/lecture/17299/cos-pro-1%EA%B8%89-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-python/lesson/839015/1%EC%B0%A8-%EB%AC%B8%EC%A0%9C5-%EC%86%8C%EC%9A%A9%EB%8F%8C%EC%9D%B4-%EC%88%98-python
def solution(n):  # n: nxn 	return : 수의합
    answer = 0

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    arr = [[0] * n for _ in range(n)]

    x, y = 0, 0
    d = 0

    # 달팽이 배열 만들기
    for i in range(1, n * n + 1):
        arr[x][y] = i

        if not (0 <= x + dx[d] < n and 0 <= y + dy[d] < n) or arr[x + dx[d]][y + dy[d]]:  # 범위 내가 아니거나 이동지역에 이미 숫자가 있다면
            d = (d + 1) % 4
            x += dx[d]
            y += dy[d]

        else:
            x += dx[d]
            y += dy[d]

    for i in range(n):
        answer += arr[i][i]

    return answer


if __name__ == '__main__':
    n1 = 3
    ret1 = solution(n1)

    print("solution 함수의 반환 값은", ret1, "입니다.")

    n2 = 2
    ret2 = solution(n2)

    print("solution 함수의 반환 값은", ret2, "입니다.")
