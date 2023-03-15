import sys

input = sys.stdin.readline

N = int(input().rstrip())
kits = list(map(int, input().split()))
mid = sum(kits) // N
same = [mid] * N
cnt = 0


def spread(L, R):
    print(f'kitsL = {kits[L]} , kitsR = {kits[R]}')
    global cnt
    if kits[L] > kits[R]:
        print(f'L > R')
        v1 = kits[L] - mid
        v2 = mid - kits[R]

    elif kits[L] < kits[R]:
        print(f'L < R')
        v1 = kits[R] - mid
        v2 = mid - kits[L]

    else:
        return

    print()
    diff = v1 if v1 <= v2 else v2
    print(f'v1 = {v1}, v2 = {v2}, diff = {diff}')

    cnt += abs(L - R) * diff
    print(f'cnt는 {cnt}')

    kits[L] = kits[L] - diff if kits[L] > kits[R] else kits[L] + diff
    kits[R] = kits[R] + diff if kits[L] > kits[R] else kits[R] - diff

    print(kits)


print(f'중간값 = {mid}')
is_left_small = False
while True:
    for i in range(N):
        print()
        print()
        print(f'i = {i}에서의 시도')
        if kits[i] < mid:
            # print(f'{kits[i]}를 찾음')
            for j in range(i + 1, N):
                # print(f'{kits[j]}를 찾음')
                if kits[j] > mid:
                    spread(i, j)
                    break

        if kits[i] > mid:
            for j in range(i + 1, N):
                if kits[j] < mid:
                    spread(i, j)
                    break

    else:
        if kits == same:
            break
        else:
            continue

print(cnt)
print(kits)






# # import sys
# import time
#
# # input = sys.stdin.readline
#
# while True:
#     ins = input()
#     if ins == '':
#         break
#     else:
#         print(f'ins = {ins} 0.5초 대기')
#         time.sleep(0.5)
#
