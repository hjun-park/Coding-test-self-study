import sys

'''


'''

'''
    2021-07-26
    [시작 체크 리스트]
          15분 지났으나 발상 불가 또는 아예 다른 길
            코드 50% 정도 완성
            30분 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
    V       코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
    V       완벽히 이해함

    [첨언]

'''

'''

'''

data = []

N = int(sys.stdin.readline())


def is_empty_list(data):
    if len(data) == 0:
        return True
    else:
        return False


for i in range(N):
    order = list(map(str, sys.stdin.readline().rstrip().split()))

    if order[0] == "push":
        data.append(order[1])

    elif order[0] == "pop":
        if is_empty_list(data):
            print('-1')
            continue
        print(data.pop())

    elif order[0] == "size":
        print(len(data))

    elif order[0] == "empty":
        if is_empty_list(data):
            print('1')
            continue
        print('0')

    elif order[0] == "top":
        if is_empty_list(data):
            print('-1')
            continue
        print(data[-1])
