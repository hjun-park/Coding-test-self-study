import sys

input = sys.stdin.readline

'''
    https://yoonsang-it.tistory.com/55
    
    핵심: 앞뒤로 붙여서 생각하기보다는, A문자를 B에 맞춘다는 생각으로 한다.
        어차피 결과값은 len(A)을 벗어나지 않는다.
        
    예시: 
          t o p a b c c o d e r
     1    a b c
     2      a b c
     3        a b c
     4          a b c
    ... 이런 방식으로 끝까지 돈 후에 최솟값을 출력한다. 
    
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
