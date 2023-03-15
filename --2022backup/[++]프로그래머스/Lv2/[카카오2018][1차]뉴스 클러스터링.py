'''
1. 문제 빠르게 이해하기
[자카드 유사도]
 - J(A, B) = 교집합(A, B) // 합집합(A, B)
 - 단, 교집합 0일 경우 1로 대체
 - 다중집합일 경우
  - [교집합] A, B 같은 원소 중 최소로 선택
  - [합집합] A, B 같은 원소 중 최대로 선택
 - 문자열은 두 글자씩 쪼개서 만들기 
 - 단, 두 글자 모을 시 문자 이외가 들어오면 버린다.
 - 소문자는 대문자로 저장한다.
 - 결과는 65536 곱한 후 소수점 아래는 버린다.
'''

'''
2. 구현해야 할 함수
- make_set(_s) // 다중집합 반환 1개
- find_union(a, b) // 다중집합 대상으로 합집합 구하기
- find_intersection(a, b) // 다중집합 대상으로 교집합 구하기
'''

'''
4. 해결방법 고민하기
1) 자카드 구하기
 - 교집합과 합집합 개수 구하기
 - 다중교집합이라 일반 set 연산이 되지 않는다. 리스트로 진행

'''

'''
5. 수도 코드 작성하기
1) 다중집합 만들기
result = []
for i in range(1, len(문자열)-1):
    if not 문자열[i-1].isalpha() or not 문자열[i].isalpha():
        continue
    result.append(문자열[i-1] + 문자열[i])

    return result
        

2) 자카드 구하기
 2-1) 교집합 구하기 : 레퍼런스
 2-2) 합집합 구하기 : 레퍼런스
 _inter = find_intersection(a, b)
 _union = find_union(a, b)
 
 if _inter == 0:
    _inter = 1

 return int((_inter // _union) * 65536) 
 
'''


def make_set(_s):
    result = []
    for i in range(1, len(_s)):
        if not _s[i - 1].isalpha() or not _s[i].isalpha():
            continue
        result.append(_s[i - 1].upper() + _s[i].upper())

    return result


def find_union(str1, str2):
    a = str1.copy()
    b = str2.copy()

    a_temp = a.copy()  # 다 처리하면 차집합 A-B만 남게됨
    a_result = a.copy()  # 다 처리하면 A에 B-A요소가 들어가져서 A + B가 완성됨

    for i in b:
        if i not in a_temp:
            a_result.append(i)  # A에 B-A 차집합이 더해진 결과가 들어간다.
        else:
            a_temp.remove(i)  # 차집합 A-B만 남게 된다.

    return len(a_result)  # A + B


def find_intersection(str1, str2):
    a = str1.copy()
    b = str2.copy()

    result = []
    for i in b:
        if i in a:
            a.remove(i)
            result.append(i)

    return len(result)


def solution(str1, str2):
    # 다중집합 만들기
    str1 = make_set(str1)
    str2 = make_set(str2)

    # 교집합 구하기
    _inter = find_intersection(str1, str2)

    # 합집합 구하기
    _union = find_union(str1, str2)

    # 둘 다 0인 경우 (테케 5, 13)
    if _inter == 0 and _union == 0:
        temp = 1
    else:
        temp = _inter / _union

    return int(temp * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
print(solution(' abc', 'abbb'))
print(solution('A+C', 'DEF'))
print(solution('ABC', 'DEF'))
