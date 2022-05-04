# 3. [정렬] 두 번째 요소 기준으로 정렬
s = sorted(s, key=lambda a: a[1])

# 4. 리스트 생성 시 일정한 개수만큼 생성해주고 싶을 때
solution_list = ['A' for _ in range(N)]

# 5. 차집합을 이용해서 리스트 생성
_reserve = [r for r in A_list if r not in B_list]

# 6. 중복 제거
d2 = list(set(d))

# 7. 중복제거하고 정렬하지 않기
from collections import OrderedDict

list(OrderedDict.fromkeys(d).keys())

# 15. 조건 2가지 이상의 정렬 할 때는 lambda를 이용하는 것이 좋음
# x[0]에 대해서 먼저 정렬 후 x[1]에 대해서 정렬
coordinate.sort(key=lambda x: (x[0], x[1]))

# 29. 알파벳인 것을 확인하는 방법
if x.isalpha():

# 30. 리스트를 문자열로 바꾸어 출력
print(''.join(result))
print(*result)


# 33. 시뮬레이션 문제 중 좌표 방향을 전환하는 방법
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


# 34. 순열과 조합을 이용하는 방법
# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
from itertools import combinations

candidates = list(combinations(chicken, m))  # 총 리스트 chicken 개수 중에서 m개만을 선택하는 경우
# candidate 값은 좌표가 들어가서 저렇게 나옴, 저렇게 나온 경우는 조합 경우의 수가 5라는 의미
print(f'candidate: {candidates}')  # candidate: [((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),), ((4, 1),)]

# 35. 중복 순열을 이용하는 방법
from itertools import product

# 사칙연산을 사용하기 때문에 중복순열을 사용 => product 라이브러리 사용
n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n - 1))))

# 37. 여러 요소 정렬 더 쉬운 방법 - 한 줄로 정렬이 가능하다.
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 38. 1부터 10000까지 루프를 돌면서 각 자리의 수를 더하는 예제
# # ex) 123 = 1 + 2 + 3
generated_num = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
        generated_num.add(i)

# 40. 집합 자료형에서 x라는 값을 제거함
s.discard(x)

# 44. 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합

# 45. 리스트에서 특정한 값 제거
A.pop(A.index(min(A)))
B.pop(B.index(max(B)))  # 값 -> 인덱스 -> pop

# 47. 해당 인덱스가 영문자거나 숫자인지 확인하는 방법
sl[index].isalnum()

# 48. Counter를 이용하면 문자 개수를 알 수 있음
s = list(map(int, sys.stdin.readline().split()))
cnt = Counter(s)

# 52. 이차원배열(행렬)을 순회하면서 새로운 좌표 리스트 생성 방법
chicken = [[i, j] for i in range(n) for j in range(n) if graph[i][j] == 2]
home = [[i, j] for i in range(n) for j in range(n) if graph[i][j] == 1]

# 53. 행렬(matrix) 최댓값 찾기
max_val = max(map(max, graph))

# 55. 간선이 연결된 경우 서로 대칭해주어 저장해야 한다.
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 56. 없는 인덱스에도 입력받을 수 있도록 하는 리스트 생성
from collections import defaultdict

graph = defaultdict(list)

# 57. [1,2,3,4,5] 입력이 들어왔을 때 1 ~ 4만 리스트에 순수하게 담고 싶을 때
num_list = list(input().rstrip()[1:-1].split(','))

# 50-1. 알파벳 단어사전 생성 (string 패키지 이용)
alpha_dict = dict.fromkeys(string.ascii_uppercase, 0)

# 60. 문자열의 끝을 제거하는 방법
'''
['B', 'A', 'C']
['B', 'A']
'''
s = s[:-1]

# 63. [12886번] 튜플을 이용해서 방문 그래프 작성
visited[tuple(stones)] = True

# 67. 비트 연산
for b in range(1 << N):
    print(b)  # N이 8이라면 2^8 을 의미
    # 만약 2 << N이라면 2^8*2 의미


# 69. 유클리드 호제법
def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod  # y는 나누어지는 수
        mod = x % y
    return y


# 70. 더 짧은 GCD 구하기
# 나머지가 0일 때까지 계속해서 제수를 줄여나간다., 그리고 그걸 리턴
def gcd2(x, y):
    while y:
        x, y = y, x % y
    return x


# 71. 유클리드 호제법 LCM
# 곱 & GCD
def lcm(x, y):
    return (x * y) // gcd(x, y)


# 71-1. 여러개의 최소공배수를 구하기 위해서는 (A, B, C) 있다고 가정
# A-B 최소공배수 구하고 그 구한 값과 C의 최소공배수를 구한다.

# 72. collections deque는 rotate함수가 있어서 편하게 사용할 수 있다.
l = deque([0, 1, 1, 1, 1])
l.rotate(1)

# 73. [14890] 행과 열을 각각 연산하는 방법
for i in range(N):
    cnt += check_level(graph[i])  # 행
    cnt += check_level([row[i] for row in graph])  # 열

# 74. append와 extend의 차이점 (extend는 확장)
x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y)
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('x:', x)

'''
출력 결과
x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]
x: ['Tick', 'Tock', 'Song', 'Ping', 'Pong']
'''

# 77. 이차원배열 가로, 세로 사이즈
print(len(graph[1]))  # 세로
print(len(graph))  # 가로

# 78. 딕셔너리 관련한 함수
# https://gomguard.tistory.com/126
# 예제
from collections import defaultdict

graph = [2, 1, 1, 3, 5, 3]
num_dict = defaultdict(int)

for key in graph:
    num_dict[key] += 1

arr = (sorted(num_dict.items(), key=lambda x: x[1]))

# 79. 행과 열을 바꾸는 방법
if len(graph) < len(graph[0]):
    graph = list(zip(*graph))  # zip을 이용하면 행과 열 바꿀 수 있음

# 80. Counter 모듈 사용법
from collections import Counter

# 0을 배제 후 재 정렬하는 작업
a = [i for i in graph[j] if j != 0]  # 0의 경우 미리 배제
a = Counter(a).most_common()  # 배제 후 각 숫자가 몇 개 있는지 센다 (리턴: 딕셔너리)
# 어떠한 수가 몇개 인지를 딕셔너리로 표현
a.sort(key=lambda x: (x[1], x[0]))  # 딕셔너리를 value먼저 이후 key 기준으로 정렬한다.
graph[j] = []  # 행을 초기화한다.


# 81. 함수를 이용해서 정렬도 가능하다.
def sum_num(arr):
    result = 0
    for num in arr:
        if num.isdigit():
            result += int(num)
    return result


# 함수를 이용해서 정렬도 가능하다.
serial.sort(key=lambda x: (len(x), sum_num(x), x))

# 82. DFS에서 한방향씩 트는게 아닌 끝까지 가는 경우라면
#  이 방식보다
for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]

# 이 방식이 낫다.
while True:
    if '범위초과 시':
        d += 1  # 방향을 틀어준다.
        continue

# 83. 2차원 배열의 가로세로를 바꾸어주는 방법
col_check = list(map(list, zip(*check)))

# 85. 배수를 비교할 때는 절반까지만 비교해도 됨
for i in range(1, (len(switch) // number) + 1):
    if switch[(number * i) - 1] == 1:
        switch[(number * i) - 1] = 0
    else:
        switch[(number * i) - 1] = 1

# 86. 2차원 배열 합 구하는 방법
dividend = sum(map(sum, graph))
ice = sum(sum(graph, list))

# 87. 하나의 리스트에 여러 값을 추가하는 방법
temp = []
a = [1, 2]
b = [3, 4]

temp += (a, b)


# 99. 이차원행렬 곱셈
def solution(arr1, arr2):
    # zip : 두 그룹의 데이터를 묶어준다.( 즉, 두 리스트에 있는 값을 하나하나 엮어서 튜플로 만들어준다. )
    #   만약 두 그룹의 데이터 사이즈가 다르다면 더 많은 쪽에 있는 것이 연산에 버려지게 된다.
    #   zip(*) 을 이용하면 행과 열을 서로 바꾸어준다. ( B열에 접근하기 위해 행과 열을 바꾸어준 것 )
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*arr2)] for A_row in arr1]


# 100.
# 연속된 수의 합으로 N을 만들기 위한 방법
# 1) 1부터 N까지 수에서 홀수 중에서도 N과 나눠서 나머지가 0인 수들을 세면 표현식이 나온다.
def solution(n):
    return len([x for x in range(1, n + 1, 2) if n % x == 0])


# 101. 이진법 변환 방법
string_bin = format(n, 'b')

# 102. 숫자 개수 카운트 하는 방법
from collections import Counter

a = [1, 2, 1, 1, 3, 4]
dic = Counter(a)

# 103. 두 번 뒤집는 것은 아예 안 뒤집은 것 하고 똑같다.
#      여러 번 뒤집는 문제의 경우 뒤집지 말고 그 count를 세어서 count 홀/짝 여부에 따라 뒤집기 여부를 결정한다.

# 104. copy()는 1차원 배열, deepcopy()는 2차원 배열에서 사용한다.
from copy import deepcopy
a = [1, 2]
b = [[1, 2], [3, 4]]
copied_a = a.copy()
copied_b = b.deepcopy()

# 105. split에도 list comprehension 사용
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]
for q in query:
    row = [x for x in q.split() if x != 'and' and x != '-']
    print(row)

# 106. 시간계산 하는 방법
from datetime import datetime

st = '01:10'
en = '02:20'
start = datetime.strptime(st, "%H:%M")
end = datetime.strptime(en, "%H:%M")

diff = end - start


