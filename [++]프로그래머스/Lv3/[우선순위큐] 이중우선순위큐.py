import heapq
import sys

input = sys.stdin.readline

'''
    [요약]
    1. 명령어와 행동이 규정된 표 존재
    2. 연산이 주어질 때 비어있고 비어있지 X 경우를 표시

    [풀이] - 최대최소를 찾는데 시간복잡도를 줄여야하나?
    1. op로부터 값을 뺀다.
    2. 값을 파싱한다.
    3. 명령어에 따라 명령을 수행한다. 
'''


def solution(operations):
    hq = []

    while operations:
        op = operations.pop(0)
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(hq, num)
        else:  # 'D'
            if hq:
                if num == 1:  # 최댓값 삭제 ( 중요 (heapq는 우선순위 최상위 값 이외의 정렬을 보장하지 않음 )
                    max_value = max(hq)
                    hq.remove(max_value)

                else:  # 최솟값 삭제
                    heapq.heappop(hq)

        # print(f'hq 상태 : {hq}')

    if not hq:
        return [0, 0]
    else:
        return [max(hq), hq[0]]


print(solution(['I 16', 'D 1']))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I 1", "I -1", "I 2", "D 1", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(['I 16', 'I 16', 'I 16', 'I 16']))
print(solution(['D 1', 'D -1', 'D 1', 'D -1']))
print(solution(
    ["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2",
     "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
print(solution(["I 5", "I 5", "D 1", "I 7", "D -1", "I 8"]))
