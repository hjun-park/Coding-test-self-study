import sys

input = sys.stdin.readline

# print((lambda x: x * (x + 1) // 2)(int(input().rstrip())))
# print((lambda a, n, d: a + (n-1)*d)(map(int, input().split())))

input().rstrip()
print(min(list(map(int, input().split()))))
