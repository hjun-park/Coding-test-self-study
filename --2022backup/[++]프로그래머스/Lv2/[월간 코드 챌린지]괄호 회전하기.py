# 회전을 시키고 다시 돌아오면 멈춘다.
# 매 회전 시마다 올바른 괄호 문자인지 확인해야 한다.
from collections import deque
from copy import deepcopy


def check_bracket(s):
    '''
    # 올바른 괄호 확인 루프 (스택 필요)
    1. 여는 괄호 -> push
    2. 닫는 괄호 -> pop
     2-1. pop 할 것이 없다면 return False
     2-2. pop 대상이 다르다면 return False
    3. s를 다 비우면 return True

    :param s: 괄호가 담긴 문자열 리스트
    :return: 정상적인 문자열 여부
    '''

    stack = []
    while s:
        _s = s.popleft()

        if _s == '{' or _s == '(' or _s == '[':
            stack.append(_s)
        else:
            if not stack:
                return 0

            e = stack.pop()

            if _s == '}' and e != '{':
                return 0

            elif _s == ']' and e != '[':
                return 0

            elif _s == ')' and e != '(':
                return 0

    if stack:  # 남아있으면 완전한 괄호 X
        return 0
    else:
        return 1


def solution(s):
    '''
    # 전체 루프
    1. len(문자열)만큼 루프 시도
    2. 올바른 괄호 확인 맞다면 cnt += 1 -> rotate
    3. 다시 2번부터 반복

    '''

    s = deque(s)
    cnt = 0
    for _ in range(len(s)):
        cnt += check_bracket(deepcopy(s))
        s.rotate(-1)

    return cnt


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
print(solution("}"))
print(solution("("))
print(solution("((("))
