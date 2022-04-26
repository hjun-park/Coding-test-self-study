import math
import re


def solution(str1, str2):
    # 문자 s에서 문자가 아닌 것들을 제외하고 2글자인 s[i]+s[i+1]로 구성된 리스트 생성
    str1 = [str1[i:i + 2].lower() for i in range(0, len(str1) - 1) if not re.findall('[^a-zA-Z]+', str1[i:i + 2])]
    str2 = [str2[i:i + 2].lower() for i in range(0, len(str2) - 1) if not re.findall('[^a-zA-Z]+', str2[i:i + 2])]

    # 합집합과 교집합을 구함
    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    # 합집합이 0이라면 (0으로 나눌 수 없으니) return 65536
    if len(hap) == 0:
        return 65536

    # 교집합, 합집합 원소를 돈다.
    # # 교집합의 경우 두 문자열 중 가장 적게 나온 것들의 합
    # # 합집합의 경우 두 문자열 중 가장 많이 나온 것들의 합
    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])
    # print(gyo, gyo_sum)
    # print(hap, hap_sum)


    return math.floor((gyo_sum / hap_sum) * 65536)


print(solution("FRANCE", "french"))
