arr = [1, 8, 7, 4, 3, 5, 6]
n = len(arr)

psum = [0] * n
start, end = 1, 5

psum[0] = arr[0]
for i in range(1, n):
    psum[i] = psum[i - 1] + arr[i]

_sum = psum[end] - psum[start - 1]
print(_sum)
