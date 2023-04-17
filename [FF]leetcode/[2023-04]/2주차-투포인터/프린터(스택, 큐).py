from collections import deque


def solution(priorities, location):
    cnt = 0
    checked = deque()
    checked.extend([False] * len(priorities))
    checked[location] = True

    while priorities:
        p = priorities.pop(0)

        for e in priorities:
            if e > p:
                checked.rotate(-1)
                priorities.append(p)
                break
        else:
            cnt += 1
            c = checked.popleft()
            if c is True:
                return cnt


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5

# 느낀점 :
# 1)처음 펜으로 설계 (손코딩) 시 순서를 잘 정하고 이 순서가 정말 맞나 검증 후 코드로 옮기자

# 이전코드
# def solution(priorities, location):
#     checked = [False] * len(priorities)
#     checked[location] = True
#
#     cnt = 1
#     while priorities:
#         # 우선순위가 제일 크다면 출력한다.
#         if priorities[0] == max(priorities):
#             # 그런데 출력하는 것이 내가 원하는 번호라면 카운트 반환
#             if checked[0]:
#                 return cnt
#             # 아니라면 pop 이후 문서만 증가
#             else:
#                 priorities.pop(0)
#                 checked.pop(0)
#                 cnt += 1
#
#         # 우선순위 출력 대상이 아닌 경우라면 끝에 집어넣는다.
#         else:
#             priorities.append(priorities.pop(0))
#             checked.append(checked.pop(0))
