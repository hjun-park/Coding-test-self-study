import sys
input = sys.stdin.readline

N = int(input().rstrip())
tower_list = list(map(int, input().split()))

stack = []
result = [0] * N


'''
    배운 점 https://suri78.tistory.com/197 / https://qrlagusdn.tistory.com/112 / https://jayb-log.tistory.com/189
    1) while 문도 else를 붙일 수 있다.
    2) 원리
        - 오른쪽에서 왼쪽으로 레이져를 쏘지만 확인은 왼쪽에서 오른쪽 순으로 한다.

    예시
     - 6 9 5 7 4 가 있다고 가정한다. 레이저는 4에서 6으로 쏘지만 
       우리는 6에서 4로 확인을 하자
     - 처음 6을 확인한다. stack에는 비어 있으므로 while문은 돌지 않을 것이다.
       스택에 6을 넣는다. 
     - 다음으로 9를 확인한다. stack에는 6이 있지만, 6은 9보다 크지않다.
       즉, 9에서 레이저를 왼쪽으로 쏘고 있는데 6은 그걸 받지 못한다.
       따라서 스택에서 6을 제거한다. 
     - 이렇게 반복적으로 체크하다보면 각각 어디 탑에서 레이저를 받는지 알 수 있다.

'''

for i in range(N):
    tower = tower_list[i]
    # 스택에 있는 것들보다
    while stack and tower_list[stack[-1]] < tower:
        stack.pop()
    if stack:     # 스택에 수신할 탑이 있는 경우
        result[i] = stack[-1] + 1
    stack.append(i)
print(' '.join(map(str, result)))
