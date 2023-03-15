import sys

input = sys.stdin.readline

N = int(input().rstrip())
switch = list(map(int, input().split()))  # 스위치 상태
S = int(input().rstrip())
students = [list(map(int, input().split())) for _ in range(S)]  # 성별, 스위치번호 (-1)


def male_student(num):
    i = 1
    while (i * num) - 1 < N:
        if switch[(i * num) - 1] == 0:
            switch[(i * num) - 1] = 1
        elif switch[(i * num) - 1] == 1:
            switch[(i * num) - 1] = 0

        i += 1


def female_student(num):
    left = num - 2
    right = num

    # 처음 한 자리는 직접 바꿔줌
    if switch[(num - 1)] == 0:
        switch[(num - 1)] = 1
    else:
        switch[(num - 1)] = 0

    # 그 다음 대칭부터는 같을 경우에만 바꿔줌
    while 0 <= left and right < N and switch[left] == switch[right]:
        if switch[left] == 0:
            switch[left], switch[right] = 1, 1
        elif switch[left] == 1:
            switch[left], switch[right] = 0, 0

        left -= 1
        right += 1


for student in students:
    if student[0] == 1:
        male_student(student[1])
    elif student[0] == 2:
        female_student(student[1])

result = ''
cnt = 0
for i in range(N):
    result += (str(switch[i]) + ' ')
    cnt += 1

    if cnt == 20:
        print(result)
        result = ''
        cnt = 0

# 20개 출력하고 남은 것 프린트
if len(result) != 0:
    print(result)
