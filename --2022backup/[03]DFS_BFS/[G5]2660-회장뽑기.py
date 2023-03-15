import sys
from collections import deque

input = sys.stdin.readline

# 입력
N = int(input().rstrip())
member = [[] for _ in range(N + 1)]


def bfs(mem_num):
    base_score = 0
    q = deque()
    q.append((mem_num, base_score))

    # BFS 시작
    while q:
        to_mem, score = q.popleft()
        # 문제 주의 사항을 살펴보면 최소 점수를 점수로 취급한다.
        # 자기 자신은 0점이 들어간다.
        member_score[mem_num][to_mem - 1] = min(member_score[mem_num][to_mem - 1], score)

        # 큐에 다음 score 멤버를 집어넣는 과정
        for friend in member[to_mem]:
            if member_score[mem_num][friend - 1] == 51:
                q.append([friend, score + 1])  # 집어넣을 때 친구 거리가 추가되므로 1을 증가해준다.


# 멤버 추가 과정
while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    member[a].append(b)
    member[b].append(a)

# 멤버별 친구관계
member_score = [[51] * N for _ in range(N + 1)]
scores = []  # 멤버별 점수

for e in range(1, N + 1):
    bfs(e)

# 멤버별 점수 산정 후 저장
for i in range(1, N + 1):
    scores.append(max(member_score[i]))

# 회장 후보 선정
lowest_score = min(scores)
candidates = [i + 1 for i in range(N) if scores[i] == lowest_score]

print(lowest_score, len(candidates), sep=' ')
print(*candidates)
