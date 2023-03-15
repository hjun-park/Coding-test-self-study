import sys

input = sys.stdin.readline

N, K = map(int, input().split())

'''
    [에라토스테네스의 체 알고리즘] 
    2부터 n까지 모든 정수 적는다.
     - num_list = [ x for x in range(2, n+1) ]

    지우지 않은 수 중 가장 작은 수를 찾는다.
    p = min(num_list)   // 이건 소수

    P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
    num_list.remove(p)
'''


def find_delete_prime_number(M):
    array = [True for _ in range(M + 1)]

    cnt = 0
    for i in range(2, len(array) + 1):
        for j in range(i, M + 1, i):
            if array[j]:
                array[j] = False
                cnt += 1
                if cnt == K:
                    return j


print(find_delete_prime_number(N))
