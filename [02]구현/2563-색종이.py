import sys

input = sys.stdin.readline


'''
    참고: https://ywtechit.tistory.com/182
    
    핵심: 전체넓이 - 겹친부분으로 구하는 것이 아니다.
    100x100 이차원 배열 생성 후 색종이가 위치한 부분을 1로 셋팅하면 된다.
    그럼 중복될 지라도 1은 1인 것이고 1만 센다면,
    최종적으로 겹친부분을 제외한 넓이가 잘 출력이 된다. 

'''

N = int(input().rstrip())
papers = [[0] * 100 for _ in range(100)]

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(b, b+10):
        for j in range(a, a+10):
            papers[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if papers[i][j]:
            cnt += 1


print(cnt)


