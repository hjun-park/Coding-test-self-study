import sys

sys.setrecursionlimit(100000)

N = int(input())


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


number = str(factorial(N))

count = 0
for n in number[::-1]:
    if n == '0':
        count += 1
    else:
        break

print(count)



