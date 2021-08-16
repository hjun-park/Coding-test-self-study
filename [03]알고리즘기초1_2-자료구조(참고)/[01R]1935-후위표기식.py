import sys

N = int(input())
str_list = list(input())
alpha = [0] * N

for i in range(N):
    alpha[i] = (int(input()))
stack = []
for s in str_list:
    if s.isalpha():
        stack.append(alpha[ord(s) - ord('A')])

    else:
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
