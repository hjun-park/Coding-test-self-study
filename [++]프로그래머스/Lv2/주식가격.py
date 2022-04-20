from collections import deque


def solution2(prices):
    q = deque(prices)
    result = []

    while q:
        p = q.popleft()
        cnt = 0

        # 빼고나서 남은 prices에 대해서 루프 돌기
        for _q in q:
            cnt += 1  # 일단 1초는 문제에 무조건 센다고 되어 있음 (문제가 이해하기 힘듦)
            if p > _q:  # 주식가격이 크다면 유지
                break

        # 집어 넣자
        result.append(cnt)

    return result


def solution(prices):
    length = len(prices)

    # 만약 끝까지 가격이 담길 경우 가질 수 있는 인덱스 별 최댓값
    answer = [i for i in range(length - 1, -1, -1)]

    # 초깃값으로 0번 인덱스 넣기
    stack = [0]

    # 1번부터 최대 길이까지 prices 순회
    for i in range(1, length):

        # prices[stack[-1]] : 최초가
        # prices[i] : i초 뒤의 가격
        # 최초가보다 i초 뒤 가격이 떨어지는 경우
        while stack and prices[stack[-1]] > prices[i]:
            print(f'{i}번째 {stack}')
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)  # stack에는 순서대로 인덱스 담김
        print(f'{stack} 내용')
    return answer


print(solution([1, 2, 3, 2, 3]))
# print(solution([2, 1]))
