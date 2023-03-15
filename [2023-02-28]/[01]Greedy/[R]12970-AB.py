import sys

input = sys.stdin.readline

# AB => (i, j)쌍 만족
# BA => (i, j)쌍 만족 X


'''
    참고 : https://rccode.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-12970%EB%B2%88-AB?category=1186954?category=1186954
    구현 2가지
    1) A를 앞으로 미는 경우
    2) 민 자리에 A가 있는지 체크하여 A로 바꾸는 작업
    
    예시
    3 2 라고 하면 B*3 생성
    BBB - K = 0
    BBA - K = 0
    BAB - K = 1
    ABB - K = 2 정답
'''


def get_string(N, K):
    current_string = ['B'] * N
    a_cnt = 0
    current_k = 0
    last_a_idx = -1

    while current_k < K:
        # 1) A를 추가하는 경우
        if last_a_idx <= a_cnt - 1:
            # 더 이상 추가할 것이 없는 경우
            if current_string[N - 1 - (a_cnt + 1)] == 'A':
                break
            # 해당 자리에 A 추가
            else:
                current_string[N - 1 - (a_cnt + 1)] = 'A'
                last_a_idx = N - 1 - (a_cnt + 1)
                a_cnt += 1  # a개수 증가
                current_k += 1  # 현재 K 증가
        # 2) A를 앞으로 밀어내는 경우
        else:
            current_string[last_a_idx] = 'B'
            current_string[last_a_idx - 1] = 'A'
            last_a_idx -= 1
            current_k += 1  # 현재 K 증가

    if current_k == K:
        return current_string
    else:
        return "-1"


N, K = map(int, input().split())
print(''.join(get_string(N, K)))
