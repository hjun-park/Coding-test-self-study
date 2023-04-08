import sys

input = sys.stdin.readline

# N, K = 10, 5
# arr = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
N, K = map(int, input().split())
arr = list(map(int, input().split()))

'''
1) 투포인터 지정, 0과 0+K
2) 두 포인터 간 합 계산
3) 왼쪽 꺼 빼고 왼쪽 이동, 오른쪽 이동 후 오른쪽 더함
4) right가 끝까지 갈 때까지 진행
'''
left, right = 0, K
_sum = sum(arr[:right])
_max = -1

for i in range(K, N):
    _sum = _sum + arr[i] - arr[i - K]
    _max = max(_max, _sum)

print(_max)
