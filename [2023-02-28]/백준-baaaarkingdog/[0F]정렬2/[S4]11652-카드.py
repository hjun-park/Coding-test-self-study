from collections import Counter

N = int(input().rstrip())
print(sorted(Counter([int(input().rstrip()) for _ in range(N)]).items(), key=lambda x: (-x[1], x[0]))[0][0])
