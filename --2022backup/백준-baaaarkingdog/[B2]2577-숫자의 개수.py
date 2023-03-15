import sys
from collections import Counter

input = sys.stdin.readline

a, b, c = [int(input().rstrip()) for _ in range(3)]
tot_dict = Counter(list(map(int, str(a * b * c))))

for i in range(10):
    print(tot_dict[i])
