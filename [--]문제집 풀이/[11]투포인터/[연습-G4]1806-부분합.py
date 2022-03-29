import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

'''
    [요약]
    1. 연속된 수들 중 그 합이 S 이상이 되는 것들
    2. 그것들 중에서도 가장 짧은 것의 길이
    
    [풀이] - 시간초과 
    1. 따로 1개인 경우에 S를 넘는 경우를 찾으면 1 출력 후 종료
    2. 전체 합을 구했을 때 S를 넘지 못하면 0 출력 후 종료 
    3. 투포인터를 조정하며 2개, 3개, 4개 늘려간다. 
    4. 그 중간에 S가 넘게되면 right - left를 통해 값 출력
    
    [풀이]
    1. right와 sum을 잡음 (sum 초기화 이유는 1개만으로도 S를 넘어갈 수 있기 때문에)
    2. 합이 s 이상일 때까지 en을 증가시킨다.
    3-1. 합이 s 이상이라면 min_len에 최소길이를 반영 후 st를 증가.
    3-2. 단순히 en이 N을 넘어선 경우라면 st만 증가시킨다..
    4. min_len이 변경되지 않는 경우 S를 못 넘는 경우이다. 
    
    [주의점]
'''
min_len = int(1e12)
en = 0
_sum = A[0]

for st in range(N):
    # 1) 합을 못 넘은 경우는 en을 증가시킴
    while en < N and _sum < S:
        en += 1

        # 1-1) en 증가시켰을 때 N을 넘어서지 않는경우에만 다음 값을 더함 (누적합)
        if en != N:
            _sum += A[en]

    # 3-2) en이 넘어가는 경우는 break하여 st를 증가시킴
    if en == N:
        break

    # 3-1) 최소길이 반영 후 st증가
    min_len = min(min_len, (en - st) + 1)
    _sum -= A[st]  # st가 증가될 것이므로 머리길이 제외

# 4) S를 못 넘은 경우에 대한 처리
if min_len == int(1e12):
    min_len = 0

print(min_len)
