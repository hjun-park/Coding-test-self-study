import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    checked = [False] * N
    checked[M] = True

    count = 0  # 문서 번호 세기
    while True:
        if docs[0] == max(docs):  # 중요도가 제일 크다면
            count += 1  # 문서 번호 증가

            if checked[0]:  # 알고 싶은 대상이라면
                print(count)
                break

            else:  # 아니라면 그냥 출력하기
                docs.pop(0)
                checked.pop(0)

        else:  # 출력 대상이 아닌 경우
            docs.append(docs.pop(0))
            checked.append(checked.pop(0))
