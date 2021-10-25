import sys

input = sys.stdin.readline

# M개의 블루레이에 lecture 모두 담을 수 있는 최소 시간
N, M = map(int, input().split())
lecture = list(map(int, input().split()))

start = max(lecture)
end = sum(lecture)

result = 0

'''
 문제 핵심: 모든 강의자료를 돌면서 블루레이 개수에 맞도록 맞추어주는 것
   1) 시작값 : 블루레이 리스트 중 제일 큰 값,  끝값 : 블루레이 리스트를 모두 합한 값
   2) binary search, 중간값을 정함
   2-1) 모든 lecture를 돌면서 1개의 블루레이 레코드 완료할 때마다 count 증가
   2-2) 만약 M개보다 많다면 mid값 갱신, M개보다 적거나 같으면 mid 갱신 + mid를 결과값으로 저장 
'''

def binary_search(start, end):
    global result

    while start <= end:
        count = 1  # 블루레이 개수
        mid = (start + end) // 2
        temp = mid

        for lec in lecture:
            # 1개의 블루레이를 다 레코드 했을 때
            if temp - lec < 0:
                temp = mid
                count += 1
            temp -= lec

        # 녹음해야 할 양보다 더 많은 경우 녹음시간을 증가
        if count > M:
            start = mid + 1
        else:  # 그 반대
            end = mid - 1
            result = mid


binary_search(start, end)
print(result)
