N = int(input())
offset = 1
result = 1

for i in range(N):
    result += offset
    if i % 2 == 0:
        offset += 1

print(result)


