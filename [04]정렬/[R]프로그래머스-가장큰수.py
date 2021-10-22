def solution(numbers):
    answer = ''

    # 1) numbers를 문자열 형태로 변환
    # 2) x*3 기준으로 정렬(문자열 3번 곱은 3번 여러번 출력의 의미)
    '''
    2-1)
        x * 3 -> 문자열에 3을 곱해주면 해당문자열을 3개 나열하는 것과 같으니 '333', '303030', '343434', '555', '999'를 key로 넣어주면. 정렬을 하면 303030 -> 333 -> 343434 -> 555 -> 999가 될 것인데 reverse에 의해 거꾸로 정렬된 결과 출력
    '''
    # 3) join을 이용하여 list -> string

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # [0, 0, 0, 0]이 들어오는 경우 0000이 된다. 0을 반환해야 하기 때문에 int로 한 번 변환한다. 그리고 리턴은 str을 요구하므로 다시 또 변환 필요
    return str(int(''.join(numbers)))
