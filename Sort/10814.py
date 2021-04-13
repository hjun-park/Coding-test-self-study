import sys

N = int(sys.stdin.readline().rstrip())
m_list = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().strip().split())
    age = int(age)
    m_list.append((age, name))

# 나이 숫자 정렬 => 가입순 정렬  ( 가입순 정렬은 입력한 순서니까 굳이 정렬 안해도 된다.
m_list.sort(key=lambda m: (m[0]))

# 가입 순 정렬
for m in m_list:
    print(m[0], m[1])
