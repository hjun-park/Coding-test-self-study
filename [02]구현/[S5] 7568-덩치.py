n = int(input())
data = []

for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

# 한 사람 당 n-1번씩 전수조사
for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:  # 자기보다 키도 크고 덩치가 크면 증가
            rank += 1
    print(rank, end=' ')
