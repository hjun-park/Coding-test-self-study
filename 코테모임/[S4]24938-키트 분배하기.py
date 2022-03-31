import sys

input = sys.stdin.readline


N = int(input().rstrip())
kits = list(map(int, input().split()))
_len = len(kits)
eq = sum(kits) // _len
eq_list = [eq for _ in range(N)]

pos = 0
before_index = 0

def i_am_min(pos):

    if kits[pos - 1] <= kits[pos + 1]:
        kits[pos] += 1
        kits[pos + 1] -= 1

    elif kits[pos - 1] > kits[pos + 1]:
        kits[pos] += 1
        kits[pos - 1] -= 1

    # 같은 경우
    else:
        pass


is_reverse = False
cnt = 0
while True:
    # 균등분배 되었는지 확인

    if kits == eq_list:
        print(cnt)
        sys.exit(0)

    before_index = pos
    pos = kits.index(max(kits))

    print(f'이전 = {kits}')
    print(f'pos = {pos}')
    if pos == 0:
        kits[pos] -= 1
        kits[pos + 1] += 1

    elif pos == _len - 1:
        kits[pos] -= 1
        kits[pos - 1] += 1

    else:  # 양쪽 중 더 작은 애들을 대상으로 연산
        # pos 랑 이전 인덱스랑 똑같으면 반대로 하기
        is_reverse = False
        if pos == before_index:
            if kits[pos-1] - kits[pos] == 1 and kits[pos+1] - kits[pos] == 1:
                pos = kits.index(max(kits))
                i_am_min(pos)
                print('리버스트루')
                continue

            # is_reverse = True

        if kits[pos - 1] <= kits[pos + 1]:
            print('aaaa')

            kits[pos] -= 1

            # if is_reverse:
            #     kits[pos + 1] += 1
            # else:
            kits[pos - 1] += 1

        elif kits[pos - 1] > kits[pos + 1]:
            print('bbbbb')
            kits[pos] -= 1

            # if is_reverse:
            # kits[pos - 1] += 1
            # else:
            kits[pos + 1] += 1

        # 같은 경우
        else:
            pass

    print(f'키트 결과 = {kits}')
    # print(f'카운트증가')
    cnt += 1
