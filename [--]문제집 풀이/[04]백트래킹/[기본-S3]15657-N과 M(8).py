import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

'''
 [함수 정의]
 def logic():
 
 [base condition]
 if len(temp) == M:
    print(*temp)
    return
 
 [recursion] - 오름차순
 
'''

temp = []


def logic(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, N):
        temp.append(nums[i])
        logic(i)
        temp.pop()


logic(0)
