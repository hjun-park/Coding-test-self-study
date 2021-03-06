import sys

n = int(input())

'''
    2021-06-29
    [시작 체크 리스트]
            1시간 지났으나 발상 불가 또는 아예 다른 길
            코드 50% 정도 완성
            1시간 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
      V     코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
      V     완벽히 이해함

    [첨언]
      - DP문제는 이전 값의 상관관계를 잘 살펴보고 점화식을 작성하기
      - 상관관계 규칙을 잘 살펴보면 점화식과 코드는 쉽게 작성됨

'''

'''
    [접근] 각각의 수에 대해서 1, 2, 3으로 만드는 경우의 수
    2x1 = 1개
    2x2 = 2개
    2x3 = 3개
    2x4 = 5개 ( (2x2개수) + (2x3개수) )
    
    d[n] = d[n-2] + d[n-1]

'''

d = [0] * (n + 1)


def logic(x):
    if x == 1:
        return 1
    if x == 2:
        return 2

    if d[x] != 0:
        return d[x]

    d[x] = logic(x - 2) + logic(x - 1)

    return d[x] % 10007


print(logic(n))
