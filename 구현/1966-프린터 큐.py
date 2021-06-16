import sys

n = int(input())

while n > 0:    # 테스트케이스가 끝날 때까지 반복
    n -= 1
    N, M = map(int, sys.stdin.readline().split())
    pri_q = list(map(int, sys.stdin.readline().split()))    # 문서 우선순위
    check = [0 for _ in range(N)]                           # 문서 번호(순서대로)
    check[M] = True    # 원하는 문서의 위치 표시                   # 내가 알고 싶은 문서 (1)로 체크

    count = 0
    while True: # 원하는 위치의 문서가 프린트 될 때까지 진행
        if pri_q[0] == max(pri_q):  # FIFO 첫 요소가 최대 우선순위를 가진다면 출력할 순서이다.
            count += 1  # 프린트 횟수 증가
            if check[0]:   # 알고 싶은 문서 위치가 프린트 된다면
                print(count)    # 몇 번째로 프린트되는지 출력하고 나가기
                break

            else:   # 알고 싶은 문서가 아니라면 그냥 출력하고 제거
                pri_q.pop(0)
                check.pop(0)
        else:   # FIFO 첫 요소가 최대 우선순위가 아니라면 맨 뒤로 집어넣는다.
            pri_q.append(pri_q.pop(0))  # 뒤에 넣어준다.
            check.append(check.pop(0))   # 뒤에 넣어준다.
