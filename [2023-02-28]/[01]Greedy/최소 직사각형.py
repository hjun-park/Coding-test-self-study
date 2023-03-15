import sys

input = sys.stdin.readline

# size = [[60, 50], [30, 70], [60, 30], [80, 40]]
# size = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
size = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

row_sorted_size = sorted(size, reverse=True, key=lambda x: x[0])
col_sorted_size = sorted(size, reverse=True, key=lambda x: x[1])

one = 0
two = 0


def check(e, name):
    global two

    temp_sorted_size = 0
    if name == 'row':
        for i in row_sorted_size:
            if e[1] >= i[0] or e[1] >= i[1]:  # 세로 중에서 전부를 하나 커버 가능해야함
                continue
            else:
                return

        two = e[1]



    elif name == 'col':
        for i in col_sorted_size:
            if e[0] >= i[0] or e[0] >= i[1]:  # 가로 중에서 전부를 하나 커버 가능해야함
                continue
            else:
                return

        two = e[0]


print(row_sorted_size)
if row_sorted_size[0][0] >= col_sorted_size[0][1]:
    one = row_sorted_size[0][0]
    # row_sorted_size = row_sorted_size[1:]
    for e in col_sorted_size:  # 세로 하나씩 뽑아서
        check(e, 'row')

else:
    one = col_sorted_size[0][1]

    for e in row_sorted_size:
        check(e, 'col')

print(one, two)
print(one * two)

'''
 1) 가로 세로 중 가장 큰 수를 구한다.

'''
