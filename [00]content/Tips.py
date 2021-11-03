# 1. 입력값을 여러 개 받고싶을 때
n, m, k = map(int, input().split())         # 일반
data = list(map(int, input().split()))      # 리스트로 저장
data2 = list(int(input()) for _ in range(N)) # 여러 개 문장

# 2. 개수만큼 입력을 받아 순서 쌍으로 저장
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

# 3. 두 번째 요소 기준으로 정렬
s = sorted(s, key=lambda a: a[1])

# 4. 리스트 생성 시 일정한 개수만큼 생성해주고 싶을 때
solution_list = [ 'A' for _ in range(len(input_list))]

# 5. 차집합을 이용해서 리스트 생성
_reserve = [r for r in reserve if r not in lost]

# 6. 중복제거하고 정렬
d2 = list(set(d))

# 7. 중복제거하고 정렬하지 않기
from collections import OrderedDict
list( OrderedDict.fromkeys(d).keys())

# 8. 이차원 정사각 행렬 입력받기
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]

# 9. 2차원 행렬, 좌표문제 풀 때는 dx, dy 리스트를 선언해주어서 접근해보기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 10. 재귀 한도 해제
import sys
sys.setrecursionlimit(10000)    # 재귀 한도를 풀어줌

# 11. 파이썬 기본 라이브러리 이용하여 역순 정렬
array = sorted(array, reverse=True)

# 12. 키를 이용하여 점수를 기준으로 정렬
array.append((input_data[0], int(input_data[1])))
array = sorted(array, key = lambda student: student[1]) # array에서 2번째 인자 기준으로 정렬

# 13. 많은 값들을 입력 받을 때 빠르게 입력받으려면 sys 라이브러리 사용
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)

# 14. 두 개의 좌표를 입력받는 방법
for i in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().split())))

# 15. 조건 2가지 이상의 정렬 할 때는 lambda를 이용하는 것이 좋음
# x[0]에 대해서 먼저 정렬 후 x[1]에 대해서 정렬
coordinate.sort(key=lambda x: (x[0], x[1]))

# 16. 2차원 배열 입력받아서 생성하는 방법
for i in range(X):
    wb_list.append([i for i in sys.stdin.readline().rstrip()])

# 17. 각 컬럼마다 한번씩 접근해서 2차원 행렬의 값을 불러오는 방법
sliced_matrix = [x[col:col + 8] for x in wb_list[row:row + 8]]


# 18. 리스트 거꾸로 출력
num[::-1] == num # (num은 그냥 숫자)

# 19. 큐에서 리스트를 각 원소별로 관리하기에는 deque가 좋음
from collections import deque
num_queue = deque([x for x in range(1, N+1)])
temp = num_queue.popleft()

# 20. deque에서 특정 원소 개수 세기 위해서,
#     리스트와 함께 사용한다.
s = deque([])

# 21. 큐에 대한 루프를 돌 때는 사이즈로 도는 것이 아니라
#      while 문을 써서 전체가 빌 때까지로 해본다.
while s: ... # <== deque는 이렇게 루핑돌리기

# 22. 2차원 배열을 이용하는 문제에서 굳이 2차원 배열 만들 필요가 없으면 행 하나씩 비교하는 방법으로 처리
for i in range(n):
    data = list(map(int, sys.stdin.readline().split()))

# 23. ascii 문자를 정수로 변환
int(ord('a'))

# 24. list comprehension 을 이용하여 2차원 행렬의 초기화 ( n x m )
d = [[0] * m for _ in range(n)]
graph = [[] for _ in range(n + 1)]  # 2차원 배열 ( N x N )


# 25. N * M 2차원 배열 입력받기 ( 리스트 형식 )
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# 26. 한 번에 입력받을 때 split을 이용하여 하나의 변수에 모두 담을 수 있음
input_data = sys.stdin.readline().rstrip().split()

# 27. 계수정렬에서 반복문을 split으로 입력받을 수 있음
for i in input().split():
    array[int(i)] = 1

# 28. 2차원 리스트(그래프 표현) 만든 후 모든 값 무한으로 초기화
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

# 29. 알파벳인 것을 확인하는 방법
if x.isalpha():

# 30. 리스트를 문자열로 바꾸어 출력
print(''.join(result))

# 31. 좌표 입력받는 방법
for _ in range(L):
    x, c = map(int, input().split())
    info.append((int(x), c))

# 32. 좌표 입력받는 방법 2
for i in range(k):
    a, b = map(int, input().split())
    apple[a][b] = 1

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
print(f'candidate: {candidates}')   # candidate: [((0, 1),), ((1, 1),), ((2, 1),), ((3, 1),), ((4, 1),)]

# 35. 중복 순열을 이용하는 방법
from itertools import product
# 사칙연산을 사용하기 때문에 중복순열을 사용 => product 라이브러리 사용
n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n - 1))))

# 36. 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 37. 더 쉬운 방법 - 한 줄로 정렬이 가능하다.
data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 38. 1부터 10000까지 루프를 돌면서 각 자리의 수를 더하는 예제
# # ex) 123 = 1 + 2 + 3
generated_num = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
        generated_num.add(i)

# 39. 리스트에 해당 수가 들어간 개수가 몇 개인지 number[i]에 집어넣음
number[i] = n.count(str(i))

# 40. 집합 자료형에서 x라는 값을 제거함
s.discard(x)

# 41. 리스트 컴프리헨션
# 0부터 19까지 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
# 1부터 9까지의 수 중 제곱 값만을 포함하는 리스트
array = [i * i for i in range(1, 10)]

# 42. N*M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]

# 43. 딕셔너리 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

if '사과' in data:
    print("사과를 키로 가지는 데이터가 존재합니다")

key_list = data.keys() # 키 데이터만 담긴 리스트
value_list = data.values() # 값 데이터만 남긴 리스트

# 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 44. 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 45. 리스트에서 특정한 값 제거
A.pop(A.index(min(A)))
B.pop(B.index(max(B))) # 값 -> 인덱스 -> pop

# 46. 리스트
ps_list = list(map(str, input())) # 요소 하나하나 들어감
ps_list_merge = list(map(str, input().split()))   # 요소 전체를 하나로 묶어 집어넣음

# 47. 해당 인덱스가 영문자거나 숫자인지 확인하는 방법
sl[index].isalnum()

# 48. Counter를 이용하면 문자 개수를 알 수 있음
s = list(map(int, sys.stdin.readline().split()))
cnt = Counter(s)

# 49. 리스트의 모든 내용을 출력하는 방법
print(*result)

# 50. 알파벳 리스트를 만드는 방법
import string
str_list = list(sys.stdin.readline().rstrip())
alpha_list = string.ascii_lowercase
alpha_dict = dict.fromkeys(alpha_list, -1)

# 51. DP에서 0부터 시작이 아닌 i+1부터 값을 담고 싶다면
p = [0] + list(map(int, sys.stdin.readline().split()))

# 52. 이차원배열(행렬)을 순회하면서 새로운 좌표 리스트 생성 방법
chicken = [[i, j] for i in range(n) for j in range(n) if graph[i][j] == 2]
home = [[i, j] for i in range(n) for j in range(n) if graph[i][j] == 1]

# 53. 행렬(matrix) 최댓값 찾기
max_val = max(map(max, graph))

# 54. DFS 방문 기록 관련 히스토리 리스트 선언
history = [[False] * m for _ in range(n)]

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

# 58. BFS 에서 가중치를 이용할 수 있는데, 비교 후 큐에 집어넣을 때
# 가장 먼저 빨리 빼고 싶다면 appendleft
# 늦게 빼고싶다면 append를 이용
# ==> 가중치 처음시작할 때는 dist[0][0] = 0 해 주는 것이 필요
dist = [[-1] * M for _ in range(N)]

# 59. 알파벳 단어사전 생성
alpha_dict = dict.fromkeys(string.ascii_uppercase, 0)

# 60. 문자열의 끝을 제거하는 방법
'''
['B', 'A', 'C']
['B', 'A']
'''
s = s[:-1]

# 61. [1192문제]
# 이전 거를 들고 가면 모든 부분을 확인할 수 있다.
dfs(idx + 1, sum - s_[idx])
dfs(idx + 1, sum)

# 62. 그래프를 한 번에 출력하는 방법
for row in board:
    print(*row)

# 63. [12886번] 튜플을 이용해서 방문 그래프 작성
    visited[tuple(stones)] = True

# 64. 삼중배열
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# 65. 이차원 배열을 담으면서 중간에 값을 추가로 담고자 할 경우 [ 경쟁적 전염 ]
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):  # 입력된 정보를 확인
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            data.append(graph[i][j], 0, i, j)  # 바이러스 종류, 시간, x, y 좌표

# 66. list의 경우 deepcopy를 해야 완전한 복사가 가능하다.
#  equal (=) 이용한 대입의 경우 포인터처럼 끌어 당긴 상태가 되어 완전한 복사가 아닌 참조가 된다.
import copy
r1 = copy.deepcopy(A)
r2 = copy.deepcopy(A)

# 67. 비트 연산

for b in range(1 << N):
    print(b)    # N이 8이라면 2^8 을 의미
                # 만약 2 << N이라면 2^8*2 의미



# 68. defaultdict 사용법
# wear_dict이라는 defaultdict 만들고 값을 추가하는 과정
for _ in range(T):
    n = int(input().rstrip())
    wear_dict = defaultdict(list)

    for i in range(n):
        name, kind = input().split()
        wear_dict[kind].append(name)

# 69. 유클리드 호제법
def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod # y는 나누어지는 수
        mod = x % y
    return y

# 70. 더 짧은 GCD 구하기
def gcd2(x, y):
    while y:
        x, y = y, x % y
    return x

# 71. 유클리드 호제법 LCM
def lcm(x, y):
    return (x * y) // gcd(x, y)

# 72. collections deque는 rotate함수가 있어서 편하게 사용할 수 있다.
l = deque([0, 1, 1, 1, 1])
l.rotate(1)

# 73. [14890] 행과 열을 각각 연산하는 방법
for i in range(N):
    cnt += check_level(graph[i])                    # 행
    cnt += check_level([row[i] for row in graph])   # 열

# 74. append와 extend의 차이점
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


# 75. graph에 여러 정보들을 저장하고 싶을 때
trees = [[deque() for _ in range(N)] for _ in range(N)]
dead_trees = [[list() for _ in range(N)] for _ in range(N)]

# 76. for문 구현에 도움되는 예제
# 3085-사탕 게임

# 77. 이차원배열 가로, 세로 사이즈
print(len(graph[1]))    # 세로
print(len(graph))   # 가로

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
from  collections import Counter

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
        d += 1
        continue
