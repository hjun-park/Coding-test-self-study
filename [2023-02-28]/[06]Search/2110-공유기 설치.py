import sys

input = sys.stdin.readline

N, C = map(int, input().split())
house = sorted([int(input().rstrip()) for _ in range(N)])

start = 1
end = house[-1] - house[0]

result = 0


# target 개수만큼 설치 (1, 도착지는 (공유기마지막 - 공유기처음)
def binary_search(target, start, end):
    global result

    # current를 조정하면서 current + mid에 설치하고 mid를 조율한다.
    # target과 설치한 공유기 개수를 맞추어 가면서 같거나 많으면 result를 갱신하고
    # 최종값을 출력한다.
    while start <= end:
        mid = (start + end) // 2
        current = house[0]  # 공유기 현재 위치에 설치
        count = 1  # 공유기 설치 개수

        # 설치 가능한 경우
        for i in range(1, len(house)):
            if current + mid <= house[i]:
                count += 1  # 공유기 증가
                current = house[i]  # 설치된 곳으로 이동

        # 공유기 개수가 target보다 많다면 result 설정
        if count >= target:
            start = mid + 1
            result = mid

        # 설치된 공유기 수가 적은 경우
        else:
            end = mid - 1


binary_search(C, start, end)
print(result)
