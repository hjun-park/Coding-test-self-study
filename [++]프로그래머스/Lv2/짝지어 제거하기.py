def solution(s):
    _stack = []

    # 스택을 만들기

    for _s in s:
        if _stack:
            if _stack[-1] == _s:  # 이전 문자와 현재 문자를 비교
                _stack.pop()    # 같은 경우 이전 문자 pop
            else:
                _stack.append(_s)  # 다른 경우 추가 // 그럼 2개씩 처리 가능

        else:
            _stack.append(_s) # 처음 혹은 모두 중복제거 된 경우

    if _stack:
        return 0
    else:
        return 1


print(solution('baabaa'))
print(solution('cdcd'))
