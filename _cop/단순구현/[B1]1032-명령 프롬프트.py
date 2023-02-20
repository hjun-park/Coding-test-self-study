import sys

input = sys.stdin.readline

N = int(input().rstrip())
prev = list(input().rstrip())
_len = len(prev)

# 첫 번째 행은 prev로 지정
# 두 번째 행부터 비교하면서 진행
for i in range(N - 1):  # 다음 문자열로 넘어감
    now = list(input())
    for j in range(_len):  # 이전 문자열과 비교
        if prev[j] != now[j]:
            prev[j] = '?'
print(''.join(prev))
