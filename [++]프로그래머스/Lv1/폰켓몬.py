def solution(nums):

    select = int(len(nums)//2)
    tp = list(set(nums))

    if len(tp) < select:
        return len(tp)
    else:
        return select


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
