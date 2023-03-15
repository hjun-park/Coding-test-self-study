import sys

input = sys.stdin.readline

''' 
    핵심: 에라토스테네스의 체 + 투포인터 알고리즘
    
    투포인터 알고리즘
     :  start, end 두 개의 포인터 이용해서 원하는 값보다 작은 경우 end += 1
     :  원하는 값보다 큰 경우 start += 1 적용해서 end가 N될 때까지 수행
'''

N = int(input())


def find_prime_number():
    array = [True for _ in range(N + 1)]

    for i in range(2, N + 1):
        if array[i] is True:
            j = 2
            while i * j <= N:
                array[i * j] = False
                j += 1

    return [x for x in range(2, N + 1) if array[x]]


prime = find_prime_number()

# 투 포인터,  0부터 시작
start = 0
end = 0
count = 0

while end <= len(prime):
    temp_sum = sum(prime[start:end])

    if temp_sum == N:  # 문제에서 요구하는 것과 같으면 end값이 0부터 시작하므로 end + 1
        count += 1
        end += 1
    elif temp_sum < N:  # 원하는 값보다 작을 경우 end += 1 ( 범위 늘려주기 )
        end += 1
    else:  # 원하는 값보다 클 경우 start += 1
        start += 1

print(count)
