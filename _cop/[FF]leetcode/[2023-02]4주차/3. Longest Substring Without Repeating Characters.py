from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 1. s가 아무것도 없으면 길이 0
        if len(s) == 0:
            return 0

        # 2. 단어 세는 딕셔너리 선언
        words = defaultdict(int)
        _max = -1

        # 3. left, right 포인터 초기화
        left = right = 0

        # 4. 오른쪽 포인터부터 탐색 시작
        for right in range(len(s)):
            # 1. 오른쪽 포인터가 지나는 문자 count
            words[s[right]] += 1

            # 2. 중복으로 센 문자열이 있으면 왼쪽 포인터를 중복문자열까지 while 실행
            while words[s[right]] > 1 and left < len(s):
                # 1. left가 지나가는 문자는 count-1
                words[s[left]] -= 1

                # 2. left 포인터 움직임
                left += 1

            # 3. 오른쪽 한 턴 지나면 _max 값 구하기
            #    문자의 개수를 세기 위해 +1
            #    ex) 0 1 2 3 는 4개인데 3-0 = 3이니까 3-0+1 = 4 조정
            _max = max(_max, right - left + 1)

        return _max


print(Solution().lengthOfLongestSubstring('bbbbb'))
print(Solution().lengthOfLongestSubstring('abcabcbb'))
print(Solution().lengthOfLongestSubstring('pwwkew'))
