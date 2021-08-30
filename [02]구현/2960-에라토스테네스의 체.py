import sys

n, k = map(int, input().split())

'''
    2부터 n까지 모든 정수 적는다.
     - num_list = [ x for x in range(2, n+1) ]
    
    지우지 않은 수 중 가장 작은 수를 찾는다.
    p = min(num_list)   // 이건 소수
    
    P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
    num_list.remove(p)

    
    
'''
