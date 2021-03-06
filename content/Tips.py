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







