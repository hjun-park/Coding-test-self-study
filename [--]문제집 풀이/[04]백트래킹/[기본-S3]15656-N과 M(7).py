import sys

input = sys.stdin.readline

'''
    [정의]
    def logic(start):
      - start: 
        
    
    [종료]
    if len(temp) == M:
        print(*temp)
        return 
   
    
    [로직]
    for i in range(start, N):
        temp.append(nums[i])
        logic(i+1)
        temp.pop()
'''

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

temp = []


def logic():
    if len(temp) == M:
        print(*temp)
        return

    for i in range(N):
        temp.append(nums[i])
        logic()
        # logic(i + 1)
        temp.pop()


logic()
