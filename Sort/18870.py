import sys

'''
    틀린문제 : 참고 코드 : https://neomindstd.github.io/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/boj18870/
    문제에서는 좌표값에 따른 출력 순서 결정 ( 가장 작은게 먼저 출력되어야함 , 정렬 순위가 높음 )
'''
N = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))
xt = list(sorted(set(x)))
xt = {xt[i]:i for i in range(len(xt))}

print(*[xt[i] for i in x])