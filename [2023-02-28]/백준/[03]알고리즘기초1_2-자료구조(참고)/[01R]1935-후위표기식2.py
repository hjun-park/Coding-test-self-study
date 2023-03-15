import sys

N = int(input())
str_list = list(input())
alpha = [0] * N

for i in range(N):
    alpha[i] = (int(input()))
stack = []
for s in str_list:
    # 알파벳 순서대로 1부터 번호가 주어짐
    # 따라서 52를 빼는 방식으로 번호를 저장
    if s.isalpha():
        # ord ( str -> int )
        stack.append(alpha[ord(s) - ord('A')])

    else:
        # 두 연산자를 빼고 입력받은 수를 가지고 다시 append 
        n2 = stack.pop()
        n1 = stack.pop()
        if s == '+':
            stack.append(n1 + n2)
        elif s == '-':
            stack.append(n1 - n2)
        elif s == '*':
            stack.append(n1 * n2)
        elif s == '/':
            stack.append(n1 / n2)

print(format(*stack, ".2f"))
