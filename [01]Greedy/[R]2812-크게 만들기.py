import sys

n, k = map(int, input().split())
numbers = list(sys.stdin.readline().rstrip())

# 1. k개 삭제하여 가장 큰 수를 만들어야 함
for _ in range(k):
    max_value = max(numbers)


# 0부터 len(array)-k 까지 순회하며 max를 찾음
# max의 index값부터 시작해서 다음 값을 찾음,
# 만약 같은 값이라면 그 앞의 값을 추출할 것
#
