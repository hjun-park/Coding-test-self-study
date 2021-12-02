import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 국가정수, 금, 은, 동, K는 알고싶은 나라 등수
graph = [list(map(int, input().split())) for _ in range(N)]

graph.sort(key=lambda x: (-x[1], -x[2], -x[3]))

# 국가번호 K의 인덱스를 찾음
index = 0
for i in range(N):
    if graph[i][0] == K:
        index = i

# 찾았다면 정렬된 배열을 검사하면서 인덱스와 같은 값이 있는지 확인하고 있다면
# 그 값에 +1을 더한 값을 출력 ( 그 이후가 같아도 똑같은 등수기 때문 )
for i in range(N):
    if graph[i][1:] == graph[index][1:]:
        print(i + 1)
        break
