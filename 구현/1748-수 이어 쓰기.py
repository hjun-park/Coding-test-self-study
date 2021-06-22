import sys

'''
    1-9 : 9개
    10-99 : 90개 * 2
    100-999 : 900개 
    
    ** 1, 2, 3은 길이
    n이 120일 때 1 * (10 - 1) + 2*(100 - 10) + 3 * (120-100+1)
    n이 15일 때 1 * (10 - 1) + 3 * ( 15 - 10 + 1 )   
'''

n = int(input())
length = len(str(n))

ans = 0

# 123 이라면 아래 루프를 2번만 돌게 될 것임
# 길이 수가 1개 일 때, 길이 수가 2개 일 때 ,  ( 1, 2 숫자 ) 대해서 루프
for i in range(1, length):
    ans += i * ((10 ** i) - (10 ** (i-1)))

# 길이 수가 3개 일 때 ( 1, 2 , 0 ) 에 대해서 최종 연산
ans += length * (n - (10 ** (length - 1)) + 1)
print(ans)
