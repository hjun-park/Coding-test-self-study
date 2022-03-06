import sys

input = sys.stdin.readline

pp = [int(input().rstrip()) for _ in range(20)]
print(sum(sorted(pp[:10], reverse=True)[:3]), sum(sorted(pp[10:], reverse=True)[:3]))
