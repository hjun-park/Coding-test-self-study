import sys

'''
5
    7
   3 8
  8 1 0
 2 7 4 4
4 5 2 6 5
'''

'''
    2021-07-11
    [시작 체크 리스트]
    V       15분 지났으나 발상 불가 또는 아예 다른 길
            코드 50% 정도 완성
            30분 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
            코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
    V       중간 정도 이해함
            완벽히 이해함

    [첨언]
    
'''

'''
    [접근]
     - 점화식
        dp[i] = 현재 위치의 값 + max(왼쪽 위 대각선, 오른쪽 위 대각선)
     -  예외처리 ( 왼쪽 및 오른쪽 위 대각선 값들이 없을 수 있음 )
        1) 위치가 제일 첫 번째의 경우 왼쪽 대각선 값이 없음 
        2) 위치가 제일 마지막의 경우 오른쪽 대각선이 없음 
            
    
'''

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0:  # 제일 왼쪽의 값은 왼쪽 대각선이 없음
            data[i][j] += data[i - 1][j]
        elif j == len(data[i]) - 1:  # 제일 오른쪽 값은 오른쪽 대각선이 없음
            data[i][j] += data[i - 1][j - 1]
        else:
            # 점화식, 왼쪽 및 오른쪽 위 대각선을 가지고 처리
            data[i][j] += max(data[i - 1][j - 1], data[i - 1][j])

print(max(data[n - 1]))
