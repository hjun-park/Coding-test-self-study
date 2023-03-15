'''
    짝수 : 맨 뒤 0을 1로 교체
    홀수 :
     1) 왼쪽에 0을 채우기
     2) 오른쪽부터 탐색하여 가장 먼저 발견되는 0을 1로 변경
     3) 그 다음 인덱스를 0으로 변경


'''


def solution(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            num = list(bin(num)[2:])
            num[-1] = '1'

        else:
            num = ['0'] + list(bin(num)[2:])

            for i in range(len(num)-1, -1, -1):
                if num[i] == '0':     # 가장 먼저 발견되는 0을 1로 변경
                    num[i] = '1'
                    num[i+1] = '0'    # 그 다음 인덱스 0 변경
                    break

        result.append(int(''.join(num), 2))

    return result


print(solution([2, 7]))
