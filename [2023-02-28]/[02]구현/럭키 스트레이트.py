import sys

n = list(map(int, sys.stdin.readline().rstrip()))

mid = len(n)//2

left = 0
right = 0

for a in range(mid):
    left += n[a]

for b in range(mid, len(n)):
    right += n[b]

if left == right:
    print("LUCKY")
else:
    print("READY")



