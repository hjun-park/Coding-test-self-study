def solution(N, stages):
    answer = {}  # 딕셔너리 // 중복값은 하나로
    player = len(stages)  # 스테이지에 도달한 플레이어의 수

    for stage in range(1, N + 1):  # 1부터 N까지 (다 깬 사람, N+1은 제외)
        if player != 0:
            cnt = stages.count(stage)
            answer[stage] = cnt / player  # 각 스테이지당 실패율을 저장
            player -= cnt  # 스테이지가 올라갈 수록 남아있는 사람의 수는 줄어듦
        else:  # 1부터 5까지 중, 스테이지는 있지만 깬 사람이 없는 경우
            answer[stage] = 0

    # 딕셔너리로 넣고 정렬하면 이미 1, 2, 3, 4, 5 인덱스 순으로 값을 집어넣었기 때문에
    # 실패율로 역순 정렬만 해 주면 된다.
    return sorted(answer, key=lambda x: answer[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
