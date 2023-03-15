import sys
from itertools import permutations

input = sys.stdin.readline

'''
참고 : htps://dreamtreeits.tistory.com/44?category=1225887
set으로 풀이: https://kjy042386.tistory.com/42

1) 어떻게 어떤 생각으로 문제를 접근하여 어떤 아이디어를 냈는가 ?
2) 특별히 어느 부분이 구현이 힘들었고 그건 어떻게 구현을 하였는가 ? 
3) 나는 어떤 부분이 어려웠고 무엇을 배웠는가 ?

- 내 생각
우선, 제한사항에서 볼 때 완전탐색 문제라는 것을 알았다.
그러나 고려할 사항이 정말 많았고 결국 해결하지는 못했다. (원을 리스트로 생각했으나 그 이후 연산이 어려웠다.)
완전탐색 문제에서는 permutation을 사용하면 좀 더 수월해질 것이다.

==> 순서
1) 원형인 경우 길이를 2배로 해서 일자로 구성한다, len(weak)을 2배 늘리면 된다.
2) 투입할 친구의 최솟값을 찾기 위해 dist 최대 길이보다 +1 더 큰 값으로 초기화한다. (answer = len(dist) + 1)
3) 취약한 부분을 순회 하면서 그 안에는 순열로 친구 여려명 투입해서 점검한다.
4) 그렇게 해서 answer를 반환하되, answer가 친구 수보다 많으면 -1 반환

==> 배운 점
1) 배열 길이가 크지 않고, 모든 경우의 수를 따져보아야 하는 경우 itertools.permutation을 통해 확인하면 쉽게 알 수 있다.

 
'''


def solution(n, weak, dist):
    length = len(weak)

    # 1) weak 배열을 2배 길게 늘린다. 그렇게 되면 방향을 고려할 필요가 없게 된다.
    # 즉, 12m 원형 외벽에서 4m부터 9m까지 반시계방향으로 도는 것 == 9m부터 12+4m = 16m 시계 방향과 같다.
    for i in range(length):
        weak.append(weak[i] + n)  # n을 더하는 이유는 weak는 외벽 위치가 적혀있고, 상대값이기 때문이다.

    # 2) 투입할 친구의 최솟값,친구 수 + 1 로 초기화
    min_friend = len(dist) + 1

    # 3) 외벽 취약점을 하나하나 start를 이동하면서 찾는다.
    # 아래 코드 순서
    #  - 취약한 부분 개수만큼 순회 (첫번째 케이스는 4개 )
    #  - 친구 전체에 대해 모든 순열을 만들고 처음 친구의 취약점 점검 가능한 범위 설정
    #  - 만약에 그 친구가 모든 취약점을 확인 가능하다면 (if not position < weak[i]) 최솟값을 1로 업데이트 할 것이다.
    #  - 만약에 그 친구가 모든 취약점 탐색이 불가능하다면 다음 친구를 투입하여
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            friend_count = 1  # 투입할 친구 수

            # 현재 친구가 확인할 수 있는 최대 거리
            # position에는 취약점 시작지 + 해당 친구가 볼 수 있는 거리
            position = weak[start] + friends[friend_count - 1]

            # 시작점부터 모든 취약지점까지 확인
            for i in range(start, start + length):
                if position < weak[i]:  # 확인할 수 있는 최대 거리를 넘었다면
                    friend_count += 1  # 다음 친구 투입

                    # 더 이상 투입할 친구가 없다면 다음 친구로 탐색하기 위해 빠져나온다.
                    if friend_count > len(dist):
                        break

                    # 친구가 확인할 수 있는 최대 거리를 업데이트 한다.
                    # 만약 처음 친구는 position이 weak[i]보다 작았지만
                    # 어떤 친구가 모든 weak[i]값을 커버 가능한다면
                    # if position < weak[i] 내 코드를 순환하지 않으므로 최솟값이 나오게 된다.
                    # https://kom-story.tistory.com/191
                    position = weak[i] + friends[friend_count - 1]

            # 투입할 친구의 최솟값을 업데이트
            min_friend = min(min_friend, friend_count)

    if min_friend > len(dist):
        return -1
    return min_friend


# def solution(n, weak, dist):
#     answer = 1
#
#     # 외벽에 취약한 부분 설정
#     n_list = [0] * n
#
#     for w in weak:
#         n_list[w] = 1
#
#     dist.sort(reverse=True)
#     print('========================================')
#     print(f'친구: {dist}')
#     print(f'취약점:{weak}')
#
#     # 계산
#     for d in dist:
#         is_reverse_wise = False
#         start = 0
#         max_count = -1  # 가장 많은 값을 커버하는 것
#
#         for w in weak:
#             print(f'n_list: {n_list}')
#             print(f'친구 : {d}, 취약점 : {w}')
#             print(f'시계 방향 : {n_list[w:w + d + 1]}')
#             # print(f'반시계 방향 : {n_list[w:w - d - 1:-1]}')
#             print(f'반시계 방향 : {n_list[0:w + 1], n_list[w-d-1:]}')
#             clockwise = n_list[w:w + d + 1].count(1)
#             # counter_clockwise = n_list[w:w - d - 1].count(1)    # 어떻게 반대방향으로 리스트 범위를 지정하지
#             counter_clockwise = (n_list[0:w + 1] + n_list[w - d - 1:]).count(1)  # 어떻게 반대방향으로 리스트 범위를 지정하지
#
#             print(f'시계 1 개수: {clockwise}')
#             print(f'반시계 1 개수: {counter_clockwise}')
#
#             # 시계방향으로 돌 때 더 많은 값을 커버 가능한 경우
#             if clockwise > counter_clockwise:
#                 if max_count <= clockwise:
#                     max_count = clockwise
#                     start = w
#                     is_reverse_wise = False
#             # 반시계 방향으로 돌 때 더 많은 값을 커버 가능한 경우
#             else:
#                 if max_count <= counter_clockwise:
#                     max_count = counter_clockwise
#                     start = w
#                     is_reverse_wise = True
#
#             # 전체 커버 가능하면 answer 출력하고 종료
#             if max_count == n_list.count(1):
#                 print(f'친구 {d}가 {n_list.count(1)} 만큼 커버 가능하므로 종료')
#                 return answer
#
#         # 취약 리스트를 한 번 순회하였으면 그 시작점과 방향을 가지고 n_list 취약점 제거
#         # 어떻게 리스트를 0으로 초기화 하지
#         if not is_reverse_wise:
#             # n_list[start:start+d+1] = 0
#             for i in range(start, start+d+1):
#                 n_list[i] = 0
#
#         else:
#             for i in range(0, start+d+1):
#                 n_list[i] = 0
#
#             for i in range(start - d - 1, len(n_list)):
#                 n_list[i] = 0
#             # n_list[0:start + 1] = 0
#             # n_list[start - d - 1:] = 0
#
#         # 다음 친구를 불러야 하니 += 1
#         answer += 1
#
#     return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
