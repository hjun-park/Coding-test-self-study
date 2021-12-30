# def solution(s):
#     return string.capwords(s)

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])


print(solution('3people unFollowed me'))
print(solution('for the last week'))
print(solution('  fFr   the last week'))
print(solution('t'))
print(solution('T'))
print(solution('*T'))
