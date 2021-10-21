import sys

input = sys.stdin.readline

N = int(input().rstrip())
tips = []
for _ in range(N):
    tips.append(int(input().rstrip()))

max_tip = 0
tips.sort(reverse=True)

for i in range(len(tips)):
    tip = tips[i] - i
    if tip > 0:
        max_tip += tip

print(max_tip)
