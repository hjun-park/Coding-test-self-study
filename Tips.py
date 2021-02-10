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
