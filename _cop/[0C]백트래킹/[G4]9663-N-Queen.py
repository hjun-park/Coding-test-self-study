import sys

input = sys.stdin.readline

# 각 행에 퀸은 1개씩 존재할 수밖에 없다. (즉, 행에 대해 생각할 필요가 없다)
# 대신 열과 대각선에 대해 생각해야한다.

N = int(input().rstrip())

graph = [[0 for _ in range(N)] for _ in range(N)]
count = 0

is_used1 = [False] * 40  # (y) 열을 확인
is_used2 = [False] * 40  # (x+y) 왼쪽 아래 -> 오른쪽 위 대각선 확인
is_used3 = [False] * 40  # (x-y+n-1) 왼쪽 위 -> 오른쪽 아래 대각선 확인


# 함수 정의
def logic(cur):  # Queen을 배치한 개수 (행 인덱스 즉, x좌표)
    global count

    # base condition
    if cur == N:  # 각 행마다 퀸을 전부 배치한 경우 방법 수 추가
        count += 1
        return

    # recursion logic
    # 접근이 가능한 지 확인
    '''
     1) (0, 1), (2, 1)이 같은 열에 있는지 확인하려면 y값이 같은지 보면 된다.
     2) (3, 0), (1, 2)과 같은 대각선(좌하<->우상)인지 확인하려면 두 좌표의 x+y가 같은지 확인하면 된다.
     3) (1, 2), (3, 3)과 같은 대각선(좌상<->우하)인지 확인하려면 두 좌표의 x-y가 같은지 확인하면 된다.
        -> 3)의 경우 음수가 나올 수 있으니 x-y+N-1을 해준다.    
    '''

    for i in range(N):  # y좌표를 차례대로 이동
        # 만약 열, 대각선에서 하나라도 놓여있다면 continue
        if is_used1[i] or is_used2[i + cur] or is_used3[cur - i + N - 1]:
            continue

        # 열, 대각선에 아무것도 없다면 방문처리 + 재귀 시작 + 재귀 복구
        is_used1[i] = True
        is_used2[cur + i] = True
        is_used3[cur - i + N - 1] = True
        logic(cur + 1)
        is_used1[i] = False
        is_used2[cur + i] = False
        is_used3[cur - i + N - 1] = False


logic(0)
print(count)
