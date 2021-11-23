import operator
import sys
from collections import defaultdict

sys.stdin.readline()

monsters = ["Knight 3 10 10 3", "Wizard 5 10 15 1", "Beginner 1 1 15 1"]
character = [10, 5, 2]  # ch, cs, cd

exp_dict = defaultdict(float)


def solution(character, monsters):
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
            mh -= (cs - int(md))
            if mh <= 0:
                exp_dict[name] = int(exp) / time  # 경험치 기록
                break

            # 2) 몬스터 공격
            ch -= (ms - cd)
            if ch <= 0:  # 플레이어 사망
                exp_dict[name] = 0  # 경험치 제로
                break

            # 3) 피 회복
            ch = character[0]

    sorted_dict = sorted(exp_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_dict[0][0]


print(solution(character, monsters))
