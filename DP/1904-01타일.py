import sys

'''
    2021-07-01
    [시작 체크 리스트]
            15분 지났으나 발상 불가 또는 아예 다른 길
            코드 50% 정도 완성
            30분 보다 더 걸려서 코드 완성
    V       코드는 다 돌아가는데 효율성에서 걸림
            코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
    V       완벽히 이해함

    [첨언]
     - 문제에서 15746으로 나누라는 걸 읽지 않았음, 꼼꼼히 읽기

'''

'''
    [접근]
    d[n] = d[n-2] + d[n-1] 
'''

n = int(input().strip())
d = [0] * 1000001
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 15746

# for i in range(1, n+1):
#     if i == 1:
#         d[i] = 1
#     elif i == 2:
#         d[i] = 2
#     else:
#         d[i] = d[i-2] + d[i-1]

print(d[n])

# def logic(x):
#     if x == 1:
#         return 1
#
#     if x == 2:
#         return 2
#
#     if d[x] != 0:
#         return d[x]
#
#     d[x] = logic(x - 2) + logic(x - 1)
#     return d[x]
# print(logic(n))
