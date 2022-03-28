import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = sorted(list(map(int, input().split())))

'''
    [요약]
    - 세 가지 용액을 합쳐서 0에 가까운 용액을 만듦
    - 산성은 (+), 알칼리성은 (-)
    - 출력값은 0에 가장 가까운 용액 3개
    
    [풀이]
    1) 입력 받은 배열 arr 정렬
    2) arr에 대해서 enumerate 순회 + left, right를 지정 (핵심)
    3) 투포인터를 돌면서 _sum을 구하고 0에 가까우면 갱신하고 이후 left, right를 움직임
    
    [주의점]
    1) 문제의 입력범위를 잘 살펴보자 (value를 1e9 -> 1e11로 변경)
'''

A, B, C = 0, 0, 0
value = int(1e11)
for i, e in enumerate(arr):
    left, right = i + 1, N - 1  # 이 부분이 핵심

    while left < right:
        _sum = arr[i] + arr[left] + arr[right]

        if _sum == 0:  # 0에 가깝다면 바로 출력
            print(arr[i], arr[left], arr[right])
            sys.exit(0)

        elif _sum < 0:  # 음수인 경우
            if abs(_sum) < value:  # 0에 더 가깝다면 갱신
                value = abs(_sum)
                A, B, C = arr[i], arr[left], arr[right]

            left += 1

        elif _sum > 0:  # 양수인 경우
            if abs(_sum) < value:  # 0에 더 가깝다면 갱신
                value = abs(_sum)
                A, B, C = arr[i], arr[left], arr[right]

            right -= 1

print(A, B, C)
