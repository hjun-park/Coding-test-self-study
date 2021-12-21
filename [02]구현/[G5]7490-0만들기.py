import sys

input = sys.stdin.readline

''' https://westmino.tistory.com/47
    1) 전형적인 백트래킹 문제
    2) +, -는 괜찮지만 문제에서는 ' '를 두 수를 잇는 것으로 했는데, 이것이 문제점
      -> 1-2 3  계산하는 방법이 관건
    3) 문제의 핵심
     - 백트래킹 
     - eval 함수는 수학식 계산이 가능
    4) 마지막 ASCII 정렬 후 출력하는 파트
     - 숫자는 1, 2, 3 순서 .. 중간 연산자는 아스키코드에서 ' ' -> '+' -> '-' 순서이다.
       백트래킹 들어갈 때 연산자는 저 위에처럼 들어가면 최종적으로 정렬할 필요가 없다.
'''


def calc(formula):
    temp = formula.replace(' ', '')

    if eval(temp) == 0:
        print(formula)


def dfs(now, formula):
    # 개수가 N과 같으면 연산하기
    if now == N + 1:
        calc(formula)
        return

    # 다르면 계산식 추가
    dfs(now + 1, formula + ' ' + str(now))
    dfs(now + 1, formula + '+' + str(now))
    dfs(now + 1, formula + '-' + str(now))


for num in range(int(input().rstrip())):
    N = int(input())
    dfs(2, '1')  # 계산식에서 1은 넣고 시작
    print()
