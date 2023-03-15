import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().split()))  # 숫자 리스트
ops = list(map(int, input().split()))  # 연산자 갯수

result = [int(1e9), -int(1e9)]

# 최대와 최소를 구하는 문제

'''
1) 함수의 정의
 logic(total, depth, plus, minus, mul, div) 
2) base condition
 depth == N ( 수의 개수가 최대에 달했을 때 )
   - 최종 값을 result에 별도로 저장
   - return
3) recursion logic
 if plus ... div
 
 
'''


def logic(total, depth, plus, minus, mul, div):
    global result
    if depth == N:
        result[0] = min(result[0], total)
        result[1] = max(result[1], total)
        return

    # recursion logic
    if plus:
        logic((total + A[depth]), depth + 1, plus - 1, minus, mul, div)

    if minus:
        logic((total - A[depth]), depth + 1, plus, minus - 1, mul, div)

    if mul:
        logic((total * A[depth]), depth + 1, plus, minus, mul - 1, div)

    if div:
        logic(int(total / A[depth]), depth + 1, plus, minus, mul, div - 1)


logic(A[0], 1, ops[0], ops[1], ops[2], ops[3])

print(result[1])
print(result[0])

