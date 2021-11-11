import sys

input = sys.stdin.readline

'''
팁1 :  
    
배운점:
0) 특정 인덱스 값이 몇 번째로 pop이 되는지 체크하는 방법으로써는 visited를 이용하면됨
    M = 1   # 특정 인덱스 값

    q = list(map(int, input().split())) # 프린트 큐 중요도 값
    visited = [False] * len(q)
    q[M] = True 
'''

# 3:45
for _ in range(int(input().rstrip())):
    N, M = map(int, input().split())  # M 몇 번째로 인쇄됐는지 궁금한 문서

    q = list(map(int, input().split()))
    visited = [False] * len(q)

    visited[M] = True

    count = 0
    while True:
        if q[0] == max(q):  # 자신의 출력순서가 찾아오면
            count += 1  # 출력한다.
            if visited[0]:  # 그 출력된 값이 내가 찾는 index 라면
                print(count)  # 출력하고 종료한다.
                break

            else:  # 내가 찾는 index가 아니라면 그냥 출력해준다.
                q.pop(0)
                visited.pop(0)
        else:  # 자신의 출력순서가 아니라면 빼고 다시 집어넣는다.
            q.append(q.pop(0))
            visited.append(visited.pop(0))
