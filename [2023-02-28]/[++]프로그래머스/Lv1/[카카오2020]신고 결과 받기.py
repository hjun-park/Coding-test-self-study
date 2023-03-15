from collections import defaultdict

'''
    1. 신고횟수 제한 X, 한 유저를 여러번 신고할 경우 1회처리
    2. K번 이상 신고된 유저는 게시판 이용 정지, 해당 유저 신고한 모든 유저에게 정지 사실 발송
    3. 신고내용 취합 -> K번 이상 유저 전부 이용 정지 -> 신고한 유저에게 메일 발송
'''

# --- 모범 답안 ---
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports = {x : 0 for x in id_list}
#
#     for r in set(report):
#         reports[r.split()[1]] += 1
#
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1
#
#     return answer


def solution(id_list, report, k):
    report_dict = defaultdict(list)
    mail = defaultdict(int)

    for name in id_list:
        mail[name] = 0

    for users in report:
        a, b = users.split()
        report_dict[b].append(a)
        report_dict[b] = list(set(report_dict[b]))  # 중복 제거

    for name in id_list:
        if len(report_dict[name]) >= k:
            for n in report_dict[name]:
                mail[n] += 1

    return list(mail.values())


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
