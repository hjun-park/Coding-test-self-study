import sys

input = sys.stdin.readline

'''
    -> 대표적 투포인터 문제
    https://baby-ohgu.tistory.com/12
    > 1. 정렬 
    > 2. left ,right를 이용하여 arr[left], arr[right]를 더해준다. 이 값은 tmp 변수 저장
    >  =>  X일 경우 count += 1, tmp > X 일 경우 right감소, tmp < X 일 경우 left증가
    > 기본적으로 right는 감소하게 짜고, temp < X 일 경우만 left 증가하게 짜면됨
'''

N = int(input().rstrip())
numbers = list(map(int, input().split()))
X = int(input().rstrip())

numbers.sort()

left = 0
right = N - 1

count = 0
while left < right:
    tmp = numbers[left] + numbers[right]

    if tmp == X:
        count += 1
        left += 1
    elif tmp < X:
        left += 1
    else:
        right -= 1

print(count)
