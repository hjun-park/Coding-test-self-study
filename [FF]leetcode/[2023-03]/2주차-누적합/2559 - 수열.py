import sys

input = sys.stdin.readline

N, K = map(int, input().split())
days = list(map(int, input().split()))

psum = sum(days[:K])
result_list = [psum]

for i in range(0, len(days) - K):
    psum = psum - days[i] + days[i + K]
    result_list.append(psum)

print(max(result_list))
