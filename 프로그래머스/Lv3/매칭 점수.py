import re
import sys

input = sys.stdin.readline


def get_base_score(word, pages):
    base_score = []

    for page in pages:
        count = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                count += 1
        base_score.append(count)

    return base_score


def get_external_links(pages):
    external_links = []
    for page in pages:
        count = len(re.findall(r'<a href=', page))
        external_links.append(count)

    return external_links


def get_link_score(base_score, external_links, pages):
    link_score = [0 for _ in range(len(pages))]

    for i in range(len(pages)):
        # 이름 추출
        p = re.compile(r'<meta property="og:url" content="(\S+)"')
        name = p.search(pages[i])
        for j in range(len(pages)):
            if i == j:  # 자기자신은 계산하지 않는다.
                continue
            else:  # 다른 상대라면
                # 자기 도메인 이름 있는지 확인
                if re.findall(name.group(1), pages[j]): # (0)은 매치된 개수를 반환, (1)부터는 단어
                    # 있으면 base_score[j] / external_links[j]를 link_score에 추가
                    link_score[i] += base_score[j] / external_links[j]

    return link_score



def solution(word, pages):
    _len = len(pages)

    # 기본 점수
    base_score = get_base_score(word, pages)

    # 외부 링크 수
    external_links = get_external_links(pages)

    # 링크 점수
    link_score = get_link_score(base_score, external_links, pages)

    # 매칭 점수
    match_score = [0 for _ in range(len(pages))]
    for i in range(len(pages)):
        match_score[i] = base_score[i] + link_score[i]

    # print(f'매칭 점수 = {match_score}')

    return match_score.index(max(match_score))


print(solution("blind", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))

print(solution("Muzi", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
