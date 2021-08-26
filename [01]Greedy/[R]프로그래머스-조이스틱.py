'''
for 루프 시작
    0. 순방향 좌우 이동 시 이동거리
     - len(A) + 1

    1. 상하 이동에 따른 최솟값 선정
     - (1)순방향이동(a to z)
     - (2)역방향이동(z to a)
     - min((1), (2)) -> 이동 수에 반영

    2. next 값 지정
     - 만약 next가 'A'라면 A가 안 나올 때까지 next 값 지정, 이동
     - (1) 시작점 - A가 나오기 직전
     - (2) A가 나오기 직전 - 시작점
     - (3) 전체 길이 - next  ( A가 끝나는 지점부터 끝까지 )
    - (1) + (2) + (3) 과 0번 순서에 순방향 이동과 비교해서 최소 지정
'''

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 다음값 이동
        next = i + 1
        # next가 len(name)안에 있으면서 다음 문자가 A라면
        # 오른쪽으로 계속해서 이동 ( 좌우변환 없이 )
        while next < len(name) and name[next] == 'A':
            next += 1

        reverse_move = i + len(name) - next
        # 순방향 이동값과 역방향 이동값을 더한 것 중 최소를 구함
        min_move = min(min_move, i + reverse_move)
    answer += min_move
    return answer

print(solution('JEROEN'))
print(solution('JAN'))
print(solution('JBN'))
print(solution('AABA'))

#
# # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def solution(name):
#     count=0
#     alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     d={}
#     indexes=[]
#     current_idx=0
#     n=len(name)
#     for i in range(len(alpha)):
#         d[alpha[i]]=min(i,26-i)
#     print(d) # A부터 각 문자열까지의 최소 길이가 저장된 배열
#     for i in range(n):
#         num=d[name[i]] # 입력받은 각 문자 자리마다 거리를 num에 저장
#         count+=num  # 총 거리를 구하기 위해 더함
#         if num !=0 :  # 거리가 있으면
#             indexes.append(i)  # 인덱스 값 indexes에 추가 (A는 indexes에 추가 X)
#     while True:
#         if len(indexes)==0:
#             break
#         min_dist=99
#         min_idx=0
#         for it in indexes: # it는 name에서 A가 아닌 문자열의 인덱스 번호값
#             # 현재 자리에서
#             min_dist2=min(abs(it-current_idx),n-abs(it-current_idx))
#             if min_dist2 < min_dist:
#                 min_dist=min_dist2
#                 min_idx=it
#         count+=min_dist
#         indexes.remove(min_idx)
#         current_idx = min_idx
#
#     return count# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
