import sys

input = sys.stdin.readline

N = int(input().rstrip())

liq = list(map(int, input().split()))

'''
    
    [요약]
    1. 음수: 산성 / 양수: 알칼리성
    2. 같은 양의 두 용액 혼합 -> 특성값 0에 가깝도록 만들 계획
    3. 정렬된 순서로 주어지기 때문에 정렬할 필요 X
    
    시간복잡도 1초, 값의 범위는 20억, O(lgN) 내로 해결 필요
    
    [풀이과정] binary search + two pointer
    1. left, right 를 각각 처음 idx, 끝 idx 설정
    2. 연산진행 -> 음수면 right-1, 양수면 left +1
    3. left가 right를 넘어서면 종료 

'''

L, R = 0, N - 1
min_liq = int(1e9)
sol1, sol2 = 0, 0


def find_minimum():
    global min_liq, L, R, sol1, sol2

    while L < R:
        abs_solution = abs(liq[L] + liq[R])
        non_solution = liq[L] + liq[R]

        if abs_solution <= min_liq:
            min_liq = abs_solution
            sol1, sol2 = liq[L], liq[R]

        if non_solution == 0:
            break

        elif non_solution < 0:
            L += 1

        else:
            R -= 1


find_minimum()
print(sol1, sol2)
