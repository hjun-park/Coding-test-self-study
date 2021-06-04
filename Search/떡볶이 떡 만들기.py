import sys

n, m = list(map(int, input().split(' ')))   # 떡의 개수 / 요청한 떡 사이즈
array = list(map(int, input().split())) # 총 떡 사이즈

start = 0
end = max(array)

# 반복적 이진탐색
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    # 잘랐을 때 떡의 양 계산
    for x in array:
        if x > mid:
            total += x - mid

    # 떡의 양이 부족하면 더 많이 자르기
    if total < m:
        end = mid - 1

    # 떡의 양이 많으면 덜 자르기
    else:
        result = mid # 최대한 떡을 덜 자른게 정답이므로 여기서 정답을 저장
        start = mid + 1

print(result)