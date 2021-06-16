import sys

# 방 번호 n 입력
n = input()

# 숫자 리스트 초기화
number = [0] * 10

# 6과 9의 개수를 담을 변수
six_nine = 0

# 각 수 개수 구하기
for i in range(10):
    number[i] = n.count(str(i))
    if i == 6 or i == 9:    # 6이나 9인 경우
        number[i] = 0       # 개수를 세고 집어넣는 것이 아니라
        six_nine += n.count(str(i)) # six_nine 수를 증가시켜줌


# 6과 9를 제외한 수 중 가장 많은 수 구하기 ( 그만큼 세트가 필요할 것이므로 )
big = max(number)


# 6과 9를 하나로 생각해서 나눈 몫 + 1 개로 인식
if six_nine % 2 == 0:
    six_nine //= 2
else:
    six_nine = six_nine // 2 + 1

answer = max(six_nine, big)  # 이전에 구한 세트 수와 six_nine값을 비교
print(answer)
