import sys

input = sys.stdin.readline

'''
    1) start, end 정하기
    2) 아이들 수가 놀이기구 수보다 적으면 아이들 수 출력 
    3) 그렇지 않을 경우 이분탐색을 진행
    3-1) 놀이기구를 순회하면서 (분) // (각 놀이기간 시간) 나누며 count를 구함
    3-2) count가 아이들 수와 같거나 크면 충분히 수용이 가능한 상태이므로 result에 mid 담고 end 수정
    3-3) count가 아이들 수와 작으면 수용하지 못하므로 start값을 증가하고 진행
    4) 놀이기구를 순회하면서 result-1분 전까지 놀이기구에 몇 명 탔는지 탐색
    5) 놀이기구를 순회하면서 해당 result 때 탔던 애를 구한다.
'''

# 아이들, 놀이기구
N, M = map(int, input().split())
time = list(map(int, input().split()))

start = 0
end = 2000000000 * 30  # 최대인원 * 최대시간

result = 0


def binary_search():
    global result, start, end

    while start <= end:
        mid = (start + end) // 2

        cnt = M  # 처음에는 모든 사람들이 다 탐
        for t in range(M):  # 놀이기구 순환
            cnt += mid // time[t]  # 결과적으로 몇 명 타는지 알 수 있음
        if cnt >= N:  # 실제 아이들보다 더 많은 애들을 태운 경우 시간을 줄임
            result = mid  # 시간을 저장
            end = mid - 1
        else:  # 반대의 경우 시간을 늘림
            start = mid + 1

    # 마지막 아이가 타기 직전 시간까지 몇 명이서 탔는지 알 수 있음
    cnt = M
    for t in range(M):
        cnt += (result - 1) // time[t]

    for t in range(M):
        if result % time[t] == 0:  # 이 때 마지막 아이가 놀이기구를 탔다는 의미
            cnt += 1
        if cnt == N:  # 마지막 아이라면
            print(t + 1)  # 놀이기구 번호 출력
            break


binary_search()
