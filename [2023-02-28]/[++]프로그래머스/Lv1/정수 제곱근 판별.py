from math import sqrt

def solution(n):
    if int(sqrt(n)) != sqrt(n):
        return -1
    else:
        return (int(sqrt(n)) + 1)**2
