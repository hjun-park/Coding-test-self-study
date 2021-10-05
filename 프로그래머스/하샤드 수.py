def solution(x):
    sx = list(str(x))
    digit_sum = 0

    for num in sx:
        digit_sum += int(num)

    return True if x % digit_sum == 0 else False
