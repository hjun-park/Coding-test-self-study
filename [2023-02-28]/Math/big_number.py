number_list = []

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first_big_number = data[n-1]
second_big_number = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_big_number
        m -= 1

    if m == 0:
        break
    result += second_big_number
    m -= 1

print(result)