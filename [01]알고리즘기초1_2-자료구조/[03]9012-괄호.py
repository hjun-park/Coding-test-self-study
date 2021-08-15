import sys

N = int(input())

'''


'''

'''
    2021-07-26
    [시작 체크 리스트]
    V     15분 지났으나 발상 불가 또는 아예 다른 길
          코드 50% 정도 완성
          30분 보다 더 걸려서 코드 완성
          코드는 다 돌아가는데 효율성에서 걸림
          코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
    V       완벽히 이해함

    [첨언]

'''

'''

'''

for _ in range(N):
    ps_list = list(map(str, input()))
    # print(ps_list)
    result = 0 # 괄호 개수가 0이 안 된다면 제대로 된 괄호가 아님

    for ps in ps_list:
        if ps == "(":
            result += 1
        elif ps == ")":
            result -= 1

        if result < 0:
            print('NO')
            break

    if result > 0:
        print('NO')
    elif result == 0:
        print('YES')
