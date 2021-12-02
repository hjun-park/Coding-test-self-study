import sys

input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())

'''
ababababa
aba

'''
count = 0
i = 0
while i <= len(a) - len(b):
    if a[i:i + len(b)] == b:
        count += 1
        i += len(b)
    else:
        i += 1
print(count)
