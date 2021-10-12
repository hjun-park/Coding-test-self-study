import sys

input = sys.stdin.readline

i = 0
while True:
    i += 1
    L, P, V = map(int, input().split())

    if L+P+V == 0:
        break

    rest = min(V % P, L)     # 남은 일수(V%P)가 캠핑장 이용 할 수 있는 일 수(L일)보다
                             # 예를 들면 남은 일수가 3일인데 캠핑장 이용 가능한 날은 3일 중 2일 경우
    use = V // P * L

    print(f'Case {i}: {rest + use}')
