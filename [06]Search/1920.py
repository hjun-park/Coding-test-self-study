import sys

'''
    이진탐색은 정렬을 하고 써야한다.
    해당 문제 이해하기가 제일 어려웠음
'''

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    n_num_list = list(map(int, sys.stdin.readline().rstrip().split()))
    M = int(sys.stdin.readline().rstrip())
    m_num_list = list(map(int, sys.stdin.readline().rstrip().split()))

    n_num_list.sort()
    # m_num_list.sort()

    for num in m_num_list:
        # print(binary_search(n_num_list, num, 0, N - 1))
        if binary_search(n_num_list, num, 0, N - 1) is not None:
            print("1")
        else:
            print("0")
