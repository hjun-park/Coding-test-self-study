import sys

n, l = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

tape = 1 # 처음 붙일 땐 한 장으로 시작
start = position[0]

# 시작지에서 테이프 더 한 끝점까지
end = start + l - 0.5

for p in position:
    # 1. 끝점을 봤을 때 물이 새는 곳이 커버가 가능한 경우라면
    if end >= p:
        continue
    else:   # 2. 커버할 수 없는 경우 새로운 테이프 추가 그리고 end 값 갱신 ( 테이프길이 + 끝점위치 )
        tape += 1
        end = p + l - 0.5


print(tape)






