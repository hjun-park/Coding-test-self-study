import sys

'''
    clothes: [의상 이름, 의상 종류]
'''


def solution(clothes):
    cloths = {}
    answer = 1  # 아예 안 입을 때 음수가 나오므로 1부터 시작

    # 옷의 종류를 키 값으로 두고
    # 옷의 이름을 value로 분류하는 작업
    for name, kind in clothes:
        if kind in cloths:
            cloths[kind] += 1
        else:
            cloths[kind] = 1

    # 모든 경우의 수를 구합 (선택조합)
    for key, value in cloths.items():   # 키를 기준으로 순환
        answer *= (value + 1)

    return answer - 1  # 모두 안입는 경우 빼기

'''
    [ A ] [ B ] [ C ] [ D] [A C ] [ A D ] [ A C D ] [B C ] [ B D ] [ B C D ] [ C D ]
    총 11개가 있다. 이 11이라는 값은 3 x 2 x 2 - 1로 구할 수 있다.
    
    즉 ! "X 개의 의상의 종류1 이 있고, Y개의 의상의 종류2 가 있고, Z개의 의상의 종류3" 이 있다고 가정했을 때
    나올 수 있는 모든 조합의 수는 (X + 1) * (Y + 1) * (Z + 1) - 1 이다.
'''

# (HEADGEAR + 1) * (eyewear + 1) - 1
# 여기서 +1은 선택하지 않는 경우의 수 ( 최소 1개의 의상은 입음 )

clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
