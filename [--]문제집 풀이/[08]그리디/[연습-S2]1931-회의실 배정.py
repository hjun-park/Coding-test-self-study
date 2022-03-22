import sys

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

'''
 그리디 아이디어 : 끝나는 시간이 빠른 회의부터 선택한다. 
'''
graph.sort(key=lambda x: (x[1], x[0]))

cnt = 0
t = 0  # 끝나는 시간
for i in range(N):
    if t > graph[i][0]:  # 회의가 아직 끝나지 않은 경우
        continue

    cnt += 1  # 회의 수 증가
    t = graph[i][1]  # 회의 진행, 끝나는 시간 기록

print(cnt)
