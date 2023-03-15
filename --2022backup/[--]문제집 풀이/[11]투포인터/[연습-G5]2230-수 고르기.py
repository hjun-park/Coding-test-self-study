import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input().rstrip()) for _ in range(N)])

'''
    [요약]
    1. 두 수를 골랐을 때 차이가 M 이상이면서 제일 작은 경우 출력
    2. 두 수가 같은 경우일 수 있다.
    
    [풀이]
    1. 입력값에 대한 정렬
    2. left, right 지정 ( left는 0부터 N까지 순서대로 돌 것이고, right는 left 부터 N까지 순회 )
    3, 순회하면서 차이비교 
    3-1. 차이가 M보다 작으면 right를 증가한다.
    3-2. 차이가 M보다 크거나 같다면 diff에 갱신 후 left를 증가시킨다.
    
    [주의점]

'''

left, right = 0, 0
result = int(1e12)

while left < N and right < N:

    # 1) 범위 내면서 차가 M을 넘지 못하는 경우 right만 증가
    if A[right] - A[left] < M:
        right += 1

    # 2) 차이가 M을 넘어가는 순간 반영 후 left 증가
    else:
        result = min(result, A[right] - A[left])
        left += 1

print(result)
