import sys

'''
    오답 : 솔루션 : https://huidea.tistory.com/127
    
    배운 점
        1) 이차원 배열 입력방법  
        2) 이차원 배열 값 접근방법
        3) brute forcing
'''


def main():
    wb_list = []
    X, Y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(X):
        wb_list.append([i for i in sys.stdin.readline().rstrip()])

    real_min_cnt = 1e9
    # 8x8 사이즈 순회 가능한 만큼 순회하기
    for row in range(X - 7):
        for col in range(Y - 7):
            # 2차원 배열이기 때문에 row로 접근하고 그 row에서 col 인덱스로 접근하면 하나씩 접근하게됨
            # wb_list[row][col] 이런 식으로 접근
            sliced_matrix = [x[col:col + 8] for x in wb_list[row:row + 8]]
            min_cnt = isBW(sliced_matrix)
            real_min_cnt = min(min_cnt, real_min_cnt)
    return real_min_cnt


def isBW(matrix):
    w_need_to_switch = 0
    b_need_to_switch = 0

    # 시작점(0, 0)이 W인 경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 != 0) and (y % 2 != 0)):  # 행 짝수, 열 짝수 / 행 홀수, 열 홀수
                if matrix[x][y] != "W":  # W가 아니라면
                    w_need_to_switch += 1  # 바꿔줘야하므로 카운터 셈

            elif ((x % 2 != 0) and (y % 2 == 0)) or ((x % 2 == 0) and (y % 2 != 0)):  # 행 홀수, 열 짝수 / 행 짝수, 열 홀수
                if matrix[x][y] != "B":  # B가 아니라면
                    w_need_to_switch += 1  # 바꿔줘야하므로 카운터 셈

    # 시작점(0, 0)이 B"인 경우
    for x in range(8):
        for y in range(8):
            if ((x % 2 == 0) and (y % 2 == 0)) or ((x % 2 != 0) and (y % 2 != 0)):  # 행 짝수, 열 짝수 / 행 홀수, 열 홀수
                if matrix[x][y] != "B":  # W가 아니라면
                    b_need_to_switch += 1  # 바꿔줘야하므로 카운터 셈

            elif ((x % 2 != 0) and (y % 2 == 0)) or ((x % 2 == 0) and (y % 2 != 0)):  # 행 홀수, 열 짝수 / 행 짝수, 열 홀수
                if matrix[x][y] != "W":  # B가 아니라면
                    b_need_to_switch += 1  # 바꿔줘야하므로 카운터 셈

    return min(w_need_to_switch, b_need_to_switch)


print(main())
