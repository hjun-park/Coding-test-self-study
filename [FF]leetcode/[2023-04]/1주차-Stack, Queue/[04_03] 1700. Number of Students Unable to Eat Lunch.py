from collections import Counter
from typing import List

'''
문제풀이 2가지 방법
1. 스택, 큐를 써서 직접 구현
2. 그리디로 접근

- 학생은 매번 번갈아가면서 순서가 바뀐다.
- 샌드위치는 순서가 바뀌지 않는다.
- 이 얘기는 즉, 샌드위치는 가만히 있고 줄 상관 없이 원하는 학생이 가져가게 될 것이다.
- 하지만 샌드위치 순서는 변하지 않기 떄문에 원하는 학생이 없는 샌드위치의 경우 남은 학생들은 모두 샌드위치를 먹지 못한다. 
'''


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)   # 원하는 샌드위치별로 학생 수 구하기 (0, 1)

        # 1) 샌드위치를 순회하면서 이를 원하는 학생이 있는지 확인
        for sandwich in sandwiches:
            # 2) 샌드위치를 원하는 학생이 있는 경우 빼기 (학생은 샌드위치를 가져감)
            if c[sandwich]:
                c[sandwich] -= 1
            # 3) 샌드위치를 원하는 학생이 없는 경우 탈출 (샌드위치는 순서가 바뀌지 않기 때문에 남아 있는 학생들도 먹지 못함)
            else:
                break

        return sum(list(c.values()))


s = Solution()
print(s.countStudents([1, 1, 0, 0], [0, 1, 0, 1]))                 # 0
print(s.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))     # 3
