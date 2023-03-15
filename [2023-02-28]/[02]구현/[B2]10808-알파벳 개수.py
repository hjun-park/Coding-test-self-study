# 첫 번째 풀이 (2020-05-04)  -> for문 난사
string = list(input())

alphabets = []

for _ in range(26):
    alphabets.append(0)

for s in string:
    alphabets[ord(s) - 97] += 1

for i in alphabets:
    print(i, end=' ')

# =========================================================================================================

# 두 번째 풀이 (2021-08-05) -> Counter 패키지
import sys
from collections import Counter  # Counter 패키지는 리스트 각 원소의 개수를 세는 데 사용

str_list = list(sys.stdin.readline().rstrip())
count_list = Counter(str_list)  # Counter({'o': 2, 'b': 1, 'a': 1, 'e': 1, 'k': 1, 'j': 1, 'n': 1})

for i in range(ord('a'), ord('{')):
    result = count_list.get(chr(i))
    if result is None:
        print('0', end=' ')
    else:
        print(result, end=' ')

# =========================================================================================================


# 세 번째 풀이 (2022-02-03) -> string 패키지
import sys
import string

input = sys.stdin.readline

S = list(input().rstrip())

# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)

for c in S:
    alpha_dict[c] += 1

# 딕셔너리 값 뽑는 3가지 방법
print(*alpha_dict.values())  # 값만 출력
