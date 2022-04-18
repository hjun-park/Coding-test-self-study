import re

# ===== 내 코드 =====
# def solution(dartResult):
#     nums = re.findall('\d+', dartResult)
#     _strings = re.findall('[a-zA-Z*#]+', dartResult)
#
#
#     # print(nums)
#     # print(_strings)
#     score = []
#     for i in range(len(nums)):
#
#         if _strings[i][0] == 'S':
#             score.append(int(nums[i]) ** 1)
#         elif _strings[i][0] == 'D':
#             score.append(int(nums[i]) ** 2)
#         elif _strings[i][0] == 'T':
#             score.append(int(nums[i]) ** 3)
#
#         # print(i, score)
#         if _strings[i][-1] == '*':
#             if i == 0:
#                 score[i] *= 2
#             else:
#                 score[i - 1] *= 2
#                 score[i] *= 2
#
#         elif _strings[i][-1] == '#':
#             score[i] = -score[i]
#
#     return sum(score)


# ===== 모범 답안 =====
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    # 정규표현식 좋은 예제
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

print(solution('1S2D*3T10S#'))
print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))
