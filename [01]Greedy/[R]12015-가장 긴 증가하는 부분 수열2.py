import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [A[0]]

'''
  참고: https://daekyojeong.github.io/posts/BOJ42/
  예시 :  A = 4 3 7 5 2 1 일 때 코드 흐름에 따른 dp 변화
  4
  4
  3
  3 7
  3 5
  2 5
  1 5 => 완료
  
'''


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if dp[mid] == target:
            return mid

        elif dp[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    # 값을 못 찾으면 왼쪽 index 라도 덮음
    return start


for item in A:
    if item > dp[-1]:  # 수열 끝 수가 dp 끝 수보다 더 크면 dp에 추가
        dp.append(item)
    else:  # 수열 끝 수가 dp 끝 수보다 작으면 binary search로 찾은 index에 덮어쓰기
        idx = binary_search(0, len(dp) - 1, item)
        dp[idx] = item

print(dp)
print(len(dp))

