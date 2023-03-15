# 이번 문제의 핵심은
# 2번 정렬을 하면 시작시간을 정렬할 뿐만 아니라 동일 시작시간 내 가장 빨리 끝나는 시간을 알 수 있다는 점

n = int(input())
s = []

# 개수만큼 입력을 받아 순서 쌍으로 저장
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

# 회의시작 시간 기준으로 정렬
s = sorted(s, key=lambda a: a[0])

# 회의 끝 시간 기준으로 정렬 ( 시작과 끝 정렬을 해 주어야 같은 시작 시간에 따라서 세부정렬이 가능하다 )
s = sorted(s, key=lambda a: a[1])

last = 0
cnt = 0

# 정렬된 s 순서쌍 배열에서 하나씩 빼고 ( X, Y )
# 당장 앞에 있는 이득만 챙겨보는 알고리즘
for i, j in s:
    if i >= last:   # 시작 시간 >= 이전에 끝나는 시간보다 크거나 같을 경우 (( 이 경우가 교체 가능한 시간 ))
        cnt += 1    # 카운트
        last = j    # 끝나는 시간을 Y로 지정

print(cnt)

