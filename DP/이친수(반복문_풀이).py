import sys

'''
    2021-06-30
    [시작 체크 리스트]
            15분 지났으나 발상 불가 또는 아예 다른 길
            코드 50% 정도 완성
            30분 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
    V       코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
      V     완벽히 이해함

    [첨언]

'''

'''
    [접근]
        - 규칙을 찾아 점화식을 세운 후 재귀로 작성
'''

n = int(input())
d = [0] * (n+1)

for i in range(1, n+1):
    if i == 1:
        d[i] = 1
    elif i == 2:
        d[i] = 1
    else:
        d[i] = d[i-1] + d[i-2]

print(d[n])
