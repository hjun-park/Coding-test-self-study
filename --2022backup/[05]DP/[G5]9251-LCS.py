import sys

input = sys.stdin.readline

# 참고: https://suri78.tistory.com/11

'''
    핵심: 점화식, 위 링크참고
    
    # 1) 가장 최근 추가된 글자가 서로 같을 때 ( ACA, CAPCA 처럼 끝에가 A로 끝 )
    matrix[i][j] = matrix [i-1][j-1] + 1    # 같은 글자 추가되기 전 가장 큰 길이 + 1  
    
    # 2) 가장 최근 추가된 글자가 서로 다를 때 ( ACAYKP, CAPCAK 처럼 끝에가 P, K 다름 )
    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j]) # 기존 주어진 문자열로 만들 수 있는 최대길이 
'''

S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:  # 추가된 문자가 같은 경우
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:  # 추가된 문자가 다른 경우
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])


