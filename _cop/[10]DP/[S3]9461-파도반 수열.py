import sys

input = sys.stdin.readline

T = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(T)]

d = [0] * (max(nums) + 2)

'''
P(9) = P(8) + P(4)
P(10) = P(9) + P(5)
P(11) = P(10) + P(6)
P(i) = P(i-1) + P(i-5) 
'''


def logic():
    d[1] = 1
    d[2] = 1
    d[3] = 1
    d[4] = 2
    d[5] = 2

    for i in range(5, max(nums) + 1):
        d[i] = d[i - 1] + d[i - 5]


logic()

for n in nums:
    print(d[n])
