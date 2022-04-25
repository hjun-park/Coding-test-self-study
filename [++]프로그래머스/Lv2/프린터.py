def solution(priorities, location):
    checked = [False] * len(priorities)
    checked[location] = True

    cnt = 1
    while priorities:
        # 우선순위가 제일 크다면 출력한다.
        if priorities[0] == max(priorities):
            # 그런데 출력하는 것이 내가 원하는 번호라면 카운트 반환
            if checked[0]:
                return cnt
            # 아니라면 pop 이후 문서만 증가
            else:
                priorities.pop(0)
                checked.pop(0)
                cnt += 1

        # 우선순위 출력 대상이 아닌 경우라면 끝에 집어넣는다.
        else:
            priorities.append(priorities.pop(0))
            checked.append(checked.pop(0))
