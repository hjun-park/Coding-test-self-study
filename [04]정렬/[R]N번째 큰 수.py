import sys
import heapq

'''
    min-heap을 이용 (heapq) 우선순위 큐
    
    1) N만큼 loop를 돈다.
    1-1) heap이 비어있지 않으면 순환
    
'''

input = sys.stdin.readline

N = int(input())
matrix = []

for _ in range(N):
    lines = (list(map(int, input().split())))

    # 첫 라인만 정렬하며 push
    if not matrix:
        for num in lines:
            # 우선순위큐는 가장 작은게 가장 먼저 꺼낼 수 있도록 자동으로 배치됨
            heapq.heappush(matrix, num)
            print(matrix, "!!")

    # N번째 수를 원하기 때문에 우선순위 큐 길이를 N사이즈만큼 유지
    else:
        for num in lines:
            if matrix[0] < num:
                heapq.heappush(matrix, num)
                print(heapq.heappop(matrix))    # 가장 작은게 빠짐
                print(matrix, "@@")

print(matrix[0])



