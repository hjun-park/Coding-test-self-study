def solution(word):
    n = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}

    # 사이간격 (자릿수가 바뀌는 규칙은 x5 + 1), 자릿수가 커질수록 x5는 제곱됨
    # A <-> E: 6개
    # A <-> I: 31개
    # A <-> O : 156개
    # A <-> U : 781개

    answer = len(word)  # 기본적으로 A는 세고 들어감
    for i in range(len(word)):
        for j in range(4, i, -1):  # 5-자릿수만큼 더해나감
            print(i, j)
            answer += 5 ** (j-i) * n[word[i]]
        answer += n[word[i]]

    return answer

# print(solution("AAAAE"))
print(solution("A"))
# print(solution("AAAE"))
