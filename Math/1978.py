import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))
result = 0


for num in num_list:
    cnt = 0
    for i in range(1, num+1):       # 1은 소수가 아님, 나눠서 1과 자기자신으로만 나누어져야 소수
        if num % i == 0:
            cnt += 1

    if cnt == 2:
        result += 1


print(result)
