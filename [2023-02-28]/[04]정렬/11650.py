import sys

# 입력받음
N = int(sys.stdin.readline())
coordinate = []     # 좌표 입력받을 리스트

for i in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

# x[0]에 대해서 먼저 정렬 후 x[1]에 대해서 정렬
coordinate.sort(key=lambda x: (x[0], x[1]))

# 출력
for i in coordinate:
    print(i[0], i[1])
