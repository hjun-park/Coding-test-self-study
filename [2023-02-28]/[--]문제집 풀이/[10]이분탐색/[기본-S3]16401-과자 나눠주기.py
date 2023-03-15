import sys

input = sys.stdin.readline

M, N = map(int, input().split())  # 조카의 수, 과자의 수
L = sorted(list(map(int, input().split())))  # 과자 N개의 길이

'''
 [요약]
  - 조카들에게 최대한 긴 과자를 나눠줘야 함
  - 반드시 같은 길이의 과자를 나눠줘야 함
  - M명의 조카, N개의 과자, [구하려는 것] 조카 1명에게 줄 수 있는 과자 최대 길이
  - 막대과자는 여러 조각으로 쪼갤 수 있으나 합치는 건 불가능
  - 구할 수 없으면 0을 출력
  
  -> Binary Search
'''

max_len = -1


def binary_search(start, end):
    global max_len
    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        # 과자 개수 계산
        for l in L:
            cnt += l // mid

        # 과자 개수 >= 조카 수 ( 값 갱신 후 과자길이 늘이기 )
        if cnt >= M:
            start = mid + 1
            max_len = max(max_len, mid)

        # 과자 개수 < 조카 수 ( 과자개수 부족 즉, 과자길이를 줄여야함 )
        elif cnt < M:
            end = mid - 1


binary_search(1, max(L))
print(max_len if max_len != -1 else 0)
