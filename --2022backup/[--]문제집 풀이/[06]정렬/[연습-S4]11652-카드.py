import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().rstrip())
tmp = [int(input().rstrip()) for _ in range(n)]
dic = defaultdict(int)

for t in tmp:
    dic[t] += 1

# 딕셔너리도 정렬이 가능하다.
#  -x[1] : -를 붙여서 가장 많이 나온 횟수를 먼저 나오게 정렬
#  x[0] : 이후 같은 횟수인 경우 가장 작은 숫자가 나오게 정렬
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(dic[0][0])
