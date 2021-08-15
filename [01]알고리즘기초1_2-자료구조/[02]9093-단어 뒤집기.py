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

N = int(input())

for _ in range(N):
    word_list = list(map(str, sys.stdin.readline().rstrip().split()))

    for word in word_list:
        print(word[::-1], end=' ')
