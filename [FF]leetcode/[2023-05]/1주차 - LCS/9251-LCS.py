import sys

input = sys.stdin.readline

'''
LCS 알고리즘
 - https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
 
 백준 
 - https://www.acmicpc.net/problem/9251
 - https://www.acmicpc.net/problem/5582
'''


# ============================ 방법 1 =========================== #
# =============== 마진을 주지 않고 1부터 루프 시작 ================= #
A = input().rstrip()
B = input().rstrip()
LCS = [[0] * (len(B)+1) for _ in range(len(A)+1)]

# Bottom-up 방식
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:    # 마진을 안 주는 방법은 비교 시 -1값과 비교 해야 한다.
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:   # 다른 경우 둘 중 큰 값
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

'''
0 0 0 0 0 0 0
0 0 1 1 1 1 1
0 1 1 1 2 2 2
0 1 2 2 2 3 3
0 1 2 2 2 3 3
0 1 2 2 2 3 4
0 1 2 3 3 3 4
'''
print(LCS[-1][-1])


# ============================ 방법 2 =========================== #
# ============= 입력 값에 마진을 주고 0부터 루프 시작 ============== #

# A = '0' + input().rstrip()
# B = '0' + input().rstrip()
# LCS = [[0] * len(B) for _ in range(len(A))]
#
# # Bottom-up 방식
# for i in range(len(A)):
#     for j in range(len(B)):
#         if i == 0 or j == 0:    # 0부터 시작해서 마진을 줌
#             LCS[i][j] = 0
#         elif A[i] == B[j]:
#             LCS[i][j] = LCS[i-1][j-1] + 1
#         else:   # 다른 경우 둘 중 큰 값
#             LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
#
# '''
# 0 0 0 0 0 0 0
# 0 0 1 1 1 1 1
# 0 1 1 1 2 2 2
# 0 1 2 2 2 3 3
# 0 1 2 2 2 3 3
# 0 1 2 2 2 3 4
# 0 1 2 3 3 3 4
# '''
#
# print(LCS[-1][-1])
