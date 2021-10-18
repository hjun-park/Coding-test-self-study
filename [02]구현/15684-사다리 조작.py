import sys

input = sys.stdin.readline

# 세로선 N개에 가로선 M개이며 가로점선은 H개가 있다.
N, M, H = map(int, input().split())

row_line = [[False] * N for _ in range(H)]  # 가로선 있는지 체크하는 함수

# 구현할 내용
# 1) i번 -> i번 잘 갔는지 체크
# 2) 3개까지 가로선을 놓는 함수

'''
    더 간결한 코드: https://velog.io/@kimdukbae/BOJ-15684-%EC%82%AC%EB%8B%A4%EB%A6%AC-%EC%A1%B0%EC%9E%91-Python
'''


'''
    백트래킹 DFS를 이용하는 문제
     - 가로선이 3개가 될 때까지 놓고 하나 제거하고 다른데 두고 이런 식으로 문제를 풀어나간다.
     
     1) 입력
     2) M이 0인 경우 i 출발 -> i 도착 형태이므로 0 출력, 종료
     3) 두 좌표를 입력받은 후 해당 좌표는 방문 체크한다. ( 입력값은 처음이 1인 경우이므로 -1 해주기 )
     4) answer = 4 초기화 후 dfs 순회하기 ( 만약 answer가 4 넘으면 -1을 출력하도록 하기 )
     
     dfs 순환부분
     1) [검증파트]
     1-1) check() 수행 True라면 answer과 cnt 값 중 최소로 설정
     1-2) cnt가 3이거나 answer보다 작으면 볼 이유도 없으니 반환
     2) [백트래킹]
     2-1) 가로선 우선 탐색하는데(H) 행이 변경된 경우 가로선을 처음부터 탐색
        -> if i==x: k = y     // else: k = 0
     2-2) 세로열 탐색,
       -> 만약 해당 자리가 not visited (가로선 없는 경우) 그래서 가로선 놓았는데 -가 존재하지 X 경우
            -> 가로선을 놓았는데 왼쪽에 가로선 존재하는 경우 return ( 이어지면 안됨 )
       -> 가로선 놓기, 
       -> cnt는 증가, 세로선 그대로, 가로선 2증가
       -> 가로선 없애기
     
     check 순환부분
'''


# i번 세로줄이 i번 도착하는지 확인 ( x좌표를 비교해야 함 )
def check():
    for start in range(N):
        k = start
        for j in range(H):
            if row_line[j][k]:  # 가로선이 존재한다면
                k += 1  # 가로선 오른쪽으로 넘어감

            elif k > 0 and row_line[j][k - 1]:  # 가로선이 왼쪽에 존재하는 경우
                k -= 1  # 가로선 왼쪽을 넘어감

        if k != start:  # 시작점이랑 끝점의 열이 다르다면
            return False
    return True


def dfs(cnt, x, y):  # cnt, 세로선 출발점, 가로선 출발점
    global answer

    # i-> i가 가능한 경우
    if check():
        answer = min(answer, cnt)
        return
    elif cnt == 3 or answer <= cnt:  # 3개 이거나 비교 대상이 아닌 경우는 return
        return

    # 행
    for i in range(x, H):  # 가로줄을 먼저 탐색
        if i == x:  # 처음 가로선인 경우
            k = y  # 가로선 계속 탐색
        else:  # 행이 변경된 경우 가로선 처음부터 탐색
            k = 0

        # 열
        for j in range(k, N - 1):
            # 현재 자리에 가로선이 없으면서 그 다음에도 가로선이 없는 경우 가로선을 놓을 수 있으며
            if not row_line[i][j] and not row_line[i][j + 1]:
                # 가로선을 놓았을 때 왼쪽에 가로선이 존재할 경우 가로선을 놓을 수 없음
                if j > 0 and row_line[i][j - 1]:
                    continue

                row_line[i][j] = True
                # 세로선은 그대로, 가로선은 +2
                # +2를 넣어준 이유는 가로선이 2개 이어지면 안 되므로
                dfs(cnt + 1, i, j + 2)
                row_line[i][j] = False  # 가로선 제거


# 가로선이 없으면 i -> i 가능
if M == 0:
    print(0)
    exit(0)

for _ in range(M):
    a, b = map(int, input().split())
    row_line[a - 1][b - 1] = True

answer = 4
dfs(0, 0, 0)
print(answer if answer < 4 else -1)
