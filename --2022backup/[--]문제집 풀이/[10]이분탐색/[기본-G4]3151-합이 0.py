import sys
from collections import Counter

input = sys.stdin.readline

N = int(input().rstrip())
A = sorted(list(map(int, input().split())))
cnt = Counter(A)  # Counter({-4: 2, 2: 2, -6: 1, -5: 1, 0: 1, 1: 1, 3: 1, 7: 1})
result = 0

'''
    [요약] https://ryu-e.tistory.com/29
    1. 대회참가는 3인 1팀
    2. 코딩 실력과 팀워크는 반비례
    3. 합이 0이 되는 3인조를 만드는 경우의 수를 구하기
    
    [풀이] - 투포인터를 이용함 ( 변수가 3개다 보니 left를 조금 특이한 위치에 잡음 )
     --> 값이 3개인 경우에 대한 적절한 값을 탐색하는 문제
    1. 입력된 코딩 실력 리스트 sort
    2. enumerate를 돌면서 left(i+1), right(N-1) 설정하고 조정
    3. sum이 0이면서 left, right 같은 경우라면 right-left 해서 같은 값들은 모두 더해주기
       -> 마지막 연산에는 left 조정
    4. sum이 크고 작음에 따라 left, right 조정
'''

# 학생을 1명씩 돌린다.
for i, a in enumerate(A):
    left, right = i + 1, N - 1

    while left < right:  # 투포인터는 <= 가 아니라 <
        _sum = A[i] + A[left] + A[right]

        if _sum == 0:
            # left와 right이 같은 경우 같은 값임을 의미, 갯수만큼 카운트
            if A[left] == A[right]:
                result += right - left

            else:  # 다를 경우 몇 개인지 모르니 cnt 참고하여 카운트
                result += cnt[A[right]]
            left += 1

        elif _sum < 0:  # 0보다 작은 경우 left 조정
            left += 1

        elif _sum > 0:  # 0보다 큰 경우 right 조정
            right -= 1

print(result)
