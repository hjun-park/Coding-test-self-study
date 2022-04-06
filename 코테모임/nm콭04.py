import sys

# from collections import deque

input = sys.stdin.readline

'''
    [요약]
    1. 한 번에 최대 N잔까지 동시에 커피 추출 
    2. 커피 만들어지는 순서 구하려고함 
    3. M잔 만들어야하고 1부터 M까지 주문번호 부여
    4. 주문번호 순대로 빈 커피 추출구에서 커피 만듦
    5. 빈 커피 추출구가 없다면 다음 추출구를 기다리며 그 다음 즉시 만들기 시작
    
    즉, 커피가 완료되는 순서를 배열에 담아 리턴
    동시에 완료되면 주문순서가 일찍인 것이 먼저
    
    N은 커피 추출구 개수
    배열에 있는 값은 커피가 만들어지는데 걸리는 시간
'''


def solution(N, coffee_times):
    M = len(coffee_times)
    idx = 1
    result = [0] * (N + 1)
    print(coffee_times)
    # q = deque()
    q = []

    for _ in range(N):
        q.append(coffee_times.pop(0))

    while coffee_times:
        _min = min(q)

        for i in range(len(q)):
            q[i] -= _min
            print(f'남은 시간', q)

            if q[i] == 0:
                print(coffee_times)
                q.pop(i)
                result[i] = idx
                idx += 1
                if coffee_times:
                    q.append(coffee_times.pop(0))


    return result


print(solution(3, [4, 2, 2, 5, 3]))
# print(solution(1, [100, 1, 50, 1, 1]))
