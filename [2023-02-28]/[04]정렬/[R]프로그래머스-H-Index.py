def solution(citations):
    citations = sorted(citations)
    l = len(citations)

    for i in range(l):
        # h번 이상 인용된 논문이 h편 이상
        # citations[i]: i번 논문 인용된 횟수
        # l-i는 논문의 개수를 최댓값부터 시작
        if citations[i] >= l - i:
            return l - i

    return 0
