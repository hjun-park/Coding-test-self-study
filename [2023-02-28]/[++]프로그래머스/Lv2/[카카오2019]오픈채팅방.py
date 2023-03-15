'''
[문제이해]
1. 닉네임 변경 방법
 a) 채팅방 나가고 새로운 닉네임으로
 b) 채팅방에서 닉네임 변경
2. 실제 오픈카톡방처럼 닉네임이 변경됨

return 최종관리자가 보는 메시지

[전체 프로세스]
1. 문자열 파싱
2. Enter, Leave, Change 따라서 처리한다.
 2-1. [Enter] 딕셔너리 uid 참고 후 변경되었다면 변경, 리스트에 Enter, UID 집어넣기
 2-2. [Leave] 리스트에 Leave, UID 집어넣기
 2-3. [Change] 딕셔너리 uid 참고 후 변경
3. owner 리스트 참고하여 result 문구 지정

[프로세스별 수도코드]
owner = []
_dict = defaultdict(str)

<Enter>
cmd, uid, nick = split
if 사전에 유저가 존재하고 and 유저 닉네임 != 딕셔너리 닉네임:
    _dict[유저ID] = 새로운 닉네임
owner.append((uid, '님이 들어왔습니다.')

<Leave>
owener.append((uid, '님이 나갔습니다.'))

<change>
if 사전에 유저가 존재하면:
    _dict[유저ID] = 새로운 닉네임



[주석옮기기]


'''

from collections import defaultdict

# 궁금증 : 인자 2개, 3개 좀 더 간편히 파싱하는 방법?
cmd, uid, nick = '', '', ''


def solution(record):
    answer = []
    owner = []
    _dict = defaultdict(str)

    # 1. 문자열 파싱
    for r in record:
        tmp = r.split()
        cmd, uid = tmp[0], tmp[1]
        if len(tmp) == 3:
            nick = tmp[2]

        # 2. Enter, Leave, Change 따라서 처리한다.
        # 2-1. [Enter] 딕셔너리 uid 참고 후 변경되었다면 변경, 리스트에 Enter, UID 집어넣기
        if cmd == 'Enter':
            if (uid not in _dict) or (nick != _dict[uid]):
                _dict[uid] = nick
            owner.append((uid, '님이 들어왔습니다.'))

        # 2-2. [Leave] 리스트에 Leave, UID 집어넣기
        elif cmd == 'Leave':
            owner.append((uid, '님이 나갔습니다.'))


        # 2-3. [Change] 딕셔너리 uid 참고 후 변경
        else:
            if uid in _dict:
                _dict[uid] = nick

    # 3. owner 리스트 참고하여 result 문구 지정
    for own in owner:
        uid, ment = own
        answer.append(f'{_dict[uid]}' + ment)

    return answer
