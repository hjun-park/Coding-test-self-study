def mul_self(a, b, m):
    # 1) 종료부
    if b == 1:
        return a % m

    # 2) 반복부
    temp = mul_self(a, b // 2, m)
    temp = temp ** 2 % m

    # 3) b가 홀수였을 경우 2k+1니까 추가적으로 a를 더 곱해준다.
    if b % 2 == 0:
        return temp
    else:
        return temp * a % m


A, B, C = map(int, input().split())

print(mul_self(A, B, C))
