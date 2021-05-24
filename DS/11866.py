from collections import deque

N, K = map(int, input().split())
s = deque([])

for i in range(1, N+1):
    s.append(i)
print('<', end='')
while s:
    # 해당 K 요소를 pop
    for i in range(K-1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    # 아직 값이 남아 있을 경우
    if s:
        print(', ', end='')
print('>')