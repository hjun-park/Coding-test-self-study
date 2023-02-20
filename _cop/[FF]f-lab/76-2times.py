import sys
from collections import Counter

input = sys.stdin.readline

s = 'ADOBECODEBANC'
t = 'ABC'

'''
1. two pointer로 선정할 left, right 지정
2. t에 대한 counter와 length 구하기
3. s를 순회하면서 left와 right 사이에 모든 t가 들어올 때까지 right를 움직임
    3-1. 모든 t가 들어왔다면 (len_t == 0) left를 움직임
    3-2. left를 움직이면서 t에 존재하는 문자열을 만났다면 stop
    3-3. left, right와 min_left_ptr, min_right_ptr 비교해서 최소인 쪽으로 담아주기 
    3-4. left += 1, len_t += 1 이후 3번 다시 시작
'''

ctr_t = Counter(t)
len_t = len(t)

left = min_left_ptr = min_right_ptr = 0

for right in range(1, len(s)):  # 중요: left는 0부터 right는 1부터 시작
    if ctr_t[s[right]] > 0:
        len_t -= 1
    ctr_t[s[right]] -= 1

    if len_t == 0:
        while left < right and ctr_t[s[left]] < 0:
            ctr_t[s[left]] += 1
            left += 1

        # 이전 저장된 최소 거리보다 더 작은 left, right가 있다면
        if min_right_ptr == 0 or right - left <= min_right_ptr - min_left_ptr:
            # 갱신
            min_left_ptr, min_right_ptr = left, right

            # left 조정하면서
            left += 1

            # 이전 값 복구
            len_t += 1
            ctr_t[s[left]] += 1

print(min_left_ptr, min_right_ptr)
print(s[min_left_ptr:min_right_ptr])



