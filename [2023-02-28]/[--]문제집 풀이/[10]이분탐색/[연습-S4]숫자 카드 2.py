import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().split()))
M = int(input().rstrip())
check = list(map(int, input().split()))

cnt = 0

# =====================================
# 첫 번째 시도 (index 사용)  --> 시간초과
# =====================================
for to in check:
    print(nums.count(to), end=' ')

# ====================================
# 두 번째 (dictionary)
# ====================================
dt = defaultdict(int)

for n in nums:
    dt[n] += 1

for c in check:
    if c in dt:
        print(dt[c], end=' ')  # 있다면 개수를 출력
    else:
        print(0, end=' ')  # 없다면 0을 출력
