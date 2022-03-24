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
    
    [풀이과정] 투 포인터
    1. left, right 를 각각 처음 idx, 끝 idx 설정
    2. (sol1 + sol2) > liq[left] + liq[right] 조건만족 시 sol1, 2값 갱신
    3. left, right 를 각각 이동한 경우를 비교 
     3-1) abs(liq[left + 1] + liq[right])
     3-2) abs(liq[left] + liq[right - 1])
     3-3) 이 둘을 비교, 값이 더 작은 쪽으로 축을 조정 
    4. left가 right를 넘어서면 종료, sol1, sol2 출력

'''

L, R = 0, N - 1
min_liq = int(1e9)
sol1, sol2 = int(1e9), int(1e9)


def find_minimum():
    global min_liq, L, R, sol1, sol2

    while L < R:
        if abs(sol1 + sol2) > abs(liq[L] + liq[R]):
            sol1 = liq[L]
            sol2 = liq[R]

        if abs(liq[L + 1] + liq[R]) >= abs(liq[L] + liq[R - 1]):
            R -= 1
        else:
            L += 1


find_minimum()
print(sol1, sol2)
