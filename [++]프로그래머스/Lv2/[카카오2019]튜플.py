import re


def solution(s):
    result = []
    s = s[1:-1]
    p = re.compile('(?<=\{).+?(?=\})')
    nums = sorted(re.findall(p, s), key=lambda x: len(x))

    for num in nums:
        for n in num.split(','):
            if n not in result:
                result.append(n)

    return list(map(int, result))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
