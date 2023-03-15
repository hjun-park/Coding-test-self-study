import sys

input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 구현할 것
'''
    https://deok2kim.tistory.com/8
    
    1) 90도 회전(열에 대해서 확인하기 위함)
    2) 행에 대해서 경사로인지 체크
'''


def check_level(array):
    is_slope = [False] * N
    idx = 0
    now_level = array[idx]

    while idx < N - 1:
        before_level = now_level
        idx += 1
        now_level = array[idx]

        if now_level == before_level:  # 높이가 서로 같은 경우
            continue
        elif now_level < before_level - 1:  # 이전 높이보다 2칸 이상 작은 경우
            return 0
        elif now_level == before_level - 1:  # 이전 높이보다 1칸 작은 경우 경사로 설치
            if N - idx < L:  # 경사로를 놓을 수 없는 경우
                return 0

            for i in range(L):  # L만큼 순회하여 경사로를 놓는다.
                if array[idx + i] == now_level and not is_slope[idx + i]:
                    is_slope[idx + i] = True
                    continue
                else:
                    return 0

            else:
                idx += i
                now_level = array[idx]

        # 현재가 두 칸 이상 클 때
        elif now_level > before_level + 1:
            return 0

        # 현재가 한 칸 더 클 때
        elif now_level == before_level + 1:
            if idx < L:  # 거꾸로 놓을 때 초반 인덱스 부족하지 않은지 확인
                return 0

            for i in range(L):
                if array[idx - i - 1] == before_level and not is_slope[idx - i - 1]:
                    is_slope[idx - i - 1] = True
                    continue
                else:
                    return 0

            # 경사로를 뒤로 지었으므로 인덱스를 건널 필요 없다.

    return 1


cnt = 0
for i in range(N):
    cnt += check_level(graph[i])  # 행
    cnt += check_level([row[i] for row in graph])  # 열

print(cnt)
