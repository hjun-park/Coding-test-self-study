import sys

input = sys.stdin.readline

S = list(map(int, input().rstrip()))

'''
    [요약]
    1) 연속된 세 숫자
    
    [풀이]
    1) 1부터 세기 시작한다.
    2) 이전 숫자가 현재 숫자보다 1보다 작으면 result에 더해주기
    3) 숫자가 1씩 증가하는게 맞으면 result에 들어갈 것이다.
    4) 만약 1씩 증가하는 수가 아닌 것을 만나면 길이가 3인지 체크한다.
    2-1) 1씩 증가하면 cnt 증가
    2-2) cnt == 3 이면 result += 1 
'''

result = str(S[0])
cnt = 0
for i in range(1, len(S) + 1):
    if i == len(S):
        if len(result) == 3:
            print(cnt + 1)
            sys.exit(0)
        print(cnt)
        sys.exit(0)

    if S[i - 1] == S[i] - 1:
        result += str(S[i])

    else:
        if len(result) == 3:
            cnt += 1
        result = ''
        result += str(S[i])

print(cnt)
