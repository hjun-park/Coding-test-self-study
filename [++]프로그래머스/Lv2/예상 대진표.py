def solution(n, a, b):
    cnt = 0

    # a와 b가 같을 때까지 게임을 진행 (같으면 a와 b가 경쟁 한다는 얘기)
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        cnt += 1
    return cnt


print(solution(8, 4, 7))
print(solution(4, 1, 3))
print(solution(4, 1, 2))
