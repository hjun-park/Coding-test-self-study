'''
한글자씩 확인하면서 이미 앞에서 나온 문자면,
해당 위치보다 1칸 뒤의 문자열에서 자른다. (중복된 수보다 1칸 뒤)

그렇지 않다면 문자열 뒤에 append.
매 단계마다 _max를 지정,
 마지막으로 return _max
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        # 1. 가장 긴 부분문자열
        words = []
        _max = 0

        # 2. s를 순차적으로 순회
        for x in s:
            # 1. 값이 중복된다면
            if x in words:
                # 1. 중복 문자 이후의 값으로 다시 words 지정
                words = words[words.index(x) + 1:]

            # 2. 이후 right 문자열 지정
            words.append(x)

            # 3. 최댓값 지정
            _max = max(_max, len(words))

        return _max
