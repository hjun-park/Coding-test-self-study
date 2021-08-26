import sys

# stack을 이용하여 풀어야 한다. (시간 및 메모리초과)
# 스택과 num을 비교하여 큰 num값이 들어오면 stack에서 빼준다.

N, K = map(int, input().split())
numbers = list(input())

stack = []
k = K

# 숫자 전체를 순환
for num in numbers:
    # 스택이 비어있지 않고 스택 끝값보다 큰 num값이 들어온다면 수행
    while stack and k > 0 and stack[-1] < num:
        print('del')
        del stack[-1]
        k -= 1
    stack.append(num)

print(stack)
print(''.join(stack[:N-K]))
