import sys

input = sys.stdin.readline

'''
 특징 [ 도형문제는 대부분 diff 이용 ]
 1) 사각형을 좌표에 그리고 (겹쳤을 때, 선분일치, 점일치, 떨어질 때 ) 
   - 아래 있는 사각형의 (p, q)와 위 사각형의 (x, y)에 의해 4가지 경우가 구분됨

 2) 그럼 아래있는 사각형과 위 사각형 어떻게 구분 ?
    => 빼서, 그렇게 해서 두 사각형이 서로 만나려고 하는 두 점 x, y, p, q를 구한다.  
   
'''
#

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 2) 두 사각형이 서로 만나려고 하는 주어진 점을 구한다.
    x = x1 if x1 >= x2 else x2
    p = p1 if p1 <= p2 else p2

    y = y1 if y1 >= y2 else y2
    q = q1 if q1 <= q2 else q2

    # 3) x < p, y < q임에 유념하고 p,q 에서 x,y를 빼야한다.
    if p - x > 0 and q - y > 0:  # 빼도 값이 남으면 사각형을 형성한 경우
        print('a')
    elif p - x == 0 and q - y == 0:
        print('c')
    elif p - x < 0 or q - y < 0:  #
        print('d')
    else:
        print('b')
