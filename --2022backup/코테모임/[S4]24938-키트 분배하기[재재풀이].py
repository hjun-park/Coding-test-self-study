import sys

input = sys.stdin.readline

N = int(input().rstrip())
kits = list(map(int, input().split()))
avg = sum(kits) // N

# print(f'평균 = {avg}')
moved = 1
cnt = 0
for i in range(N):
    # print(f'i = {i}')
    # 1. avg 와 현재 위치의 값이 같으면 continue
    if kits[i] == avg:
        continue

    # 3. avg 보다 현재 값이 크면 그만큼 오른쪽으로 옮김
    # - 그 의미는 need 값을 구하고 need 만큼 오른쪽으로 옮기라는 의미
    # - 어차피 선형으로 하는 것이므로 오른쪽으로 옮기게 되면
    # - 이동횟수가 더 늘어나는거나 마찬가지 이다.

    if kits[i] > avg:
        # print(' >> swap')
        # moved += 1
        kits[i], kits[i + 1] = kits[i + 1], kits[i]
        cnt += 1


    # 3. (2)번 함수 돌고 여기도 돎 avg 보다 현재 값이 작으면 오른쪽에서 그만큼 가져옴
    #     ㄴ 가져올 때 오른쪽이 음수가 되는 경우 상관 없음
    if kits[i] < avg:
        need = avg - kits[i]
        # print(' >> 빼기')
        kits[i] += need
        kits[i + 1] -= need
        cnt += (need * moved)
        # moved = 1


    print(f'움직인 이후 = {kits}')
    print(f'카운트 = {cnt}')

print(cnt)

'''
6
55 1 1 1 1 1

6
1 1 1 1 1 55

6
1 1 1 1 55 1

(18)
6 
4 3 2 3 4 2
-> 카운트 2 + 1 = 3

6
13 1 1 1 1 1
'''
