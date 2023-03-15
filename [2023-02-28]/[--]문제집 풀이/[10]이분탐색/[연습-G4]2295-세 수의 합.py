import sys

input = sys.stdin.readline

N = int(input().rstrip())
a = sorted([int(input().rstrip()) for _ in range(N)])

'''
    [문제] a[i] + a[j] + a[k] = a[l] 을 만족하는 a[l] 중에서 최댓값

    [여러가지 풀이 방법]
    1. O(N^4) = i, j, k, l에 대한 4중 for문
    2. O(N^3logN) = i, j, k 3중 for문을 돌리고 나온 결과가 배열 a에 있는지 이중탐색

    [핵심적인 풀이 방법 - 신박함]
    3. O(N^2logN)
     3-1) 가장 먼저 a[i] + a[j] 를 더해서 two[m] 배열을 만든다. -- O(N^2)
       -> two[m] + a[k] = a[l]을 만족하는 a[l] 중에서 최댓값
     3-2) k, l 2중 for문, a[l]-a[k]가 배열 two[m]에 있는지 이분탐색
       -> two의 길이는 O(N^2), 이분탐색은 O(logN)
       -> two에 대한 이분탐색은 O(log(N^2))
       -> (lg(N^2) = 2lgN) 이므로 O(N^2lg(N^2)) == O(N^2 * 2lgN) = O(N^2lgN)

'''


def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if two[mid] == target:
            return True

        elif two[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return False


two = []
for i in range(N):
    for j in range(i, N):
        two.append(a[i] + a[j])

two = sorted(two)

for l in range(N - 1, 0, -1):  # l은 가장 큰 것부터 찾기
    for k in range(l):  # k는 l보다 작게
        # end는 a의 길이가 아니라 two 배열의 길이 ( 그만큼 찾으니까 )
        num = binary_search(a[l] - a[k], 0, len(two) - 1)

        if num is True:
            print(a[l])  # 가장 먼저 큰 것부터 찾으므로 출력
            sys.exit(0)
