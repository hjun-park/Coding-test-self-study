import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

'''
 [함수 정의]
 def logic()
 
 [base condition]
 if M == len(temp):
    print(*temp)
    return
 
 
 [함수 로직]
 for i in range(N):
    if nums[i] in temp:
        continue
    
    temp.append(nums[i])
    logic()
    temp.pop()
'''

temp = []
visited = [False] * N


def logic():
    if M == len(temp):
        print(*temp)
        return

    before = 0
    for i in range(len(nums)):
        if visited[i] or before == nums[i]:
            continue

        visited[i] = True
        temp.append(nums[i])
        before = nums[i]
        logic()
        visited[i] = False
        temp.pop()


logic()
