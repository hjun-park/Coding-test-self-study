import sys
from collections import deque


'''
문제의 제약 사항
1) 보트는 2명씩 탈 수 있다.
2) 무게제한 'limit'가 있다.
3) 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 한다. (탐욕법)
사람들의 무게를 오름차순으로 정렬한다.

사람들의 리스트를 deque형식으로 만들어 무게가 제일 많이 나가는 사람을 고른뒤 제일 가벼운 사람과 더해서 limit 이하인지 확인다.

만약 무게가 limit 이하라면 앞에 하나, 뒤에 하나 pop하고 두 사람을 보트에 태운다는 의미에서 boat를 하나 증가시킨다.

그래도 만약 앞 뒤 사람의 합이 limit를 초과한다면 보트에
 둘이 담을 수 없기에 제일 무게가 많이 나가는 사람을 pop 한다.
 (탐욕:무거운 사람을 태워야 남은 가벼운 사람들이 보트에 2명씩 타서 보트 수를 줄일 
 가능성이 높아지기 때문이다.) 보트는 당연히 하나 더 증가.
'''


def solution(people, limit):
    # minimize value
    # 1. sorting
    # 2. 최대 + 최소 < 100
    # 3. A + B / 2 < 50
    result = 0
    # 오름차순으로 정렬한다.
    people.sort()
    people = deque(people)

    # 무게가 가장 큰 사람과 작은 사람 추출 -> 합 구하기
    while people:
        if len(people) < 2:
            result += 1
            break

        biggest = people[-1]
        less = people[0]
        sum = biggest + less

        # limit 이하 확인
        if sum <= limit:
            people.pop()
            people.popleft()
            result += 1
        else:
            people.pop()
            result += 1
        # limit 이하라면 양옆으로 pop 후에 result += 1

    return result


people = [70, 50, 50,  80]
limit = 100
print(solution(people, limit))
