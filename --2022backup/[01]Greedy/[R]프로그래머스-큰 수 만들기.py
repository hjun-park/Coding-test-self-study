import sys

k = int(input())
numbers = list(input())

# 1) 처음 스택 값을 집어넣고 시작
stack = [numbers[0]]

# 2) 0은 집어넣었으니 1부터 looping 시작
for number in numbers[1:]:
    # 3) 처음 a) 스택값존재, 스택last값보다 num이 더 큰 경우며 K가 0보다큰 경우
    # -> k값 감소와 스택의 값을 여러개 뺀다.
    while len(stack) > 0 and stack[-1] < number and k > 0:
        k -= 1
        stack.pop()

# 4) while문이 끝나면 스택에 큰 값을 집어넣는다.
    stack.append(number)

# 5) 가끔 K가 끝나기도 전에 마지막 numbers까지 도달하는 경우 발생
if k != 0:
# 6) 이러한 경우는 그만큼 스택에 있는 값을 끝에서부터 제거
    stack = stack[:-k]

# 7) list joining을 통한 결과물 출력
print(''.join(stack))
