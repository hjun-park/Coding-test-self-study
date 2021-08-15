import sys

sl = list(sys.stdin.readline().rstrip())

index = 0
start = 0

# 단어 범위를 넘어가는 순간 종료
while index < len(sl):
    if sl[index] == "<":     #열린 괄호로 시작해서
        index += 1
        while sl[index] != ">":  #닫힌 괄호를 만날 때까지 순회
            index += 1
        index += 1

    # 숫자나 알파벳을 만나면
    elif sl[index].isalnum():
        start = index
        # 알파벳이고 숫자라면
        while index < len(sl) and sl[index].isalnum():
            index += 1

        # while문을 안 타는 경우는 "<", ">"을 만난 경우

        tmp = sl[start:index]
        tmp.reverse()
        sl[start:index] = tmp
    else:
        index += 1

print("".join(sl))




