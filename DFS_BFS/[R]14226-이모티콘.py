import sys
from collections import deque

input = sys.stdin.readline


# 저장, 붙여넣기 (화면 -> 클립보드)
# 화면 이모티콘 1개 삭제  => 모두 1초
# https://vixxcode.tistory.com/34

def bfs(left, right):
    queue = deque()
    queue.append((left, right))
    time[left][right] = 0

    while queue:
        emo, clip = queue.popleft()

        # 원하는 만큼 이모티콘 사용
        if emo == S:
            break

        # 클립보드가 있다면
        if clip:
            # 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
            if time[emo+clip][clip] == -1 and emo+clip <= S:
                queue.append([emo+clip, clip])
                time[emo+clip][clip] = time[emo][clip] + 1

            # 화면에 있는 이모티콘 복사하여 클립보드 저장
            if time[emo][emo] == -1:    # 두번째 인덱스 clip이 emo로 변함 ( 복사한 상태 )
                queue.append([emo, emo])
                time[emo][emo] = time[emo][clip] + 1    # 클립에서 이모 복사 => 1초 추가

            # 화면에 있는 이모티콘 중 하나 삭제
            if time[emo-1][clip] == -1 and emo-1 > 0:
                queue.append([emo-1, clip])
                time[emo-1][clip] = time[emo][clip] + 1

        # 클립이 없다면 무조건 이모티콘 모두 복사해서 클립에 넣는게 이득
        else:
            queue.append([emo, emo])
            time[emo][emo] = time[emo][clip] + 1




S = int(input())
time = [[-1] * 3000 for _ in range(3000)]
answer = 1e9
bfs(1, 0)   # bfs(처음 이모티콘 개수, 클립보드 사이즈)
for i in range(S+1):
    if time[S][i] != -1:
        answer = min(answer, time[S][i])

print(answer)


