import sys

input = sys.stdin.readline

'''
 - 하노이 탑 이동 순서
   1) n-1개의 원판 기둥1 -> 기둥2 이동
   2) n번 원판 기둥1 -> 기둥3 이동
   3) n-1개의 원판 기둥2 -> 기둥3 이동

 - 하노이를 귀납적으로 접근한다면,
    - 원판이 1 개일 때 원판을 내가 원하는 곳으로 옮길 수 있다.
    - 따라서, 원판이 K개일 때 옮길 수 있다면 원판이 K+1개일 때에도 옮길 수 있다.
    
 - 재귀함수를 정의하자.
   1) 함수 정의 (함수가 어떤 역할을 수행하는지, 어떤 인자를 가지는지 정의)
    void func(int a, int b, int n) : 원판 n개를 a에서 b번 기둥으로 옮기는 방법
    
   2) base condition
    - n=1일 때 count << a << ' ' << b << '\n';
    
   3) 재귀식
    a) n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다. (기둥번호합이 6이니까) func(a, 6-a-b, n-1);
    b) n번 원판을 기둥 a에서 기둥 b로 옮긴다. cout << a << ' ' << b << '\n';
    c) n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다. func(6-a-b, b, n-1);
'''


def hanoi(a, b, n):
    global K

    K += 1
    # 1) 우선 원판이 1개 남아서 옮겨야 되는 경우 (마지막 원판) 출력한다.
    if n == 1:
        moves.append((a, b))
        return

    # a) n-1개 이동 ( a -> 6-a-b )
    hanoi(a, 6 - a - b, n - 1)

    # b) n번째 이동 ( a -> b )
    moves.append((a, b))

    # c) n-1개 이동 ( 6-a-b -> b )
    hanoi(6 - a - b, b, n - 1)


N = int(input().rstrip())
moves = []
K = 0

hanoi(1, 3, N)
print(K)

for m in moves:
    print(m[0], m[1])
