import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

'''
  [함수 정의]
  def logic(depth, idx):
    depth : M까지 진입
    idx : 인덱스값 
  
  [base condition]
  if depth = M:
    if sorted(li) == li:
        print(*li)
    return
    
  
  [recursion logic]
  for i in range(idx, N):
    logic(depth + 1, i+1)
    
    
      
  
'''

temp = []


def logic(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, N):
        if nums[i] not in temp:
            temp.append(nums[i])
            logic(i + 1)
            temp.pop()


logic(0)
