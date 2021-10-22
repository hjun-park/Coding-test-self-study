import sys
import heapq

'''
    1. 시작시간 기준으로 정렬한다.
    2. heapq q를 선언한다. ( 종료시간만 들어갈 큐 )
    3. 처음 회의의 시간을 꺼낸다.
    4. 선언한 q에 처음 회의의 종료 시간을 넣는다.
    
    5. 강의 시간 리스트를 순회한다.
    5-1) 만약 이전 회의 종료시간과 현재 회의 시작시간 비교
      -> 현재 회의가 이전 종료보다 늦게 시작한다면 큐를 뺴고 종료시간을 새로 갱신
    5-2) 아니라면 그냥 집어 넣는다.
    
    6. 최종적으로 heapq 길이를 반환한다. ( 종료 시간 개수 따라서 강의실 길이가 정해짐 ) 
'''

input = sys.stdin.readline

N = int(input())
C = []

for _ in range(N):
    C.append(list(map(int, input().split())))

# 시작 시간 기준으로 정렬
C.sort(key=lambda x: x[0])

q = []
first = C.pop(0)

# 종료 시간을 집어넣음 ( 강의실 1개 추가 )
heapq.heappush(q, first[1])

for time in C:
    # 이전 강의 종료시간과 현재 강의 시작 시간 비교
    # 이전 강의 시간 종료와 함께 현재 강의가 시작된다면
    # heapq를 pop하고 heappush 한다. ( 갱신하는 것, ( 강의실 1개 그대로 ) )
    # 갱신할 때는 종료시간으로 한다.
    if q[0] <= time[0]:
        heapq.heappop(q)
        heapq.heappush(q, time[1])
    else:  # 아니라면 그냥 추가 ( 강의실 1개 추가 )
        # 추가할 때는 종료시간으로 한다.
        heapq.heappush(q, time[1])

print(len(q))
