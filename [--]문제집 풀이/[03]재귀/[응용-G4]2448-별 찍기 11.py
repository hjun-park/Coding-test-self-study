# [참고] https://ku-hug.tistory.com/149

import sys

input = sys.stdin.readline

n = int(input())

stars = [[' '] * 2 * n for _ in range(n)]


# 재귀 형식처럼 n=1 작은 값부터 생각해 점화식을 생각하기
def recursion(i, j, size):
    if size == 3:
        '''
                       *                        
                      * *                       
                     *****    
         => 이런 형식의 별 트리 하나 만드는 base condition
        '''
        stars[i][j] = '*'
        stars[i + 1][j - 1] = stars[i + 1][j + 1] = "*"
        for k in range(-2, 3):
            stars[i + 2][j - k] = "*"

    else:
        newSize = size // 2
        recursion(i, j, newSize)    # 위 (자기자신)
        recursion(i + newSize, j - newSize, newSize)    # 아래 왼쪽
        recursion(i + newSize, j + newSize, newSize)    # 아래 오른쪽


recursion(0, n - 1, n)
for star in stars:
    print("".join(star))
