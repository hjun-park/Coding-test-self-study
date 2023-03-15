import sys

'''
    // https://jinho-study.tistory.com/150
    1) 입력 + flag 설정
    2) x가 M*N 아래까지 루프 돌기 
    3) x%N, y%N 나머지가 같은 경우에는 x를 출력하고 flag값 False 설정
    4) 아닌 경우라면 x += M 
'''

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    flag = True

    while x <= M * N:
        if x % N == y % N:
            print(x)
            flag = False
            break
        x += M

    if flag:
        print(-1)
