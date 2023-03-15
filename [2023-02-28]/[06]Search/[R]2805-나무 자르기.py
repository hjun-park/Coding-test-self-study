import sys

'''
    1) start, end 정하기 ( 값으로 정하고 start는 0 )
    2) 이분탐색 수행, 잘린트리 변수 선언
    3) trees 순회, 만약 각 tree가 중간값보다 크다면 잘린트리 변수에 더해주기
    4) 그 다음으로 tree가 잘린크기보다 큰지 작은지를 정해보고 start값 혹은 end값 조절하기
    
'''

input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        tree = 0    # 잘린 나무 합

        for i in trees:
            if i > mid:
                tree += i - mid

        # if array[mid] == target:
        #     return mid

        if tree >= target:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
binary_search(trees, M, start, end)


