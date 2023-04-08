import sys

input = sys.stdin.readline

N, K = 10, 5
arr = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
# N, K = map(int, input().split())
# arr = list(map(int, input().split()))

'''
    이 방식은 psum의 index가 보기 어려움
'''
# _len = len(arr)

# psum = [0] * _len
# psum[0] = arr[0]
#
# for i in range(1, _len):
#     psum[i] = psum[i - 1] + arr[i]
#
# _max = psum[K - 1]
#
# for i in range(K + 1, _len):
#     _max = max(_max, psum[i - 1] - psum[i - K - 1])
#
# print(_max)


'''
    이 방식은 psum의 index가 보기 쉬움
    1. psum의 0번째 인덱스에 0을 대입
    2. psum의 1번쨰부터 사실상 arr[0]이 들어감
    3. psum의 N+1번쨰에 arr[N]이 들어감
'''
_len = len(arr)

psum = [0] * (_len + 1)

for i in range(1, _len + 1):
    psum[i] = psum[i - 1] + arr[i - 1]

_max = psum[K]

for i in range(K, _len + 1):
    _max = max(_max, psum[i] - psum[i - K])
