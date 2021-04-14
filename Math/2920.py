import sys

dl = list(map(int, sys.stdin.readline().rstrip().split()))

if dl == sorted(dl):
    print('ascending')
elif sorted(dl) == list(reversed(dl)):
    print('descending')
else:
    print('mixed')
