import string

def solution(s, n):
    low = list(string.ascii_lowercase)
    up = list(string.ascii_uppercase)

    answer = ''

    for word in s:
        if word.isalpha() and word.isupper():
            answer += up[(up.index(word) + n) % len(up)]

        elif word.isalpha() and word.islower():
            answer += low[(low.index(word) + n) % len(low)]
        else:
            answer += ' '

    return answer


print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))
