'''
[문제이해/제약조건]
 - 라디오방송 한 음악 반복 재생 가능 (끝부분-처음부분 이어져 재생된 멜로디일 수도 있다)
 - 한 음악을 중간에 끊으면 원본 음악에는 기억한 멜로디가 있어도 그 곡은 네오가 들은 곡이 아닐 수도 있다 (?)
 - 기억한멜로디 <-> 재생시간/제공된악보 비교

 - 음악길이보다 재생시간이 긴 경우라면 끝나고도 다시 재실행된 경우
 - 등등 여러 제약조건

[전체프로세스]
0. musicinfos 순회
1. 재생시간,악보정보를 참고하여 재생된 곡 문자열을 만든다.
2. 재생된 곡 문자열에서 m이 들어있는지 확인한다. 들어있다면 result에 제목을 집어넣는다.

[프로세스별 수도코드]
0.  # 제거
 <재생된 곡 문자열 만들기>
 1. running_time = datetime 이용하여 계산
 2. len(악보정보) 계산 (계산 시 #의 길이는 제외하고 계산)
 3. (divmod(1, 2))하여 계산 후 곡 문자열을 만든다.

 <m이 들어있는지 확인>
 1. if m이 곡문자열 있는지 확인 then append to result (재생시간, 제목)
 2. result가 없으면 (None) 반환


[주석옮기기/전역코드먼저]



'''

# [1] <#>을 제거하는 방식
# # 내 방법은 erase_sharp()에서 앞에 소문자 변경 후 그 앞은 c로 바꾸었다.
# # 다른 사람은 str.replace()를 이용하여 C# -> c로 교체하였다.  [더 효율적]

# [2] 시간 차이를 구하는 방식
# # 내 방법은 datetime을 이용하여 연산
# # 다른 사람은 시간을 문자열로 파싱해서 시간 계산함
# # time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])

# [3] 가장 시간이 길며 곡 문자열이 있는 result를 구하는 방식
# # 내 방법은 매번 max를 갱신하면서 그대로 result에 담았고 최종적으로 순회하면서 가장 먼저 max_time이 나오는 것을 출력했다.
# # 다른 사람은 내 방식과 의도는 같지만 코드를 더 짧게 구현했다. result에 여러 개 담는게 아닌 가장 긴 시간 가지는 곡만 1개만 담았다.
'''
answer=[0,'(None)']
if m in full_notes and time_length > answer[0]:
    answer = [time_length, title]
return answer
'''


from datetime import datetime


def erase_sharp(_s):
    _s = list(_s)
    for i in range(1, len(_s)):
        if _s[i] == '#':
            _s[i - 1] = _s[i - 1].lower()

    # list comprehension 이용하여 #만 제거
    _s = [x for x in _s if x != '#']

    return ''.join(_s)


def solution(m, musicinfos):  # [시작시간, 끝난시간, 제목, 악보정보(길이는 한곡당 필요한 재생시간)]

    result = []
    max_time = -1

    # '#'을 지우고 그 앞 문자는 소문자로 변경
    m = erase_sharp(m)
    print(f'm = {m}')

    while musicinfos:
        st, en, title, info = musicinfos.pop(0).split(',')

        info = erase_sharp(info)

        # 재생시간, 악보정보를 참고하여 곡 문자열을 만든다.
        start = datetime.strptime(st, "%H:%M")
        end = datetime.strptime(en, "%H:%M")

        diff = end - start
        run_time = diff.seconds // 60
        info_len = len(info)  # - info.count('#')

        q, r = divmod(run_time, info_len)
        total_info = info * q + info[:r + 1]

        # print()
        # print(f'비교 대상 = {m}')
        # print(f'곡 시간 = {run_time}')
        # print(f'악보 길이 = {info_len}')
        # print(f'생성된 곡 : {total_info}')
        # print(f'생성된 곡의 길이 : {len(total_info)}')

        # m이 들어있는지 확인하고 result에 집어넣는다.
        if m in total_info:
            result.append((run_time, title))
            max_time = max(max_time, run_time)

    # result 출력
    for time, name in result:
        if time == max_time:
            return name

    return '(None)'


print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
