import sys

input = sys.stdin.readline

'''
: s = “ADOBECODEBANC”, t = “ABC”
: “BANC”
'''


'''
가장 왼쪽을 기준으로 오른쪽 옮겨가며 처음으로 substring 찾기

왼쪽 땡겨주며 substring이 유지되는 최소길이 찾기
substring깨지면 슬라이딩 윈도우하면서 더 짧은 substring찾기

오른쪽 끝에 닿으면
substring있다면 왼쪽으로 쭉땡겨서 최종 substring찾기
substring없다면 끝내기

ADOBECODEBANC
ABC

이 문제는 O(n) 안에 풀어야 하는 문제로,
 투포인터와 슬라이딩 윈도우를 사용했다.
  우선 첫 번째 for문을 돌면서,
   s 문자열 안에 t 문자열 중 하나가 매칭될 때마다
    missing은 하나씩 줄어들도록 하고,
     need Counter는 매칭되는 문자는 0,
      매칭되지 않는 문자는 음수 값을 갖도록 만든다.
       이후, missing이 0이 되는 순간 
       (t의 모든 문자가 s에서 모두 발견), 
       필요 없는 문자 (음수) 에서 벗어날 때까지 
       left를 1개씩 늘리면서 윈도우의 크기를 줄인다.
        (최소 윈도우를 구해야 하기 때문)  
        이후 s 문자열에서 start ~ end까지의
         문자를 슬라이싱해 return한다. 

'''

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)  # 필요 문자 카운팅
        missing = len(t)  # 필요 문자 length
        left = min_ptr = max_ptr = 0

        # 2. 오른쪽으로 이동
        for right, char in enumerate(s, 1):  # right는 1부터 시작
            # 1. 현재 문자(char)가 필요한 문자(need[char])에 포함돼 있다면 필요 문자 length 감소
            missing -= need[char] > 0

            # 2. 감소 시켰으니 필요한 문자(need[char])도 감소
            #    만약 need에 없는 문자라면 음수가 됨 (-1, -2 .... )
            need[char] -= 1

            # 3. right를 움직여 모든 문자를 다 찾았다면 left를 줄일 차례
            if missing == 0:
                # 1. left index를 포함하는 문자가 있을 때까지 움직임
                while left < right and need[s[left]] < 0:
                    # 1. 포함개수 증가
                    need[s[left]] += 1
                    # 2. left pointer를 움직임
                    left += 1

                # 2. e - left : 현재 조정 중인 값 ( two pointer )
                #    end - start :  저장된 최소 길이
                #    즉, 저장된 최소 길이보다 더 작은 투포인터 값이 나왔다면
                if not max_ptr or right - left <= max_ptr - min_ptr:
                    min_ptr, max_ptr = left, right
                    need[s[left]] += 1
                    left += 1  # 다음 짧은걸 찾기 위해 left 다음 값으로 조정
                    missing += 1  # left는 need에 있었는데 빠져나왔으므로 missing 1 복구

        return s[min_ptr:max_ptr]


solution = Solution()
print(solution.minWindow('ADOBECODEBANC', 'ABC'))
