import sys

input = sys.stdin.readline

A, P = map(int, input().split())

'''
    팁1 : 숫자의 자릿수가 다른 경우는 뒤에서부터 확인한다.
        for s in str(nums[-1]):
    
    배운점: 반복수열을 체크하는 방법
      1) 하나씩 수열을 증가시켜가며 중복된 값이 시작할 때까지 루프를 돈다. ( if문 )
      2) 중복된 값이 없다면 수열을 증가, 있다면 루프를 빠져나간다.
      3) 루프를 빠져나가고 마지막 중복이 시작된 값의 index를 뽑으면 구간의 개수이다. 
'''

result_list = [A]

# 1) 하나씩 수열을 증가시켜가며 중복된 값이 시작할 때까지 루프를 돈다. ( if문 )
while True:
    result = 0

    for n in str(result_list[-1]):  # 마지막부터 확인하여 연산
        result += (int(n) ** P)

    # 2) 중복된 값이 없다면 수열을 증가, 있다면 루프를 빠져나간다.
    if result in result_list:
        break

    # 아니라면 값 추가
    result_list.append(result)

# 3) 중복되는 값의 index를 반환하면 그 전까지는 중복이 발생하지 않는 구간의 개수
print(result_list.index(result))
