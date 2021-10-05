import sys
from collections import defaultdict

input = sys.stdin.readline

# 아이스크림 개수, 먹으면 안 되는 조합의 수
N, M = map(int, input().split())

'''
    출처: https://ihatecucumber.tistory.com/30
    핵심: set을 만들어 가장 먼저 i, j확인 후 다음으로 k-(i,j) 확인하는 방식
    0. 아이스크림 개수가 3개 이하라면 조합을 생성 하기도 전이니, 0을 반환
    1. no_mix 이름의 set 생성 ( 1부터 N )
    2. 인접행렬 생성하듯이 두 값을 입력받아 no_mix에 추가
    3. loop 두 번 순회하면서 j가 no_mix[i]에 속하는지 확인
    4. 만약 속하지 않으면 그 다음 j+1부터 해서 k 순회하고
       k가 no_mix[i]와 no_mix[j]에 속하지 않는지 확인
    5. 다 속하지 않았다면 count += 1  
'''

count = 0

if N < 3:
    print(0)
else:
    no_mix = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        no_mix[a].append(b)
        no_mix[b].append(a)

    # 아이스크림 개수만큼 순회
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in no_mix[i]:
                continue
            for k in range(j+1, N+1):
                if k in no_mix[i] or k in no_mix[j]:
                    continue
                count += 1

print(count)




