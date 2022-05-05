nums = [3, 4, 1, 2, 5, 7]
n = len(nums)

while True:
    _max = -1
    k = int(input())

    if n < k or k < 2:
        print('INVALID INPUT')
        break

    for i in range(k - 1, n + 1):
        _max = max(_max, sum(nums[i - k:i]))

    print(_max)
