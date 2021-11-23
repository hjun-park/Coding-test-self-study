import operator
import sys
from collections import defaultdict

sys.stdin.readline()

exp_dict = defaultdict(float)

'''
1. 플레이어가 Knight를 공격해 Knight의 체력이 5 - 3 = 2만큼 감소합니다. Knight의 남은 체력은 8입니다.
2. Knight가 플레이어를 공격해 플레이어의 체력이 10 - 2 = 8만큼 감소합니다. 플레이어의 남은 체력은 2입니다.
3. 플레이어가 피해를 모두 회복하여 체력이 다시 10이 됩니다. 
4. 플레이어가 Knight를 공격합니다. Knight의 남은 체력은 6입니다.
5. Knight가 플레이어를 공격합니다. 플레이어의 남은 체력은 2입니다.
6. 플레이어가 피해를 모두 회복하여 체력이 다시 10이 됩니다.
7. 플레이어가 Knight를 공격합니다. Knight의 남은 체력은 4입니다.
8. Knight가 플레이어를 공격합니다. 플레이어의 남은 체력은 2입니다.
9. 플레이어가 피해를 모두 회복하여 체력이 다시 10이 됩니다.
10. 플레이어가 Knight를 공격합니다. Knight의 남은 체력은 2입니다.
11. Knight가 플레이어를 공격합니다. 플레이어의 남은 체력은 2입니다.
12. 플레이어가 피해를 모두 회복하여 체력이 다시 10이 됩니다.
13. 플레이어가 Knight를 공격합니다. Knight의 남은 체력은 0입니다. Knight가 죽으면서 전투가 종료됩니다.
'''


def solution(character, monsters):
    # map(int, "42 0".split())

    character = list(map(int, character.split()))
    ch, cs, cd = character[0], character[1], character[2]

    for monster in monsters:
        time = 0
        name, exp, mh, ms, md = monster.split()

        exp = int(exp)
        mh = int(mh)
        ms = int(ms)
        md = int(md)

        exp_dict[name] = 0

        while True:
            time += 1
            # 1) 플레이어 선 공격
            mh -= (int(cs) - int(md))
            if mh <= 0:
                exp_dict[name] = int(exp) / time  # 경험치 기록
                break

            # 2) 몬스터 공격
            ch -= (int(ms) - int(cd))
            if ch <= 0:  # 플레이어 사망
                exp_dict[name] = 0  # 경험치 제로
                break

            # 3) 피 회복
            ch = character[0]

    sorted_dict = sorted(exp_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_dict[0][0]
