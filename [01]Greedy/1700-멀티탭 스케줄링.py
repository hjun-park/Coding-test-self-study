import sys

input = sys.stdin.readline

'''
    참고: https://pacific-ocean.tistory.com/357
'''

'''
 1) 입력값, 그리고 K 개수만큼 플러그 생성
 2) K만큼 루프를 돌기 시작
 3) 또 K만큼 루프를 돌면서 같은 플러그가 이미 꽂힌 경우나 플러그 빈 자리가 있는 경우 플러그를 꽂아줌
 4) 플러그를 꽂았다면 continue, 아니라면 5)를 돈다.
 5) K만큼 루프를 돌기 시작한다.
 6) i+1번째 콘센트부터 끝까지 확인하여 plug[j]가 있는지 확인
 7) plug[j]가 없을수록 -> 뒤에 있을 수록 플러그를 가장 먼저 뽑아야 효율적이다.
 7) plug[j]가 해당 j값으로 플러그 뽑을 위치 변수 선언 후 뽑아줌
 8) 플러그 뽑은 count 증가
'''

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
plug = [0] * N

cnt = 0
for i in range(K):  # index 만큼 반복
    is_plugged = False
    for j in range(N):  # 플러그 개수만큼 반복
        if plug[j] == 0 or plug[j] == numbers[i]:
            is_plugged = True
            plug[j] = numbers[i]
            break
    if is_plugged:
        continue
    else:
        find_index = 0
        for j in range(N):
            try:
                if find_index < numbers[i + 1:].index(plug[j]):
                    find_index = numbers[i + 1:].index(plug[j])
                    plug_index = j
            except:
                find_index = -1
                plug_index = j
                break   # 탐색할 이유 없음
        plug[plug_index] = numbers[i]
        cnt += 1
print(cnt)

# N, K = map(int, input().split())
# numbers = list(map(int, input().split()))
# plug = [0 for i in range(N)]
# cnt = 0
# for i in range(K):
#     isPlug = False
#     for j in range(N):
#         # 플러그가 이미 꽂혀있거나 플러그에 빈 자리가 있는 경우 플러그를 꽂아줌
#         if plug[j] == numbers[i] or plug[j] == 0:
#             isPlug = True
#             plug[j] = numbers[i]
#             break
#     if isPlug:
#         continue
#     else:  # 플러그 뽑아야할 때
#         find_index = 0
#         for j in range(N):
#             try:
#                 # i+1 번째 콘센트부터 확인 ( 그 전에는 이미 루프를 끝난 상태 )
#                 # [플러그 뽑을 위치 탐색] 플러그가 꽂힌 위치(j)가 최대한 뒤에 있어야 플러그 뽑기에 효율있음
#                 if find_index < numbers[i + 1:].index(plug[j]):
#                     find_index = numbers[i + 1:].index(plug[j])
#                     plugged_here = j  # 플러그 꽂을 위치
#             except:  # 인덱스를 찾지 못한 경우 (플러그가 뒤에 없는 경우)
#                 find_index = -1  # 뒤에 플러그가 올 일이 없기 떄문에 in
#                 plugged_here = j  # 플러그 꽂을 위치
#                 break
#         plug[plugged_here] = numbers[i]  # 플러그를 뽑아서 다시 꽂음
#         cnt += 1    # 플러그를 뽑은 횟수 세기
# print(cnt)
