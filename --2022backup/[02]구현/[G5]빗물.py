import sys

input = sys.stdin.readline

'''
    https://jminie.tistory.com/106
    # 투포인터 비슷한 개념을 활용
    1) 왼쪽, 오른쪽 양 끝을 left, right 선정
    2) 왼쪽, 오른쪽 양 끝 블럭 높이를 left_max, right_max로 지정
    3) 두 포인터가 만날 때까지 진행 
      3-1) max(height[left], left_max) max(height[right], right_max) 를 지정한다. 
      3-2) left, right max값 비교해서 작은 값의 포인터를 움직여주고 빗물 높이를 구한다.  
    4) 그렇게 하면 가운데 가장 큰 max 높이에 다다른 쪽은 포인터가 움직이지 않게 된다.

'''
H, W = map(int, input().split())
height = list(map(int, input().split()))
rainwater = 0

# 1), 2)
left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]

# 3)
while left < right:
    # 3-1)
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])

    # 3-2) 작은 쪽의 빗물을 계산하고 포인터도 움직여준다.
    if left_max <= right_max:
        rainwater += left_max - height[left]
        left += 1

    else:
        rainwater += right_max - height[right]
        right -= 1

print(rainwater)
