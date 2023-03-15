'''
[문제이해]
- 캐시 크기에 따른 실행시간 측정 프로그램
- 도시 이름은 전부 소문자로 변경
- LRU 방식으로 구현

[전체 프로세스]   
1. 도시이름 순회 (stack)
2. 캐시에 있는지 확인 (list)
 2-1. 있으면 캐시힛
  2-1-1. 최근에 방문했다는 처리 필요 (pop(index) -> append)
 2-2. 없으면 캐시미스
  2-2-1. [캐시사이즈부족]  append
  2-2-2. [꽉참] 가장 늦게사용 뺌 (pop(0))
3. 종료

[수도코드/손코딩]
'''


def solution(cacheSize, cities):  # 캐시사이즈, 도시  ret 실행시간
    cache = []
    cnt = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        if city in cache:
            print(f'{city} --> 캐시 힛 : {cnt}')
            cache.append(cache.pop(cache.index(city)))
            cnt += 1
            continue

        if len(cache) >= cacheSize:
            print(f'{city} --> 캐시 미스(캐시사이즈 큼) : {cnt}')
            cache.pop(0)
            cache.append(city)
        else:
            print(f'{city} --> 캐시 미스(캐시사이즈 작음) : {cnt}')
            cache.append(city)
        cnt += 5

        print(f'캐시 상태 : {cache}, {cnt}')
        print()
    return cnt


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
