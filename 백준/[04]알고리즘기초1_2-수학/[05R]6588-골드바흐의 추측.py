import sys

input = sys.stdin.readline

num_list = []

# 입력
while True:
    n = int(input().strip())
    if n == 0:
        break
    num_list.append(n)

# 입력 값 중 가장 큰 값을 담음
max_num = max(num_list)

# 가장 큰 값까지 리스트로 생성 후 1로 셋팅
sosu = [1 for i in range(max_num + 1)]

# 2는 소수이므로 0으로 셋팅
sosu[1] = 0

# 소수만 따로 담을 리스트 생성
only_sosu = []

# 2부터 해서 에레토스테네스의 체로 소수 구하기
i = 2
while i <= max_num:  # max_num이 아니더라도 math.sqrt(max_num)도 가능
    if sosu[i] == 1:  # 만약 소수라면
        only_sosu.append(i)  # 소수 리스트에 담아주고
        for j in range(i + i, max_num + 1, i):  # 그 수의 배수들은 모두 소수에서 제외
            sosu[j] = 0
    i += 1

# 숫자가 담긴 모든 리스트 순회
for x in num_list:
    for n1 in only_sosu:  # 소수 리스트를 순회하면서
        if sosu[x - n1] == 1:  # 만약 num_list와 가까운 소수를 뺸 값도 소수라면 O
            print("%d = %d + %d" % (x, n1, x - n1))
            break
