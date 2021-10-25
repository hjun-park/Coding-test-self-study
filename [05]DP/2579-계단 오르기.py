import sys

'''
    2021-06-30
    [시작 체크 리스트]
    V       15분 지났으나 발상 불가 또는 아예 다른 길
            코드 50% 정도 완성
            30분 보다 더 걸려서 코드 완성
            코드는 다 돌아가는데 효율성에서 걸림
            코드 완성

    [완료 후 체크 리스트]
            아예 모르겠음
            중간 정도 이해함
      V     완벽히 이해함

    [첨언]
      - 발상은 같았으나 코드 구현에 의심을 했기 때문에 문제를 못 풂
      - 일반적으로 아래서부터 생각하겠지만 도착해서 뒤를 바라보는 식으로 생각한다.

'''

'''
    - https://daimhada.tistory.com/181
    [접근] d[n] : n칸까지 접근했을 때 얻을 수 있는 최댓값
     - 직전 칸에서 올라오는 경우의 최대값과 전전 칸에서 올라오는 경우 최댓값 생각   
     - 식을 표현하면 아래와 같다.
        d[n] = max(직전칸을 밟은 최댓값, 전전칸을 밟은 최댓값)
    
     - 점화식
        d[n] = max(stair[n] + stair[n-1] + d[n-3],
                    stair[n] + d[n-2]) # 직전(-1), 전전(-2)
'''


def logic(n):
    d[0] = stairs[0]  # 계단 1칸은 방법 1가지
    d[1] = stairs[0] + stairs[1]  # 계단 2칸도 방법 1가지
    d[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])

    # 계단 4개부터는 반복문을 타면서 구함
    for i in range(3, n):
        d[i] = max(stairs[i] + stairs[i - 1] + d[i - 3],
                   stairs[i] + d[i - 2])

    return d[n - 1]


n = int(input())
d = [0] * 300
stairs = [0] * 300

for i in range(n):
    stairs[i] = (int(input().strip()))

print(logic(n))
