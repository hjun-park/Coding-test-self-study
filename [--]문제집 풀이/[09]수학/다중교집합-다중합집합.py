a = [1, 2, 2, 3, 4, 5]
b = [1, 1, 2, 3, 4, 6]

# A + B - A교B = 합집합
a_temp = a.copy()  # B - A
a_result = a.copy()

for i in b:
    if i not in a_temp:
        a_result.append(i)  # A에 없는 요소만 추가해줌
    else:
        a_temp.remove(i)  #

# 결과
print(sorted(a_result))
print(a_temp)
print(sorted(a_result + a_temp))
