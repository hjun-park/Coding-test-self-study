import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0


# 선행지식
# - 원소가 N개에서 부분집합의 개수는 2^N개다.
# 즉, 문제에서 요구하는 것은 부분수열과 수열 전부이므로 공집합만 뺀 2^N-1

# 반복문 이용도 있겠지만 대표적으로 백트래킹이 이용된다.

def logic(cur, tot):  # cur는 현재 index, tot는 현재까지의 합계
    global cnt
    # base condition (마지막에 다다를 때, 더한 원소의 갯수와 N이 같은 경우)
    if cur == N:
        if tot == S:
            cnt += 1
        return

    # recursion logic (처음부터 더해서 들어가는 것이 아니라, 끝에 먼저 더하는 방식으로 접근해야 한다.)
    logic(cur + 1, tot)  # 처음에는 더하지 않고 다음 인덱스로 들어간다.
    logic(cur + 1, tot + seq[cur])  # 위의 함수가 다 끝나면 해당 함수가 실행되면서 뒤에서부터 더해진다.


logic(0, 0)
# 문제에서는 크기가 양수 부분인 부분수열만 센다고 했다.
# 그래서 합이 0인 경우를 구할 경우 공집합도 0이므로 cnt-1 해주어야 한다.
print(cnt if S != 0 else cnt - 1)
