import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())

    wear_dict = {}
    for _ in range(n):
        name, type = input().split()

        if type in wear_dict:
            wear_dict[type] += 1
        else:
            wear_dict[type] = 1

    # (특정 옷 개수 + 1) * (특정 옷 개수 + 1) ... - 1 (-1은 아무것도 입지 않는 경우)
    # 첫 번째 예제의 경우 3*2-1 = 5
    count = 1
    for key in wear_dict.keys():
        count = count * (wear_dict[key] + 1)

    print(count - 1)
