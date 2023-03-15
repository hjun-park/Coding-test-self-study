import sys

input = sys.stdin.readline

'''
    [요약]
    1. 배열 A, B, C, D 존재
    2. 4개 배열에서 값을 1개씩 뽑아서 총합 0인 쌍의 개수를 구하기
    
    [풀이] - https://jaeyoon-95.tistory.com/168
    1. a, b, c, d 리스트 만들기 (graph[0], graphp[1] ... )
    2. a, b 리스트 계산을 먼저 해서 딕셔너리를 채운다. (key는 a+b, value는 개수)
    3. c, d 리스트 계산을 해서 딕셔너리를 채운다.
     -> 그렇게 해서 a + b 값이 딕셔너리에 카운트되고 거기에 -(c + d)가 있다면 그 value만 카운트해주면 된다.
    
    [주의점]
    1. 리스트를 4개 전체 생각하는 것이 아니라 2개로 쪼개서 생각하자
    2. defaultdict를 사용하면 시간초과가 났다. 따라서 일반 dictionary를 사용하도록 한다.
      `ab.get(a + b, 0) + 1` : a+b값의 인덱스 값을 가져오고 +1을 하는데, 없을 경우 0을 가져온다. 
    3. 딕셔너리를 사용하므로 정렬할 필요가 없다. 정렬 시 시간초과가 뜸
'''

N = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(N)]

graph = list(zip(*graph))

for row in range(4):
    graph[row] = sorted(graph[row])

a_b_dict = dict()
cnt = 0

# 처음 2개를 비교해서 더한 값으로 딕셔너리를 채운다.
for a in graph[0]:
    for b in graph[1]:
        a_b_dict[a + b] = a_b_dict.get(a + b, 0) + 1

for c in graph[2]:
    for d in graph[3]:
        cnt += a_b_dict.get(-(c + d), 0)

print(cnt)
