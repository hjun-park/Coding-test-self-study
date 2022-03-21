import sys

input = sys.stdin.readline

N = int(input())
lines = list(tuple(map(int, input().split())) for _ in range(N))
# lines = sorted([list(map(int, input().split())) for _ in range(N)])
lines.sort()

start, end = lines[0][0], lines[0][1]
cnt = 0

for i in range(1, N):
    now_start, now_end = lines[i]

    # 1) 두 선분이 겹치면서 앞의 end가 더 앞서는 경우
    if end > now_start:
        end = max(end, now_end)

    # 2) 두 선이 겹치면서 꺼낸 도착점(now_end)이 end보다 더 이른 경우
    # 그대로 둔다

    # 3) 두 선이 겹치지 않는 경우 => 선분 길이 반영 and (start, end) 업데이트
    else:
        cnt += (end - start)  # 선분 길이 반영
        start, end = now_start, now_end  # start, end 업데이트

# ========================
# 시간 초과된 풀이 - 사실 별 차이 없음, 파이썬이라 시간초과 나는 듯하다.
# =========================
# while lines:
#     s, e = lines.pop(0)
#
#     if s <= end:
#         end = e  # end 갱신
#     else:  # 선분이 중간에 끊기는 경우
#         cnt += end - start  # 선분 총 길이 반영
#         start = s  # 새로 셋팅
#         end = e

# 마지막 남은 선분 처리
cnt += (end - start)
print(cnt)
