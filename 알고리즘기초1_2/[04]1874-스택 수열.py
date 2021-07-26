import sys

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

n = int(input())
data = []
result = []  # 연산결과를 담을 리스트
count = 0
t_bool = True

# num_list.remove(num_list[0])

for _ in range(n):
    num = int(input())

    # 타겟 넘버가 되기 직전까지 count 증가 + append
    while count < num:
        count += 1
        data.append(count)
        result.append('+')

    # 리스트의 맨 끝과 같다면 pop
    if data[-1] == num:
        data.pop()
        result.append('-')
    else:  # pop을 하지 않았다는 건 다음 연산은 불가능하단 얘기
        t_bool = False
        break

if t_bool is False:
    print('NO')
else:
    for i in result:
        print(f'{i}')

