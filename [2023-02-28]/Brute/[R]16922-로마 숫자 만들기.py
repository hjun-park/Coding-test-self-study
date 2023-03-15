import sys

input = sys.stdin.readline

N = int(input())
numbers = []

for i in range(N + 1):  # i: 1의 개수
    for j in range(N + 1 - i):  # j: 5의 개수
        for k in range(N + 1 - i - j):  # k: 10의 개수
            l = N - i - j - k  # l: 50의 개수
            number = i * 1 + j * 5 + k * 10 + l * 50
            numbers.append(number)

print(len(set(numbers)))
