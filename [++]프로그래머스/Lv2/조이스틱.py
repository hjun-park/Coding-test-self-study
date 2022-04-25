def solution(name):
    cnt = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    # 끝이 A라면 그 갯수만큼 이동할 필요가 없다.
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1

    if min_move < 0:
        return cnt

    # name의 각 자리에서 출발해서 단어 만들기 시도한다. (브루트 포스)
    for i, _str in enumerate(name):
        # 해당 자리의 알파벳을 변경하기 위한 최솟값을 추가한다.
        cnt += min(ord(_str) - ord('A'), ord('Z') - ord(_str) + 1)

        # 해당 알파벳 다음부터 끝까지 연속된 A의 개수를 nxt에 저장한다.
        # nxt에는 현재 자신의 인덱스 + 이후 A의 개수가 들어간다.
        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1

        # for문을 반복하면서 어느 자리에서 변경해야 더 효율적인지 min_move를 변경시키며 찾아나간다.
        # [1] 왼쪽에서 오른쪽으로만 이동하는 일반적인 방식
        # [2] A 시작 바로 직전에서 역순으로 시작해 A의 끝까지 역순으로 가는 방식
        # --> 자신의 인덱스 왔다갔다 + (전체 - A까지 밟은데까지)
        print(i, len(name), nxt)
        min_move = min([min_move, i + i + len(name) - nxt])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    cnt += min_move
    return cnt


print(solution("AAAABABAAAA"))
