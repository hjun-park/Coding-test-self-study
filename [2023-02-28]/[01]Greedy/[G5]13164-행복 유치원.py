import sys

input = sys.stdin.readline

N, K = map(int, input().split())
h = list(map(int, input().split()))  # 키순서로 세움

'''
    핵심은 N명 학생들을 K개의 그룹으로 묶을 시, N-K개의 키 차이를 무시할 수 있다는 점
    무시한다는 의미는 학생 1명만 1개의 그룹으로 둔단 얘기다 ( 이 경우 비용이 0이니까 )
    그 이외에는 2명씩 묶는 것이 효율적이다. 그 이상은 비용이 더욱 커진다. 
    
    따라서,
     1) 차를 구해서 minus 배열을 만든 후 비용이 작은 순으로 정렬한다.
     2) 이후 N-K까지 더해준다. 그 이후의 값들은 무시된다. ( 무시된다 = 그룹당 1명으로 둔다 )
'''

# 1. 정렬된 인접한 학생들 끼리의 차를 만들어준다.
minus = []
for i in range(N - 1):
    minus.append(h[i + 1] - h[i])

# 2. 정렬
minus.sort()

print(sum(minus[:N - K]))
