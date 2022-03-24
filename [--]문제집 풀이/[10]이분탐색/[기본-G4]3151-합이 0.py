import sys

input = sys.stdin.readline

N = int(input().rstrip())
A = sorted(list(map(int, input().split())))

'''
    [요약]
    1. 대회참가는 3인 1팀
    2. 코딩 실력과 팀워크는 반비례
    3. 합이 0이 되는 3인조를 만드는 경우의 수를 구하기
    
    [풀이]
    1. 입력된 코딩 실력 리스트 sort
    2. 빅오를 줄이기 위해 O(N^2)으로 2개를 더한 two 리스트 생성 and sort
    3. ~!@~!#~!##~#~!#!~#~!#@#!#!!~@
    

'''


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return False


two = []
for i in range(N):
    for j in range(N):
        two.append(A[i] + A[j])

        # 이분탐색


two.sort()
print(A)
print(two)
