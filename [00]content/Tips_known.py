import copy
import sys

# 1. 입력값을 여러 개 받고싶을 때
n, m, k = map(int, input().split())  # 일반
data = list(map(int, input().split()))  # 리스트로 저장
data2 = list(int(input()) for _ in range(N))  # 여러 개 문장

# 2. 개수만큼 입력을 받아 순서 쌍으로 저장
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

# 8. 이차원 정사각 행렬 입력받기
n = int(sys.stdin.readline())
a = [list(sys.stdin.readline()) for _ in range(n)]

# 9. 2차원 행렬, 좌표문제 풀 때는 dx, dy 리스트를 선언해주어서 접근해보기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 10. 재귀 한도 해제
sys.setrecursionlimit(10000)  # 재귀 한도를 풀어줌

# 11. 파이썬 기본 라이브러리 이용하여 역순 정렬
array = sorted(array, reverse=True)

# 13. 많은 값들을 입력 받을 때 빠르게 입력받으려면 sys 라이브러리 사용
input_data = sys.stdin.readline().rstrip()
print(input_data)

# 18. 리스트 거꾸로 출력
num[::-1] = num  # (num은 그냥 숫자)

# 23. ascii 문자를 정수로 변환
int(ord('a'))

# 24. list comprehension 을 이용하여 2차원 행렬의 초기화 ( n x m )
d = [[0] * m for _ in range(n)]
graph = [[] for _ in range(n + 1)]  # 2차원 배열 ( N x N )

# 26. 한 번에 입력받을 때 split을 이용하여 하나의 변수에 모두 담을 수 있음
input_data = sys.stdin.readline().rstrip().split()

# 28. 2차원 리스트(그래프 표현) 만든 후 모든 값 무한으로 초기화
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 31. 좌표 입력받는 방법
for _ in range(L):
    x, c = map(int, input().split())
    info.append((int(x), c))

# 32. 좌표 입력받는 방법 2
for i in range(k):
    a, b = map(int, input().split())
    apple[a][b] = 1

# 36. 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 39. 리스트에 해당 수가 들어간 개수가 몇 개인지 number[i]에 집어넣음
number[i] = n.count(str(i))

# 41. 리스트 컴프리헨션
# 0부터 19까지 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
# 1부터 9까지의 수 중 제곱 값만을 포함하는 리스트
array = [i * i for i in range(1, 10)]

# 43. 딕셔너리 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

if '사과' in data:
    print("사과를 키로 가지는 데이터가 존재합니다")

key_list = data.keys()  # 키 데이터만 담긴 리스트
value_list = data.values()  # 값 데이터만 남긴 리스트

# 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

# 54. DFS 방문 기록 관련 히스토리 리스트 선언
history = [[False] * m for _ in range(n)]

# 58. BFS 에서 가중치를 이용할 수 있는데, 비교 후 큐에 집어넣을 때
# 가장 먼저 빨리 빼고 싶다면 appendleft
# 늦게 빼고싶다면 append를 이용
# ==> 가중치 처음시작할 때는 dist[0][0] = 0 해 주는 것이 필요
dist = [[-1] * M for _ in range(N)]

# 62. 그래프를 한 번에 출력하는 방법
for row in board:
    print(*row)

# 64. 삼중배열
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

# 66. list의 경우 deepcopy를 해야 완전한 복사가 가능하다.
#  equal (=) 이용한 대입의 경우 포인터처럼 끌어 당긴 상태가 되어 완전한 복사가 아닌 참조가 된다.
r1 = copy.deepcopy(A)
r2 = copy.deepcopy(A)

# 68. defaultdict 사용법
# wear_dict이라는 defaultdict 만들고 값을 추가하는 과정
for _ in range(T):
    n = int(input().rstrip())
    wear_dict = defaultdict(list)

    for i in range(n):
        name, kind = input().split()
        wear_dict[kind].append(name)


# 75. graph에 여러 정보들을 저장하고 싶을 때
trees = [[deque() for _ in range(N)] for _ in range(N)]
dead_trees = [[list() for _ in range(N)] for _ in range(N)]

# 76. for문 구현에 도움되는 예제
# 3085-사탕 게임

