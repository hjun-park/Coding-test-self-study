def solution(n):
    arr = [True] * (n + 1)

    for i in range(2, len(arr) // 2 + 1):
        if arr[i]:
            for j in range(i * 2, len(arr), i):  # 2*2부터 시작, 2씩 증가(배수)
                arr[j] = False

    return len([x for x in range(2, n + 1) if arr[x]])
