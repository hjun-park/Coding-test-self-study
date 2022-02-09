import sys

input = sys.stdin.readline

'''
 1) 함수의 정의
  int func(int n, int r, int c)
   - 2^n x 2^n 배열에서 (r,c)를 방문하는 순서를 반환하는 함수
   
 2) base condition
  - n = 0 일 때 return 0;
  --> n = 1도 가능하지만 재귀식에서 추가처리가 필요하다.
  
 3) 재귀식
  - (r, c)가 어디 사각형에 있는지 따라서 식이 달라진다.
  - 여기서 half는 한 변 길이의 절반 즉 2^(n-1) 이다.
  3-1) (r, c)가 1번 사각형일 때 return func(n-1, r, c);
  3-2) (r, c)가 2번 사각형일 때 return half * half + func(n-1, r, c-half);
  3-3) (r, c)가 3번 사각형일 때 return 2 * half * half + func(n-1, r-half, c);
  3-4) (r, c)가 4번 사각형일 때 return 3 * half * half + func(n-1, r-half, c-half);
'''


# 재귀적으로 생각했을 때
# 1) 함수의 정의
def func(n, r, c):
    # 2) base condition
    if n == 0:
        return 0

    # 3) 재귀 식
    half = 1 << (n - 1)  # 2^(n-1)과 같다.

    # 3-1) 1번 사각형 영역에 있다면
    if r < half and c < half:
        return func(n - 1, r, c)

    # 3-2) 2번 사각형 영역에 있다면
    if r < half <= c:
        # (n-1, r, c-half) => n-1 배열로 좁히고 여기선 2번 사각형인데,
        # 2번 사각형에서 r은 사각형 사이즈가 줄어도 영향 없지만
        # c의 경우 사각형 사이즈가 줄어들면 범위초과가 뜰 것이므로 c - half, 줄어든 길이만큼 뺀다.
        return half * half + func(n - 1, r, c - half)

    # 3-3) 3번 사각형 영역에 있다면
    if r < half and c < half:
        # half * 2 * half => 1, 2번 사각형을 넘기 위해 가로세로를 곱함
        return half * 2 * half + func(n - 1, r - half, c)

    # 3-4) 4번 사각형 영역에 있다면
    return 3 * half * half + func(n - 1, r - half, c - half)


N, R, C = map(int, input().split())

print(func(N, R, C))
