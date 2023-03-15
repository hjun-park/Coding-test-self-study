import sys

input = sys.stdin.readline

'''
 https://velog.io/@sangjin98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1107%EB%B2%88-%EB%A6%AC%EB%AA%A8%EC%BD%98
 1) 입력
 2) 리모컨 버튼의 경우 set 형태로 누를 수 있는 버튼리스트 생성
 3) M이 0이 아니라면 차집합을 이용
 4) start = 100, count 값은 최댓값으로 설정 ( start - N )
 5) 전체 순회 (100만까지) -> 각 자리수 순회 
   -> 각 자리가 입력 불가능하면 다시 순회
   -> 각 자리 수 입력 가능하면 count 값 설정 ( 자리수 + 해당 값 까지 거리 )
      
'''

# 1)
N = int(input())
M = int(input())

# 2)
buttons = set(map(str, input().split()))
button_list = {str(i) for i in range(10)}

# 3)
if M != 0:
    button_list -= buttons

# 4)
start = 100
count = abs(start - N)

# 5)
for i in range(1000001):
    for j in range(len(str(i))):
        # print(f'str(i)[j]: {str(i)[j]}')    # 120 ~ 123 이라면 1,2,0,1,2,1,1,2,2 순 출력
        if str(i)[j] not in button_list:
            break
        elif j == len(str(i)) - 1:  # 모든 자리가 입력 가능한 상태라면 ( j는 0부터 시작하니까 i를 1빼줌 )
            count = min(count, len(str(i)) + abs(i - N))

print(count)
