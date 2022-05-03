import re
from collections import deque
from itertools import permutations


def solution2(expression):
    answer = -1

    for ops in list(permutations(['+', '-', '*'], 3)):
        q = deque(re.split('([0-9]+)', expression)[1:-1])
        for op in ops:
            _stack = []
            while q:
                e = q.popleft()

                if e == op:
                    _stack.append(str(eval(_stack.pop() + e + q.popleft())))
                else:
                    _stack.append(e)
            q = deque(_stack)

        answer = max(answer, abs(int(q.pop())))

    return answer


# 다른 사람의 풀이
def solution(expression):
    operations = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'), ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):   # 우선순위 먼저인 것을 기준으로 split
            # 그 다음 것을 기준으로 split 하고 괄호를 씌워 준다. ( 마지막 우선순위 연산자는 제거되지 않고 괄호가 씌여짐)
            temp = [f"({i})" for i in e.split(b)]
            # 두 번째 연산자를 기준으로 temp 요소들을 join 한다.
            temp_list.append(f'({b.join(temp)})')

        # 첫 번째 우선순위 연산자 기준으로 temp_list 요소들 join 후 계산
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)


print(solution("100-200*300-500+20"))
