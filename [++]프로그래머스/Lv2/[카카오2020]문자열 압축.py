# [참고] https://whwl.tistory.com/68#recentEntries

def solution(s):
    answer = int(1e9)

    # 01. 압축단위를 1부터 해서 늘려감 ( 최대는 len(s)개 )
    for slicing in range(1, len(s) // 2 + 2):  # +2 한 이유는 문자열이 1개일 경우 슬라이싱 처리하기 위함
        res = ''
        tmp = s[:slicing]
        cnt = 1

        # 02. 압축단위 개수만큼 문자를 잘라내어 비교
        for i in range(slicing, len(s) + slicing, slicing):
            if tmp == s[i:i + slicing]:  # 일치 한다면
                cnt += 1
            else:  # 일치 X
                if cnt == 1:  # 압축할 만한 문자열 없음
                    res += tmp
                else:  # 압축할 만한 문자열이 최소 1개 존재
                    res = res + str(cnt) + tmp

                # 일치 X였으므로 다음 문자열 slicing 개수만큼 압축 지정
                tmp = s[i:i + slicing]
                cnt = 1

        # 03. 압축단위 별로 문자열 루프 순회 완료 시 min값 갱신
        answer = min(answer, len(res))

    return answer


print(solution("aabbaccc"))
