def solution(array, commands):
    answer = []

    for l in commands:
        # l[0], l[1], l[2]
        slice_list = sorted(array[(l[0] - 1):l[1]])
        answer.append(slice_list[(l[2] - 1)])

    return answer

