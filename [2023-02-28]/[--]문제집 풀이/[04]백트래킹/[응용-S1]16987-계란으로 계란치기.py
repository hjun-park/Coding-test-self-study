import sys

input = sys.stdin.readline

N = int(input().rstrip())
eggs = [list(map(int, input().split())) for _ in range(N)]
result = -1
S, W = 0, 1  # eggs[0]은 내구도, eggs[1]은 무게
# 참고 : https://kjhoon0330.tistory.com/entry/BOJ-16987-%EA%B3%84%EB%9E%80%EC%9C%BC%EB%A1%9C-%EA%B3%84%EB%9E%80%EC%B9%98%EA%B8%B0-Python

'''
    [요약] 내구도 / 무게
    1. 각 계란에는 내구도 S와 무게 W가 존재
    2. A계란을 가지고 B계란을 치게 되면, 계란 서로서로 S와 W가 각각 깎이게 된다.
    3. 내구도가 0이하가 되는 순간 계란은 깨진다.
    
    - 계란을 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깬다.
    
    
    [function]
    def logic(idx):
     - idx : 깰 계란의 index
     - eggs: 계란 상태정보        
    
    [base condition]
    if idx == N:   # 가장 깰 계란의 오른쪽이라면 (끝가지 돈 경우)
        # 계란에서 내구도가 0 이하인 계란들의 개수를 센 후 (cnt)
        # result와 cnt 중 가장 큰 것을 반영
        # return
    
    [recursion logic]
    1. 만약 자기 자신이 깨져 있으면 다음 계란으로 logic(idx + 1)
    2. 루프를 순회해서 자기 자신 외에 모든 달걀이 다 깨져 있다면 마찬가지로 max 변경 후 return
    
    3. 1-2 조건을 만족하지 않는다면 recursion logic 시작
     3-1) n만큼 루프 돌면서 i와 idx인 자기자신과 같다면 continue
     3-2) 만약 때리려는 상대 계란이 이미 내구도가 0보다 같거나 작아도 continue
     3-3) 3-1과 3-2를 수행하지 않았다면 계란을 떄리고 복구하는 백트래킹 로직
        
'''


def logic(idx):
    global result

    # [base condition] - 0
    if idx == N:
        cnt = 0
        for i in range(N):
            if eggs[i][S] <= 0:
                cnt += 1

        result = max(result, cnt)
        return

    # [base condition] - 1 자기 자신이 꺠져 있으면 다음 달걀로
    if eggs[idx][S] <= 0:
        logic(idx + 1)
        return

    # [base condition] - 2 루프 순회해서 자기 자신 외 모든 달걀이 깨져 있으면 max값 갱신 후 종료
    all_crashed = True
    for i in range(N):
        if i == idx:
            continue
        if eggs[i][S] > 0:  # 깨져있지 않은 달걀이 있으면
            all_crashed = False
            break

    if all_crashed:
        result = max(result, N - 1)
        return

    # 3. 1-2 조건을 만족하지 않는다면 recursion logic 시작
    #  3-1) n만큼 루프 돌면서 i와 idx인 자기자신과 같다면 continue
    for i in range(N):
        if i == idx:
            continue

        #  3-2) 만약 때리려는 상대 계란이 이미 내구도가 0보다 같거나 작아도 continue
        if eggs[i][S] <= 0:
            continue

        #  3-3) 3-1과 3-2를 수행하지 않았다면 계란을 떄리고 복구하는 백트래킹 로직
        eggs[idx][S] -= eggs[i][W]
        eggs[i][S] -= eggs[idx][W]
        logic(idx + 1)
        eggs[idx][S] += eggs[i][W]
        eggs[i][S] += eggs[idx][W]


logic(0)
print(result)
