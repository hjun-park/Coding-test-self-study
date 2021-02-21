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