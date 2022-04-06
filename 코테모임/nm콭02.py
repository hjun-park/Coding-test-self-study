import sys

input = sys.stdin.readline

'''
    [요약]
    1. n개의 상품을 k개 상자에 포장
    2. 상품의 크기 <= 상자의 크기, 단 1개만
    3. 최대한 많은 상품을 상자에 담아 보관 하려고 함
'''


def solution(goods, boxes):
    # 1) 둘 다 정렬
    # 2) goods를 boxes 처음 요소와 비교
    # 2-0) 만약 gi나 bi가 goods 길이나 boxes 길이와 같다면 return cnt
    # 2-1) 담을 수 있다면 gi와 bi를 1씩 증가, 카운트 증가
    # 2-2) 담을 수 없다면 bi만 증가

    goods = sorted(goods)
    boxes = sorted(boxes)

    gi, bi = 0, 0
    _len_g = len(goods)
    _len_b = len(boxes)

    cnt = 0
    while True:
        if gi >= _len_g or bi >= _len_b:
            return cnt

        if goods[gi] <= boxes[bi]:
            gi += 1
            bi += 1
            cnt += 1
        else:
            bi += 1


print(solution([5, 3, 7], [3, 7, 6]))
print(solution([1, 2], [2, 3, 1]))
print(solution([3, 8, 6], [5, 6, 4]))
print(solution([1, 1, 1], [1]))
print(solution([2, 5, 3, 8, 7, 7, 7], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
