import sys

input = sys.stdin.readline

'''
    next permutation 알고리즘
    https://jins-dev.tistory.com/entry/%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-%EC%B0%BE%EA%B8%B0-%EC%A0%84%EC%B2%B4-%EC%88%9C%EC%97%B4-%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Next-Permutation
'''

N = int(input().rstrip())
array = list(map(int, input().split()))
x = 0

# 1) 순열 전체를 역순조회하면서 가장 첫 번째 array[i-1] < array[i] 인 수를 구한다.
for i in range(N - 1, 0, -1):
    if array[i-1] < array[i]:
        x = i - 1
        break

# 2) 그 다음으로 다시 역순조회하며 array[x] 보다 큰 array[i]를 발견할 때마다
#   서로 swap 후에 x+1부터 마지막까지
for i in range(N-1, 0, -1):
    if array[x] < array[i]:
        array[x], array[i] = array[i], array[x]
        array = array[:x+1] + sorted(array[x+1:])
        print(*array)
        sys.exit(0)
print(-1)

