import sys
from copy import deepcopy

input = sys.stdin.readline

result = []

pattern = '08??840'
day_hours = 4
work_hours = 24

amount_hours = 0
for p in pattern:
    if 48 <= ord(p) <= 57:
        amount_hours += int(p)

diffs = work_hours - amount_hours


def logic(pat, idx, diff, dh):
    # Base Condition
    if idx == len(pat):
        if diff == 0:
            result.append(pat)
        return

    # Recursion logic
    if pat[idx] == '?':
        for i in range(dh):
            if i == 0:
                print('a')
            buf = deepcopy(pat)
            pat[idx] = str(i)

            # 재귀 시작
            logic(pat, idx + 1, diff - int(i), dh)

            # 복구하자
            pat = deepcopy(buf)

    else: # 물음표가 아닌 경우
        logic(pat, idx + 1, diff, dh)


logic(list(pattern), 0, diffs, day_hours)
# print(result)

for r in result:
    print(*r)
