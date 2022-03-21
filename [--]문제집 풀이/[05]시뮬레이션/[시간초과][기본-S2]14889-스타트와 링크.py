import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

'''
문제요약
 - N명, 짝수, N/2명으로 스타트, 링크 팀으로 나눔
 - S(ij) = i, j 같은 팀 then 팀에 더해지는 능력치
 - S(ij), S(ji)는 다를 수 있음
 - i와 j가 같은 팀이라면 그 팀에는 S(ij) + S(ji)
 
 - 능력차이를 최소화하고자 함
 
 <풀이핵심>
 1. 인덱스를 0과 1로 나누어 하나로 담은 팀 리스트 생성 (team 배열)
 1-1. permutation을 돌린다 ( [0, 0, 0, 1, 1, 1] 에서 순열들을 구함 )
 2. for 돌면서 팀값이 0 or 1에 따라 diff를 더하고 뺌 (그럼 최소가 나옴)
 3. 최솟값 갱신
'''

# 팀의 시작의 중간부터 끝까지 1로 채움 ( 0: 스타트, 1: 링크 )
min_diff = int(1e9)
team_list = [0] * (N // 2) + [1] * (N // 2)

for team in permutations(team_list, N):  # 순열을 돌아서 팀이 되는 경우의 수를 찾음
    diff = 0  # 능력치 차이
    for i in range(N):
        for j in range(i + 1, N):
            if team[i] != team[j]:  # 숫자가 다르다는건 둘이 다른 팀 (같은팀끼리만 능력치 계산 가능)
                continue

            if team[i] == 0:  # 스타트 팀인 경우
                diff += (graph[i][j] + graph[j][i])
                # print(f'스타트 팀 : {i}, {j}')
                # print(f'스타트 팀 : {graph[i][j]} + {graph[j][i]} ')
                # print()
            elif team[i] == 1:  # 링크 팀인 경우
                diff -= (graph[i][j] + graph[j][i])
                # print(f'링크 팀 : {i}, {j}')
                # print(f'링크 팀 : {graph[i][j]} + {graph[j][i]} ')
                # print()

    # 최솟값 갱신
    min_diff = min(min_diff, abs(diff))

print(min_diff)
