# 최소값을 만드는 방법
# 여러 케이스들을 만들면서 공식이나 규칙성을 찾는다.
# 최소값을 만들기 위해서는 (-) 뒤에 괄호를 쳐주면 된다.
# # 55 - 50 + 40 => 55 - (50 + 40) = -35
# # 1 - 2 + 3 - 4 => 1 - (2 + 3) - (4) = -8

# (-)를 기준으로 만들 것이기 때문에 split을 - 기준으로 리스트를 만든다.
user_input = list(map(str, input().split('-')))
temp_array = []


# +를 먼저 분리해서 모두 더한다.
for num in user_input:
    s2 = num.split('+')
    temp = 0
    for num2 in s2:
        temp += int(num2)

    temp_array.append(temp)

# 처음 수만 더하고 나머지는 모두 빼준다.
result = temp_array[0]

for num in temp_array[1:]:
    result -= num

print(result)