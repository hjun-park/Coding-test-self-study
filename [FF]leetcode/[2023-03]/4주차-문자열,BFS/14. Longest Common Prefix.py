from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 2. 가장 짧은 문자를 빨리 꺼내기 위해서 sorting 하고 시작한다.
        # 3. sorting하면 [0] 인덱스로 가장 짧은 문자열을 빠르게 꺼낼 수 있다.
        # _len = min([len(x) for x in strs])
        strs.sort(key=lambda x: len(x))

        if len(strs) <= 0:
            return ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]

        # 1. loop를 빠져나온 경우는 가장 짧은 문자열을 모두 순회했다는 의미
        return strs[0]


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix([""]))
print(s.longestCommonPrefix(["a"]))
print(s.longestCommonPrefix(["ab", "a"]))
