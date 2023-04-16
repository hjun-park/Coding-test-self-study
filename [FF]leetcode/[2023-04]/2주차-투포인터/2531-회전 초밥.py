import sys
from collections import defaultdict

input = sys.stdin.readline

'''
    [문제핵심]
    1) 원형의 회전 초밥이므로 리스트를 extends로 하나 더 붙임
    2) sliding window 사용
    3) 같은 번호의 초밥이 여러 개 있더라도 가짓 수는 결국 하나
        3-1) 따라서 dictionary 사용
    
    [첫 번째 풀이]
    1) set과 count 사용 -> 시간초과
    
    [두 번째 풀이] - 참고: https://wooono.tistory.com/654
    1) dictionary 이용, 모든 구간에는 항상 쿠폰이 포함 되어 있다고 가정
'''

# N : 회전 초밥 벨트에 놓인 접시의 수
# d : 초밥의 가짓수
# k : 연속해서 먹는 접시의 수
# c : 쿠폰 번호
N, d, k, c = map(int, input().split())

# 1. 초밥 번호가 적인 배열
s = [int(input().rstrip()) for _ in range(N)]

# 2. 원형의 회전초밥이므로 한 번 더 이어 붙임
s.extend(s)

# 3. sliding window를 진행할 투포인터 지정
left, right = 0, k - 1

# 4. 먹을 수 있는 초밥 최대 가짓 수
_max = -1

# 5. 초밥의 개수가 아닌 가짓 수를 말하는 것이므로 dictionary 사용
_dict = defaultdict(int)

# 6. 모든 구간에는 항상 쿠폰 번호가 포함 된다.
_dict[c] += 1

# 7. 첫 구간은 직접 계산 (sliding window size 계산)
for i in range(k):
    _dict[s[i]] += 1

# 8. `left`가 맨 끝 닿을 때까지 진행
while left < N:
    # 1. 구간 내 최대 초밥 가짓 수 갱신
    _max = max(_max, len(_dict))

    # 2. [sliding window] 현재 구간 내 가장 왼쪽 접시 제거
    _dict[s[left]] -= 1
    # 3. 만약 접시 개수가 0개 이하라면 딕셔너리에서 자체 제거
    if _dict[s[left]] <= 0:
        del _dict[s[left]]

    # 4. 왼쪽과 오른쪽을 동시에 이동
    left += 1
    right += 1

    # 5. 오른쪽이 이동 되었으니, 이동한 현재 구간 내 가장 오른쪽 접시 추가
    _dict[s[right]] += 1

print(_max)
