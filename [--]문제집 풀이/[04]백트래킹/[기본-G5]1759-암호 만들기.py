import sys

input = sys.stdin.readline

L, C = map(int, input().split())  # 암호의 길이 = L
alphas = sorted(list(input().split()))
temp = []
visited = [False] * C

'''
    [요약]
    1) 암호는 L개
    2) 최소 1개 모음, 두 개의 자음 ==> 즉, 모음이 하나씩 무조건 있으면 됨
    3) 정렬된 문자열 

'''


def check_aeiou(letters):
    cnt = 0

    for l in letters:
        if l in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1

    return cnt


def logic(start):
    if len(temp) == L:
        if check_aeiou(temp) >= 1 and len(temp) - check_aeiou(temp) >= 2:
            print(''.join(temp))
            return

        return

    for i in range(start, C):
        if visited[i]:
            continue

        temp.append(alphas[i])
        visited[i] = True

        logic(i + 1)

        visited[i] = False
        temp.pop()


logic(0)
