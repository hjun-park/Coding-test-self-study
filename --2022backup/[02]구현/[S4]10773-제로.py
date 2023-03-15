n = int(input())
data = []
for _ in range(n):
    num = int(input())
    if num == 0:
        data.pop()
    else:
        data.append(num)

print(sum(data))
