from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = []

        def recursion(x, bracket):
            # 1) base condition
            if x == 0:
                # print(f'bracket -> {bracket}')
                if isCorrect(bracket):
                    brackets.append(bracket)
                return

            # 2) recursion logic
            recursion(x - 1, bracket + '(')
            recursion(x - 1, bracket + ')')

        def isCorrect(bracket) -> bool:
            mid = 0

            for b in bracket:
                if b == '(':
                    mid += 1
                elif b == ')':
                    mid -= 1
                if mid < 0:
                    return False

            if mid != 0:
                return False

            return True

        recursion(n*2, '')

        return brackets


s = Solution()
print(s.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(1))  # ["()"]
print(s.generateParenthesis(8))
