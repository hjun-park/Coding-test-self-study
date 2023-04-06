class Solution:
    def runPalindrome(self, s: str, left: int, right: int, change_cnt: int):
        # 1. 1번 이상은 단어 제거 불가
        if change_cnt > 1:
            return False

        # 2. 투포인터 시작
        while left < right:
            # 1. 만약 다르면 단어 제거 후 다시 펠린드롬 진행
            if s[left] != s[right]:
                return self.runPalindrome(s, left + 1, right, change_cnt + 1) or self.runPalindrome(s, left, right - 1, change_cnt + 1)
            # 2. 같다면 계속 진행
            else:
                left += 1
                right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        return self.runPalindrome(s, 0, len(s) - 1, 0)


ss = Solution()
# print(ss.validPalindrome("aba"))  # true
# print(ss.validPalindrome("abca"))  # true
print(ss.validPalindrome("abc"))  # false
print(ss.validPalindrome("abaccada"))  # true
print(ss.validPalindrome("deeee"))  # true
print(ss.validPalindrome("atbbga")) # False
