import re


def solution(new_id):
    answer = ''

    answer = new_id.lower()
    answer = re.sub('[^a-z\d\-\_\.]', '', answer)  # [^] 의미는 '제외' 뜻임
    answer = re.sub('\.\.+', '', answer)
    answer = re.sub('^\.|\.$', '', answer)

    print(answer)

    if answer == '':
        answer = 'a'

    print(answer)

    # 6단계 : 길이가 16자 이상이면 1~15자만 남기기 & 맨 끝 마침표 제거
    answer = re.sub('\.$', '', answer[0:15])

    print(answer)

    while len(answer) <= 2:
        answer += answer[-1]

    print(answer)
    return answer
