import sys

n = int(input())
array = []
count = [0] * 10001  # 한정된 양 만큼 산정

for i in range(n):
    input_num = int(sys.stdin.readline().rstrip())
    count[input_num] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i)  # print도 end를 넣으면 시간 초과 그래서 뺀다.
