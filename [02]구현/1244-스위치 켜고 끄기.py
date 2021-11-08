import sys

input = sys.stdin.readline

N = int(input().rstrip())
switch = list(map(int, input().split()))  # 1부터 시작
S = int(input().rstrip())
student = [list(map(int, input().split())) for _ in range(S)]  # 성별, 받은 수

# 1) 남학생: 자기 배수에 해당하는 스위치 번호 변경
'''
2) 여학생: if 스위치번호 == 자기 수
 then check(앞, 뒤) 대칭되는 것끼리 모두 변경
'''
'''
8
0 1 0 1 0 0 0 1
1
1 3
'''


def NH(number):
    global switch

    for i in range(1, (len(switch) // number) + 1):
        if switch[(number * i) - 1] == 1:
            switch[(number * i) - 1] = 0
        else:
            switch[(number * i) - 1] = 1


def YH(number):  # 여학생의 경우 투포인터 이용

    # 처음 한 자리는 직접 비교
    if switch[(number - 1)] == 0:
        switch[(number - 1)] = 1
    else:
        switch[(number - 1)] = 0

    # 투포인터 이용 (배열은 0부터 시작하고 현재값이 number - 1 이라서 number -2, number 설정)
    left = number - 2
    right = number

    # left, right를 하나씩 늘려가며 대칭되는 스위치가 같은 경우
    while 0 <= left and right < N and switch[left] == switch[right]:
        if switch[left] == 0:
            switch[left], switch[right] = 1, 1

        elif switch[left] == 1:
            switch[left], switch[right] = 0, 0

        left -= 1
        right += 1

        # 범위 체크
        if left < 0 or right >= N:
            break


for s in student:
    gender, num = s[0], s[1]

    if gender == 1:
        NH(num)
    else:
        YH(num)

cnt = 0
ans = ''
for i in range(N):
    ans += (str(switch[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0

# 남은 것 프린트
if len(ans) != 0:
    print(ans)
