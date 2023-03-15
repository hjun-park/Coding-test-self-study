import re
import sys

input = sys.stdin.readline

'''
    # 참고 URL: https://ta-ye.github.io/2021-01-30/Pro111
    1) " " 따옴표 사이의 값은 어떻게 파싱 ?  ==> 정규식 "(.*?)" 으로  파싱
    2) re.sub를 이용하면 대상 문자열을 정규표현식으로 검색한 후에 치환할 수 있다.
    3) 리스트로 index 번호를 집어넣은 것이 아닌 딕셔너리를 이용했다. ( base_score )
        
'''


def solution(word, pages):
    meta = re.compile('<meta property="og:url" content="(.*?)"/>')  # 자기 자신 페이지 이름을 정규식으로 파싱
    href = re.compile('<a href="(.*?)">')  # 해당 페이지가 가지고 있는 외부 링크들을 찾는 정규식
    base_score, links = dict(), dict()

    for page in pages:
        my_url = meta.findall(page)[0]  # 특정 페이지의 이름을 가져온다.

        # ============================
        # 기본 점수 구하기
        # ============================
        # re.sub(정규표현식, 대상 문자열, 치환 문자)
        # 1) 즉, 모든 문자열(".")에 중에서 알파벳들을 소문자로 치환 -> 반환값은 문자열
        # 2) split으로 .으로 전부 구분해 준 후에 이것들을 word 소문자로 치환한 것과 비교해서 몇 개인지 센다.
        base_score[my_url] = re.sub("[^a-z]", "", page.lower()).split('.').count(word.lower())

        # ============================
        # 링크 점수 구하기 (외부 링크 개수는 실제 매칭 점수에는 사용되지 않기 때문에 특별히 따로 계산하지 않은 것 같다.
        # ============================
        external_url = href.findall(page)  # findall을 이용하여 외부 URL 들을 리스트로 가져온다.
        for url in external_url:  # 외부 링크를 순환하고 얻은 점수들을 모두 합하면 링크 점수를 얻을 수 있다.
            # 딕셔너리를 이용해서 손쉽게 구할 수 있었다. 리스트를 이용한다면 인덱스 순서에 신경을 썼어야 했다.
            # 즉, if links[i] == links[j] then pass
            if url in links:
                links[url] += base_score[my_url] / len(external_url)
            else:
                links[url] = base_score[my_url] / len(external_url)

    # ============================
    # 매칭 점수 구하기
    # ============================
    answer = []
    for url in base_score:  # 기본 점수는 모든 url에 존재
        if url in links:    # 링크 점수는 존재하지 않을 수 있음.
            answer.append(base_score[url] + links[url]) # 기본점수, 링크점수가 있다면 모두 더함
        else:
            answer.append(base_score[url])  # 기본점수만 있다면 따로 계산

    return answer.index(max(answer))    # 가장 큰 값의 index를 빼옴, 중복된 값일 경우 가장 index가 먼저인 것이 빠져나온다.


# def get_base_score(word, pages):
#     base_score = []
#
#     for page in pages:
#         count = 0
#         for f in re.findall(r'[a-zA-Z]+', page.lower()):
#             if f == word.lower():
#                 count += 1
#         base_score.append(count)
#
#     return base_score
#
#
# def get_external_links(pages):
#     external_links = []
#     for page in pages:
#         count = len(re.findall(r'<a href=', page))
#         external_links.append(count)
#
#     return external_links
#
#
# def get_link_score(base_score, external_links, pages):
#     link_score = [0 for _ in range(len(pages))]
#
#     for i in range(len(pages)):
#         # 이름 추출
#         p = re.compile(r'<meta property="og:url" content="(\S+)"')
#         name = p.search(pages[i])
#         for j in range(len(pages)):
#             if i == j:  # 자기자신은 계산하지 않는다.
#                 continue
#             else:  # 다른 상대라면
#                 # 자기 도메인 이름 있는지 확인
#                 if re.findall(name.group(1), pages[j]): # (0)은 매치된 개수를 반환, (1)부터는 단어
#                     # 있으면 base_score[j] / external_links[j]를 link_score에 추가
#                     link_score[i] += base_score[j] / external_links[j]
#
#     return link_score
#
#
#
# def solution(word, pages):
#     _len = len(pages)
#
#     # 기본 점수
#     base_score = get_base_score(word, pages)
#
#     # 외부 링크 수
#     external_links = get_external_links(pages)
#
#     # 링크 점수
#     link_score = get_link_score(base_score, external_links, pages)
#
#     # 매칭 점수
#     match_score = [0 for _ in range(len(pages))]
#     for i in range(len(pages)):
#         match_score[i] = base_score[i] + link_score[i]
#
#     # print(f'매칭 점수 = {match_score}')
#
#     return match_score.index(max(match_score))


print(solution("blind", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))

print(solution("Muzi", [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
