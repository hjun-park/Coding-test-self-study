'''
    배웠던 것
    1. 리스트 중복값 제거
    2. 딕셔너리 값 추가 방법
    3. 딕셔너리 키, 값 기준으로 정렬하는 방법
    4. 정렬 조건이 2개 이상이라면 lambda를 이용하는 것
'''

import sys
import collections


# return dict value
def f1(x):
    return x[1]

def f2(x):
    return x[0]


N = int(sys.stdin.readline().rstrip())
word_list = []
word_dict = collections.defaultdict(int)

# 입력
for i in range(N):
    word = sys.stdin.readline().rstrip()
    word_list.append(word)

for i in word_list:
    word_dict[i] = len(i)

# # x[0]에 대해서 먼저 정렬 후 x[1]에 대해서 정렬
res = sorted(word_dict.items(), key=lambda x: (f1(x), f2(x)))

for i in res:
    print(i[0])