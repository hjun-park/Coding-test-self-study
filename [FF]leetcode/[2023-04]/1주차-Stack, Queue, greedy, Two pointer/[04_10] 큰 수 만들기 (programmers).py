'''
1. 첫 번째 stack에 넣고 시작
2. number 순회 (num)
  2-1. stack에 값이 있고 가장 최근에 추가한 값이 num 보다 크고 k > 0 일 때
    - k가 0이 될 때까지 pop 진행
3.미처 남은 k가 있으면 한번 더 지우기
'''


def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    # 큰 것들만 만나서 미처 다 못 지운 경우 끝에서 k개수 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


print(solution("1924", 2))
print(solution("4177252841", 4))
