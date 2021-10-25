# void checknode(node v)
# {
#     node u;
#     if (promising(v)) // 방문 노드의 하위 노드에 솔루션이 있을 것 같다면 탐색하고
#         if (v에 해답이 있으면)   // 지금 내가 답을 찾았다면
#             해답 출력;            // 해답을 출력
#         else      // 해답이 없다면
#             for(v의 모든 자식 노드 u에 대해서)   // 방문한 노드의 인접한 노드에 대해서
#                 checknode(u);         // 탐색
# }


# ======================================
# 백트래킹에서 부분집합
# ======================================
# 부분집합 기본코드
def printSet(n):
    for i in range(n):
        if A[i] == 1:
            print(data[i], end=" ")
    print()


def powerset(k, n):  # k는 A배열의 k인덱스의 포함 유무를 판별한다.
    if n == k:  # 개수가 맞을 때 로직 수행
        printSet(k)
    else:   # 아니라면 값을 추가하는 연산의 반복
        A[k] = 1
        powerset(k + 1, n)  # 배열 A에 체크하고 다음 인덱스로 넘어간다
        A[k] = 0  # 재귀로 되돌아와서 체크 했던걸 다시 원상복귀시킨다
        powerset(k + 1, n)

data = 구하려는 리스트
n = len(data)  # 부분집합을 구하는 리스트의 수
A = [0] * n  # 포함 유무를 체크할 리스트 (0이 미포함, 1이 포함)

# =====================================================

# 부분집합의 합
# def powerset(k, n, sum):
#     if sum > 10:  # 부분집합의 합을 구하는 문제에서 구하고자하는 값인 10을 넘는다면 더이상 계산할 필요가 없으므로 return해버린다.(가지치기)
#         return
#     if n == k:
#         printSet(k, sum)
#     else:
#         A[k] = 1
#         powerset(k + 1, n, sum + data[k])
#         A[k] = 0
#         powerset(k + 1, n, sum)
