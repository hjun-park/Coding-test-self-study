import sys

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))
sum_list = []
count = 0


def dfs(idx, sum):
    global count

    if idx >= N:
        return

    sum_list.append(sum + S[idx])
    dfs(idx + 1, sum + S[idx])
    dfs(idx + 1, sum)


dfs(0, 0)
sum_list.sort()
sum_list = set(sum_list)

'''
 1) 수열의 최댓값까지 loop 수행
 2) 
'''
result = 0
for i in range(max(sum_list)):
    if i + 1 not in sum_list:
        result = i + 1
        break

# 모든 리스트를 순회해도 최소값이 나오지 않은 경우
# result를 출력하는데, 비어 있으면 (최댓값 + 1) 대체
print(result if result else max(sum_list) + 1)

