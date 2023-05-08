import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

LCS = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i - 1] == B[j - 1]:  # 문자열이 같은 경우 이전 값 보다 1 증가
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:  # 문자열이 다른 경우 0 초기화
            LCS[i][j] = 0

# `Longest Common SubSequence`의 경우 맨 마지막 값
# `Longest Common SubString`의 경우 행렬의 가장 큰 값
print(max(map(max, LCS)))
