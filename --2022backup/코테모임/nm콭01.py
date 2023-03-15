import sys

input = sys.stdin.readline


# 지그재그 수열
# 어떤 S가 주어질 때, 숫자를 추가해서 지그재그로 만들려고 함
# [구할 것] s를 지그재그로 만들기 위해 추가해야 하는 수의 최솟값


def solution(s):
    cnt = 0
    _len = len(s)

    for i in range(_len - 1):
        if i % 2 == 0:
            if s[i] >= s[i + 1]:
                cnt += 1
        else:
            if s[i] <= s[i + 1]:
                cnt += 1

    return cnt


print(solution([1, 2, 3]))
print(solution([3, -1, 0, 4]))
