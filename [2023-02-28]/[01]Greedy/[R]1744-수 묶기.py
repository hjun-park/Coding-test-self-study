import sys

input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input().rstrip()) for _ in range(N)])

'''
    참고: https://choewy.tistory.com/75
    0. 정렬 numbers
    1. numbers를 양수, 음수 plus, minus로 구분해서 담는다.
    2. plus는 정순, minus는 역순으로 재정렬
    3. plus길이가 1보다 큰 경우 연산 진행
     3-1. A * B > A + B 라면 A*B를 total에 더함
     3-2. 그렇지 않다면 A+B를 total에 더함
     3-3. P 길이 2 감소 ( P-2)
    4. 3번 연산을 진행하고 남은 1개 P가 있으면 plus 에서 하나 뺴고 total에 더해줌
    5. 마이너스 차례,Plus처럼 3-4의 연산과정을 거친다. 
    6 . total print 
'''

plus = []
minus = []
total = 0

while N > 0:
    tmp = numbers.pop()
    if tmp > 0:
        plus.append(tmp)
    else:
        minus.append(tmp)
    N -= 1

plus.sort()
minus.sort(reverse=True)

P = len(plus)
M = len(minus)

# 3번 과정
while P > 1:
    tmp1 = plus.pop()
    tmp2 = plus.pop()

    if tmp1 * tmp2 > tmp1 + tmp2:
        total += tmp1 * tmp2
    else:
        total += tmp1 + tmp2

    P -= 2

# 4번 과정
if P:
    total += plus.pop()

while M > 1:
    tmp1 = minus.pop()
    tmp2 = minus.pop()
    if tmp1 * tmp2 > tmp1 + tmp2:
        total += tmp1 * tmp2
    else:
        total += tmp1 + tmp2

    M -= 2

if M:
    total += minus.pop()

print(total)
    









