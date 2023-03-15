import sys

input = sys.stdin.readline

# N = int(input().rstrip())
'''
    [함수 정의]
    def logic(N, st, en):
        
    
    [base condition]
    if N == 1:
        return 
    
    [recursion logic]
    1) 27에 대해서 가운데 빈칸을 만들고 (9 - 17까지)
    2) 다음 9에 대해서 가운데 빈칸
    3) 다음 3에 대해서 빈칸
    4) 1이면 탈출

'''


def logic(n):
    if n == 1:
        return ['*']

    stars = logic(n // 3)
    L = []

    for s in stars:
        L.append(s * 3)

    for s in stars:
        L.append(s + ' ' * (n // 3) + s)

    for s in stars:
        L.append(s * 3)

    for row in L:
        print(row)

    return L

# logic(27)
# print('\n'.join(logic(9)))
