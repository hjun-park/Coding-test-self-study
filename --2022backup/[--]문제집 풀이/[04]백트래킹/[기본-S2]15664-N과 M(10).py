import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# nums = sorted(list(set(list(map(int, input().split())))))
nums = sorted(list(map(int, input().split())))

'''
    [함수 정의]
    def logic():
    
    [base condition]
    if len(temp) == M:
        print(*temp)
        return
    
    # 중복 X / 
    [로직]
    for i in range(N):
        
    

'''

temp = []
visited = [False] * N


def logic(start):
    if M == len(temp):
        print(*temp)
        return

    before = 0
    for i in range(start, len(nums)):
        if visited[i] or before == nums[i]:
            continue

        visited[i] = True
        temp.append(nums[i])
        before = nums[i]
        logic(i + 1)
        visited[i] = False
        temp.pop()


logic(0)
