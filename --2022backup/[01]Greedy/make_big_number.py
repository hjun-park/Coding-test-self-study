def solution(number, k):
    stack = [number[0]] # 1
    for num in number[1:]: # 924
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # len(stack) : 스택에 값이 있다면 그리고 스택의 마지막값이 이번값보다 작다면 그리고 아직 지울 k회가 남아있다면 스택에서 지운다.
            k -= 1
            stack.pop()

        # 일단 값을 stack에 추가한다
        stack.append(num)
    # 아직 k개수만큼 못 뺐으면 끝에서 k개만큼 제거.
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


if __name__ == '__main__':
    number = "4177252841"
    k = 4
    print(solution(number, k))

