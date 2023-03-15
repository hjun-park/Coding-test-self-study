import sys

input = sys.stdin.readline


# 연속된 수의 합으로 N을 만들기 위한 방법
# 1) 1부터 N까지 수에서 홀수 중에서도 N과 나눠서 나머지가 0인 수들을 세면 표현식이 나온다.
def solution(n):
    return len([x for x in range(1, n + 1, 2) if n % x == 0])


print(solution(15))
print(solution(4))
print(solution(8))
