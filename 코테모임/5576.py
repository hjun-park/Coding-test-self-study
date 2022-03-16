import sys

input = sys.stdin.readline

score = [int(input().rstrip()) for _ in range(20)]

'''
 W대학 => score[0:10]  -> score[:10]
 K대학 => score[10:19]  -> score[10:]
'''
# W대학의 상위 3개 스코어
w_score = sum(sorted(score[:10], reverse=True)[:3])
# K대학의 상위 3개 스코어
k_score = sum(sorted(score[10:], reverse=True)[:3])

print(w_score, k_score)


