import sys

input = sys.stdin.readline

input_money = int(input().rstrip())
money = 1000 - input_money

count = 0
for i in [500, 100, 50, 10, 5, 1]:
    count += money // i
    money %= i

print(count)
