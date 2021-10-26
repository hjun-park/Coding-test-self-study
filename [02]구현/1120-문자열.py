import sys

input = sys.stdin.readline

'''
    https://yoonsang-it.tistory.com/55
'''

A, B = input().split()

A = list(A)
B = list(B)

answer = []
for i in range(len(B) - len(A) + 1):  # +1 해 준 이유는 len(A)==len(B)에도 반복문이 돌게하기 위함
    count = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            count += 1
    answer.append(count)

# 가장 최소
print(min(answer))
