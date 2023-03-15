import sys

input = sys.stdin.readline

N = int(input().rstrip())
dice_info = [list(map(int, input().split())) for _ in range(N)]

'''
    # 브루트포싱 문제 (https://velog.io/@yoonkeem/BOJ-2116%EB%B2%88-%EC%A3%BC%EC%82%AC%EC%9C%84-%EC%8C%93%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
    
'''

# 1) 주사위 아랫면에 따라 결정된 윗면 dictionary
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
result_list = []

# 2) 맨 아래 첫 번째 주사위를 각각 다른면이 나오게 6번 for문 순환
for i in range(6):  # 맨 아래 주사위는 자유자재로 굴리는 것이 가능
    max_list = []
    dice = [1, 2, 3, 4, 5, 6]

    # 3) 주사위의 아랫면과 이를 마주보는 윗면을 결정하고 제거
    bottom = dice_info[0][i]  # 첫 번째 주사위 아랫면
    top = dice_info[0][rotate[i]]  # 아랫면에 따라 결정된 1번 주사위 윗면

    dice.remove(bottom)
    dice.remove(top)

    # 4) 옆면들 중 가장 큰 주사위 눈을 max_list 추가
    max_list.append(max(dice))

    # 5) 나머지 주사위 순환 (두번째 ~ 마지막)
    for j in range(1, N):
        dice = [1, 2, 3, 4, 5, 6]

        # 6) 주사위 아랫면 결정 후 제거
        bottom = top  # N번째 주사위 아랫면은 N-1번째 주사위 윗면과 같아야 함
        dice.remove(bottom)  # 그렇게 결정된 bottom은 옆면이 될 수 없기에 제거

        # 7) 현재 주사위 윗면도 결정 후 제거
        top = dice_info[j][rotate[dice_info[j].index(bottom)]]
        dice.remove(top)

        # 8) 옆은 자유자재로 회전할 수 있으므로 최댓값을 넣어줌 ( top, bottom 빠진 상태 )
        max_list.append(max(dice))

        # 그렇게 하면 max_list 에는 각 주사위별 옆면 최댓값이 하나하나 들어가게 된다.

    # 각 횟수마다 구해져 나온 옆면 최댓값 합들 중 가장 큰 수를 선택한다.
    result_list.append((sum(max_list)))

print(max(result_list))
