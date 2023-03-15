import sys

input = sys.stdin.readline


def solution(arr1, arr2):

    # zip : 두 그룹의 데이터를 묶어준다.( 즉, 두 리스트에 있는 값을 하나하나 엮어서 튜플로 만들어준다. )
    #   만약 두 그룹의 데이터 사이즈가 다르다면 더 많은 쪽에 있는 것이 연산에 버려지게 된다.
    #   zip(*) 을 이용하면 행과 열을 서로 바꾸어준다. ( B열에 접근하기 위해 행과 열을 바꾸어준 것 )
    return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*arr2)] for A_row in arr1]


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

