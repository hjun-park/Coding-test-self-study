from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        missing = len(t)

        left = min_left_ptr = min_right_ptr = 0

        for right in range(1, len(s) + 1):  # 중요: left는 0부터 right는 1부터 시작
            if need[s[right - 1]] > 0:
                missing -= 1

            need[s[right - 1]] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # 이전 저장된 최소 거리보다 더 작은 left, right가 있다면
                if min_right_ptr == 0 or right - left <= min_right_ptr - min_left_ptr:
                    # 갱신
                    min_left_ptr, min_right_ptr = left, right
                    # 먼저 해당 left 조정

                    need[s[left]] += 1
                    # left 조정과
                    left += 1

                    # 이전 값 복구
                    missing += 1

        return s[min_left_ptr:min_right_ptr]
