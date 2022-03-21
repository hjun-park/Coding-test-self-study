import sys

input = sys.stdin.readline

# 그리디 문제

'''
 고려할 점 ( 출처: https://studyandwrite.tistory.com/337 )
 1) 110보다 사전순으로 늦게 검색되는 문자열은 111뿐
  - 따라서 110을 모두 찾은 후 111 앞에 삽입한다면 111을 110으로 대체한 것과 같다.
 2) 110 제거 후 뒤에서 순회하면서 1의 개수를 세어 준다. 
  - 110을 제거하고 나면 문자열에서 연속된 1이 나타나는 지점이 없거나 한 곳만 나타난다.
  - 즉, 1이 연속되다가 0을 만나면 110 형태가 되어버리기 때문에 이미 제거가 된 상태
  3) stack[:len(stack)-count_1] 뒤에 110 문자 이어붙이고 연속된 1을 붙인다.
'''


def solution(s):
    answer = []

    # 1) 테스트케이스 순회
    for string in s:
        count_110 = 0  # 110 개수
        stack = []

        # 2) 문자열 순회
        for str in string:
            # 저장된 게 2개 이상인 경우 ( 3자리가 된 상태 )
            if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0':  # 그게 110 인 경우
                    count_110 += 1
                    stack.pop()
                    stack.pop()  # 어차피 str는 stack에 안 들어가서 pop은 2번만 해줘도 된다.

            else:  # 저장된 것이 2개 미만인 경우 추가
                stack.append(str)

        # 3) 110 제거한 상태
        # 뒤에서부터 1의 숫자를 계속 세면서 0을 만날 때까지 반복한다.
        count_1 = 0
        for s in stack[::-1]:  # 거꾸로 순회한다.
            if s == '0':  # 0을 만나면 종료 (110은 0 뒤에 와야 사전적으로 유리)
                break
            else:
                count_1 += 1

        '''
            # 즉, 처음 만나는 '0' + '110' * [개수만큼] + '1' * [개수만큼]
            
            stack[:len(stack) - count_1] : 0 바로 뒤에
            '110' * count_110 : '110'을 count 만큼 출력
            '1' * count_1 : '1'을 count만큼 출력
        '''
        answer.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)

    return answer


print(solution(["1110", "100111100", "0111111010"]))
