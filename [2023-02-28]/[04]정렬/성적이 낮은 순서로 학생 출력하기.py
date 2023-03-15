import sys

n = int(sys.stdin.readline().rstrip())

array = []

for i in range(n):
    input_data = sys.stdin.readline().rstrip().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
