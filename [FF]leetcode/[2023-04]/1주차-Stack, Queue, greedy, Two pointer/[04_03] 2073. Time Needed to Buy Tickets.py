from typing import List

'''
t = [5, 2, 3, 4, 2], k = 2

1. t[2] 보다 앞인(t[0], t[1])는 t[2]가 0이 되는 순간 이미 지나친 것들이다. (time이 증가된 상태)
    - 따라서 적어도 t[2]이거나 t[앞] 중 최소다. :: min(t[2], t[앞])
2. t[2] 보다 뒤인(t[3], t[4])는 t[2]가 0이 되는 순간 지나치지 않은 것들이다. (time에 반영되지 않음)
    - 그렇기 때문에 t[2]이거나 1을 뺸 값 중 최소다. ::  min(t[2], t[뒤]-1)
   
'''

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            time += min(tickets[i], tickets[k] if i <= k else tickets[k] - 1)

        return time


s = Solution()
print(s.timeRequiredToBuy([2, 3, 2], 2))  # 6
print(s.timeRequiredToBuy([5, 1, 1, 1], 0))  # 8
print(s.timeRequiredToBuy([5, 2, 3, 4, 2], 2))  # 12
