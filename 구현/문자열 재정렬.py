import sys

data = list(map(str, sys.stdin.readline().rstrip()))
result = []
value = 0

for x in data:
    # 알파벳인 경우
    if x.isalpha():
        result.append(x)
    # 숫자는 더하기
    else:
        value += int(x)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))



