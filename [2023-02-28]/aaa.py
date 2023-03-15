import sys

input = sys.stdin.readline

camp = list(map(int, input().split()))
init_list = ['Soongsil', 'Korea', 'Hanyang']

camp_dict = {num: init_list[x] for x, num in enumerate(camp)}

print('OK' if sum(camp) >= 100 else camp_dict.get(min(camp_dict)))



import sys

input = sys.stdin.readline

S, K, H = list(map(int, input().split()))
Camp = S + K + H
Camp_2 = {S, K, H}

if Camp >= 100:
    print("OK")
elif Camp < 100:
    Camp_2 = {S: "Soongsil", K: "Korea", H: "Hanyang"}
    print(Camp_2.get(min(Camp_2)))
