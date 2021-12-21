import sys

input = sys.stdin.readline

N, M = map(int, input().split())
books = list(map(int, input().split()))
steps = 0

# 0) Sorting
books.sort()

# 1) Partitioning
plus = []
minus = []
max_value = 0
for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(book)

    # 가장 큰 값 설정 ( 마지막 책은 놓고나서 돌아올 필요가 없기 때문에 가장 큰 값을 마지막에 놓으려고 함 )
    if abs(book) > abs(max_value):
        max_value = book

# 양수 - 내림차순, 음수 - 오름차순
plus.sort(reverse=True)
minus.sort()

distances = []
for i in range(0, len(plus), M):  # 세준이는 M개씩 들 수 있으므로 M개씩 체크
    if plus[i] != max_value:  # 마지막 수만 넣지 않도록 하기
        distances.append(plus[i])

for i in range(0, len(minus), M):  # 세준이는 M개씩 들 수 있으므로 M개씩 체크
    if minus[i] != max_value:  # 마지막 수만 넣지 않도록 하기
        distances.append(minus[i])

answer = abs(max_value)  # 마지막 수는 편도만 더하기
for i in distances:  # 그 이외의 수들은 갔다와야하니 *2 를 곱한다.
    answer += abs(i * 2)

print(answer)
