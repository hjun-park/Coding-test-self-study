import sys
import heapq


def solution(scoville, K):
    answer = 0
    # 섞은 음식 스코빌 = 가장 맵지 X 스코빌 + (두 번째 맵지 않은 음식 스코빌 지수 * 2)
    scoville.sort()
    heapq.heapify(scoville)

    # 섞어주어야 함
    while scoville:
        if scoville[0] < K:
            try:
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)

                heapq.heappush(scoville, first + (second * 2))
                answer += 1
            except IndexError:
                print('-1')
                return -1
        else:
            print(answer)
            return answer
'''
    우수 코드
    
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
'''
