# 이전 풀이
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if progresses[0] + (time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1

    answer.append(count)
    return answer


from math import ceil


# 내가 풀은 풀이
def solution(progresses, speeds):
    cur = ceil((100 - progresses[0]) / speeds[0])
    result = [1]

    if len(progresses) < 1:
        return result

    for p, s in zip(progresses[1:], speeds[1:]):
        next = ceil((100 - p) / s)

        if next > cur:
            result.append(1)
            cur = next
        else:
            result[-1] += 1

    return result


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
