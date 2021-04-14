import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

print(str(min(num_list)) + " " + str(max(num_list)))
