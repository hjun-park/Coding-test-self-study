import sys

input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())

# 0) 정렬
sensor = sorted(list(map(int, input().split())))

# 1) 집중국이 센서보다 더 많으면 센서마다 설치할 수 있으므로 거리는 0
if K >= N:
    print(0)
    sys.exit(0)

# 2) 인접한 센서 사이의 거리를 dist에 저장한다.
dist = []
for i in range(1, N):
    dist.append(sensor[i] - sensor[i - 1])

# 3) 센서 사이의 거리에 대해 역순으로 정렬한다.
dist.sort(reverse=True)

# 4) 집중국이 K개 이므로 구간을 K-1개로 나눈다. 나누는 방법은 역순으로 정렬된 센서 사이 거리를 K-1개를 빼면 된다.
for i in range(K - 1):
    dist.pop(0)

# 5) 최소합은 그 거리들을 모두 합산한다.
print(sum(dist))
