import sys

input = sys.stdin.readline

'''
    참고: 서로소 성질을 이용함
    https://dirmathfl.tistory.com/255
'''

N = int(input())
B = list(map(int, input().split()))
B_num = {num: 0 for num in B}

for num in B_num.keys():
    cur_num = num

    while True:
        if num % 3 == 0:
            B_num[cur_num] += 1
            num //= 3
        else:
            break

# 횟수가 가장 많은 것부터 정렬, 그 다음으로 크기가 더 큰 것부터 정렬
sort_num = sorted(B_num.items(), key=lambda x: (-x[1], x[0]))
print(*[key for key, _ in sort_num])    # key만 여러개 출력

