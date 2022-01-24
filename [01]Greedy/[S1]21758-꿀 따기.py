import sys

input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))
s = []
max_sum = 0

# -> 누적합은 계산의 편의성을 위해 0번 배열을 하나 추가하고 누적합을 구해준다.
s.append(honey[0])

# 누적합을 구한다.
for i in range(1, n):
    s.append(s[i - 1] + honey[i])

print(f'누적합 s = {s}')

'''
    누적합 문제, https://ojt90902.tistory.com/577
    -> 누적합만 계산하면 아래 3가지 경우를 loop 돌면서 계산 가능
  
    # 경우 3가지
     1) 꿀통 < 벌벌 (벌통이 왼쪽에 있는 경우) 
     2) 벌 > 꿀통 < 벌 (벌통이 두 벌 사이에 있는 경우)
     3) 벌벌 < 꿀통 (벌통이 오른쪽 끝에 있는 경우)
'''

# 벌은 가장 맨 끝에 있는게 유리하다는 전제 하에 누적합을 실행한다.

# 벌 벌 꿀 ( 3 )
for i in range(1, n - 1):
    # 맨 끝 꿀통까지 누적합 - 벌1 - 벌2(위치매번바뀜) + 맨 끝 꿀통까지 누적합 - 맨 끝 꿀통 누적합 - 벌2 위치까지의 누적합
    # 벌1, 벌2 빼준 이유는 벌 시작점은 꿀 합에 집계되지 않음 ( -honey[0] - honey[i] )
    # 이후 더 하고 빼주는 이유는 벌1은 벌2가 갔던 길을 또 가기 때문(s[n-1] - s[i])
    max_sum = max(max_sum, s[n - 1] - honey[0] - honey[i] + s[n - 1] - s[i])

# 꿀 벌 벌 ( 1 )
for i in range(1, n - 1):
    # 위와 비슷함. 누적합에 벌1, 벌2 위치를 빼주고 벌2가 벌 1 지나가므로 한 번 더 더해준다.
    max_sum = max(max_sum, s[n - 1] - honey[n - 1] - honey[i] + s[i - 1])

# 벌 벌 꿀 ( 2 )
for i in range(1, n - 1):
    # 누적합 - 벌1 - 벌2 + 꿀통 위치 (honey[i])
    # (1), (3)의 경우 꿀벌이 이동했지만, (2)의 경우 벌은 양쪽에 있다고 가정하고 꿀통 위치를 바꿔준다.
    max_sum = max(max_sum, s[n - 1] - honey[0] - honey[n - 1] + honey[i])

print(max_sum)
