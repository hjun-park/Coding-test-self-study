import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    s = [0 for _ in range(N)]   # 인원 수만큼 초기화

    # count 초기화
    count = 1   # 어차피 서류 1등은 무조건 뽑으므로

    # 서류와 면접순위를 입력받는다.
    for _ in range(N):
        resume, interview = map(int, sys.stdin.readline().split())
        s[resume-1] = interview # 오름차순으로 면접등수를 입력받음
    min_value = s[0]

    for i in range(1, N):
        if s[i] < min_value:
            count += 1
            min_value = s[i]

    print(count)




