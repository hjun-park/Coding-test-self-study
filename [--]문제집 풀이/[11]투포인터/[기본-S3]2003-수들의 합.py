import sys

input = sys.stdin.readline

'''
    [요약] - https://github.com/encrypted-def/basic-algo-lecture/blob/master/0x14/solutions/2003.cpp
    1. N개의 수열 존재
    2. i부터 j까지 합이 0이 되는 경우의 수 출력
    
    [풀이] - 각 인덱스마다 누적합이 담겨있는 prefix sum을 이용하는 방법 이용 
    0. 구간합에서는 무조건 prefix sum을 이용함
     - index 0은 0으로 초기화
     - 나머지는 각 리스트에 대해 누적합으로 담겨있음
    1. left, right = 0, 0
    2. right가 N 이하까지 루프 시작
    2-1. M보다 작으면 right 증가
    2-2. M과 같으면 카운트 증가 후 right 증가
    2-3. M보다 크다면 left 증가
'''

N, M = map(int, input().split())
prefix = [0] + list(map(int, input().split()))

# 0) prefix sum을 구함 (prefix는 기존 입력의 맨 앞에 0번 인덱스 추가)
# prefix의 N번째는 N번째가지의 합이 담겨 있음
for i in range(1, N + 1):
    prefix[i] += prefix[i - 1]

left, right = 0, 0
cnt = 0

# 2) right가 N이하까지 투포인터 루프 수행
while right <= N:  # '<'가 아닌 'N'인 이유는 prefix의 길이가 N이 아니라 N+1이라서
    # print(left, right)
    _sum = prefix[right] - prefix[left]

    # 2-1) _sum이 M과 같으면 cnt 증가
    if _sum == M:
        cnt += 1

    # 2-1) M보다 작거나 같으면 right 증가
    if _sum <= M:
        right += 1

    # 2-2) M보다 크면 left 증가
    if _sum > M:
        left += 1

print(cnt)
