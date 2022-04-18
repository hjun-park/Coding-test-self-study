def solution(s):
    if s.count('p') + s.count('P') == s.count('y') + s.count('Y'):  # lower로 써도 됨
        return True
    else:
        return False
