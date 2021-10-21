import sys

input = sys.stdin.readline

N = int(input().rstrip())
rope_weights = []
for _ in range(N):
    rope_weights.append(int(input().rstrip()))

rope_weights.sort(reverse=True)

for i in range(N):
    rope_weights[i] = rope_weights[i] * (i + 1)

print(max(rope_weights))
