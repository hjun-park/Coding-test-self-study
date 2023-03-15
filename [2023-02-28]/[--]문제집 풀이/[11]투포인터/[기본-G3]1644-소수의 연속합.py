import sys

input = sys.stdin.readline

N = int(input().rstrip())

'''
    [요약]
    1. 자연수 N을 소수의 연속합으로 나타낼 수 있는 경우의 수를 구하기
    2. 연속된 수여야 하며, 한 번씩만 쓰일 수 있다. (투포인터 증거)
    
    [풀이]
    1. 입력받은 N에 대한 소수 리스트 생성
    2. st와 en 0, 1로 초기화 및 cnt 초기화
    3. _sum은 첫 번째 인자로 초기화
    4. 루프를 돈다.
    4-1. N과 같으면 cnt 증가
    4-2. N과 같거나 작으면 꼬리 누적합 반영 후 en증가  
    4-3. N보다 작으면 크다면 머리 누적에서 차감 후 st증가
    4-4. 소수 리스트의 길이와 en이 같다면 루프를 빠져나감 (en이 끝까지 갔단 얘기는 더 이상 만족하는 수가 앞으로 없음) 

'''


def find_prime_number(M, N):
    # 1) arr 생성
    arr = [True] * (N + 1)

    # 2) 2부터 절반까지 순회
    for i in range(2, len(arr) // 2 + 1):
        # 3) arr[i]가 참이라면 그 다음 수부터 배수들은 False처리
        if arr[i]:
            for j in range(i * 2, len(arr), i):
                arr[j] = False

    return [x for x in range(2, N + 1) if arr[x]]


if N == 1:
    print(0)
    sys.exit(0)

A = find_prime_number(2, N)
st, en = 0, 1
cnt = 0
_sum = A[0]

while len(A) >= 2:
    if _sum == N:  # 4-1)
        cnt += 1

    if _sum <= N:  # 4-2)
        _sum += A[en]
        en += 1

    if _sum > N:  # 4-3)
        _sum -= A[st]
        st += 1

    if en == len(A):  # 4-4)
        break

if A[-1] == N:
    cnt += 1

print(cnt)
