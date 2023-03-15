import sys

input = sys.stdin.readline

N = int(input().rstrip())

d = [0] * (N + 7)
p, t = [0], [0]

for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(N, 0, -1):
    if N < i + t[i] - 1:
        d[i] = d[i + 1]
        continue

    d[i] = max(p[i] + d[i + t[i]], d[i + 1])

print(d[1])

'''
d[i] = N
 - i일에 상담을 시작하면 얻을 수 있는 최대 수익

제한조건
 1) 상담에 필요한 일수가 퇴사일을 넘어가는 경우
  -> d[i+1] 반환 ( 다음 날 상담 진행 시 얻을 수 있는 최대 수익 )

문제풀이
 - dp를 구하되, 뒤에서부터 구한다.
  1) 오늘 상담을 진행하는 경우 -> d[i + t[i]] + p[i]  // 오늘 상담하고 요구하는 상담일이 지난 후에 얻을 수 있는 최대 수익
  2) 오늘 상담을 하지 않는 경우 -> d[i+1] // 다음 날부터 상담 진행 시 얻을 수 있는 최대 수익  
'''
