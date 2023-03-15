import string
import sys

input = sys.stdin.readline

'''
  [아이디어]
    - 각 자리의 중요도 기록 
    - A가 100의 자리와 1의 자리에 있다면
    - A의 중요도는 101
    - 알파벳의 개수는 26개이며 모든 알파벳의 중요도를 기록해두기 (0이면 제외)
    - https://hjp845.tistory.com/129
'''

N = int(input())
s_list = []
alpha = dict.fromkeys(string.ascii_uppercase, 0)
# alpha = [0 for i in range(26)]
result = 0

for _ in range(N):
    s_list.append(list(str(input().rstrip())))

for s in s_list:
    # 가중치 초기화
    i = 0

    while s:
        idx = s[-1] # 맨 끝에 1부터 시작
        alpha[idx] += pow(10, i)  # 일의자리부터 가중치 계산
        i += 1
        s = s[:-1]  # 종료조건 만들어주기

alpha_list = sorted(alpha.values(), reverse=True)
# 가중치 리스트
# [10000, 1010, 100, 100, 10, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(9, 0, -1):
    result += i * alpha_list[9 - i]

print(result)

