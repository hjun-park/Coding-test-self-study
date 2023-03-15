# 1) (n + 1) % 5
# 2) 2,1,   2,3,   2,4,   2,5 .... ()
# 3) 3*2  1 , 2, 4, 5

def solution(answers):
    answer = []
    peoples = [0, 0, 0]
    a_arr = [1, 2, 3, 4, 5]
    b_arr = [2, 1, 2, 3, 2, 4, 2, 5]
    c_arr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # a먼저 판정
    for i, ans in enumerate(answers):
        print(i, i % len(c_arr))
        if answers[i] == a_arr[i % len(a_arr)]:
            peoples[0] += 1

        if answers[i] == b_arr[i % len(b_arr)]:
            peoples[1] += 1

        if answers[i] == c_arr[i % len(c_arr)]:
            peoples[2] += 1

    print(peoples)
    for i, ans in enumerate(peoples):
        if ans == max(peoples):
            answer.append(i + 1)

    return answer


print(solution(answers=[1, 2, 3, 4, 5]))
