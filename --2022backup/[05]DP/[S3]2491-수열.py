import sys

n = int(input().strip())
data = list(map(int, sys.stdin.readline().split()))

ans = 1


def logic(arr):
    global ans
    cnt = 1

    # 모든 수열의 값을 탐색
    for i in range(0, n - 1):
        # 다음 값이 더 크다면 값을 증가시키고 탐색
        if arr[i] <= arr[i + 1]:
            cnt += 1
        else:
            cnt = 1

        # 연속된 값 중에서도 최대값일 경우 값 갱신
        if ans < cnt:
            ans = cnt


logic(data)

# 줄어드는 연속되는 값에 대해서도 계산
logic(data[::-1])
print(ans)

'''
    아래는 위에처럼 하나 인 경우가 아니라 두 가지로 작성한 식
    
cnt = 1
max_l = 1
for i in range(1, N):
    if arr[i-1] >= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if max_l < cnt:
        max_l = cnt

cnt = 1
for i in range(1, N):
    if arr[i-1] <= arr[i]:
        cnt += 1
    else:
        cnt = 1
    if max_l < cnt:
        max_l = cnt
print(max_l)
'''
