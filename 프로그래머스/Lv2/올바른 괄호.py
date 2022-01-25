import sys

input = sys.stdin.readline


def solution(s):
    count = 0

    # 1) 처음 괄호가 닫혀있거나 마지막 괄호가 열려있는 경우 False
    if s[0] == ')' or s[-1] == '(':
        return False

    for ss in s:

        # 2-1) 열린 괄호일 경우 카운트 증가
        if ss == '(':
            count += 1

        # 2-2) 닫힌 괄호일 경우 카운트 감소
        else:
            count -= 1

        # count가 0보다 작으면 닫는 괄호가 더 추가된 것이므로 False
        if count < 0:
            return False

    # 만약 닫는괄호, 여는괄호 수가 같지 않다면 False
    if count != 0:
        return False

    return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
