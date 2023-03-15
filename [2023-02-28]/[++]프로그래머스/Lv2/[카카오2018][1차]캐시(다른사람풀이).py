
'''
# deque에 maxlen을 지정한 풀이
  - append, appendleft를 이용하여 추가 시 maxlen을 초과하면 밀려서 들어가게 된다.
  - 자세한 내용은 아래 예제 참고
  - 이렇게 풀게 되면 리스트의 길이 체크 없이 짧은 코드 작성이 가능하다.

        from queue import deque
        dq = deque((1,2,3), 3)
        print(dq)
        >>> deque([1, 2, 3], maxlen=3)

        dq.append(4)
        print(dq)
        >>> deque([2, 3, 4], maxlen=3)

        dq.appendleft(5)
        print(dq)
        >>> deque([5, 2, 3], maxlen=3)


'''
def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
