import sys
sys.setrecursionlimit(10000)

'''
    2021-07-01
    [시작 체크 리스트]
            15분 지났으나 발상 불가 또는 아예 다른 길
            20-30분 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
    V       코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
    V       완벽히 이해함

    [첨언]
     

'''

'''
    [접근]
        문제에 정답이 다 나와 있으며, DP, 재귀형식으로 풀이
'''

t = int(input().strip())
d = [0] * 68


def logic(x):
    global d
    if x < 2:
        return 1

    if x == 2:
        return 2

    if x == 3:
        return 4

    if d[x] != 0:
        return d[x]

    d[x] = logic(x - 1) + logic(x - 2) + logic(x - 3) + logic(x - 4)

    return d[x]


for _ in range(t):
    n = int(input().strip())
    print(logic(n))
