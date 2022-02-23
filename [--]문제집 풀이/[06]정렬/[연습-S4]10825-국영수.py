import sys

input = sys.stdin.readline

N = int(input().rstrip())
students = [list(input().split()) for _ in range(N)]

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in students:
    print(s[0])
