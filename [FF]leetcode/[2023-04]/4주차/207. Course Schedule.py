from collections import defaultdict, deque
from typing import List

class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 3. 위상정렬 시작
        def topo_sort():
            result = []  # 위상정렬 결과

            # 1. 위상정렬용 큐 생성
            q = deque()

            # 2. 노드 개수만큼 돌면서 indegree가 0인 경우만 q에 담는다.
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)

            # 3. q 순회 시작
            while q:
                now = q.popleft()

                # 1. 가장 먼저 방문한 노드는 결과에 포함
                result.append(now)

                # 2. 현재 꺼낸 노드가 갈 수 있는 모든 방향을 순회
                for v in graph[now]:
                    # 1. 간선을 제거 (간선 제거되면 차수 감소)
                    indegree[v] -= 1

                    # 2. 간선 제거했는데 차수가 0이라면 q에 추가
                    if indegree[v] == 0:
                        q.append(v)

            # 4. q가 다 끝나면 위상 정렬 완료된 상태
            print(result)

            # 5. 위상 정렬 결과에 노드가 전부 없다면 해당 그래프는 사이클이 존재하는 상태
            # 사이클 존재 = 해당 강의 전부 들을 수 없다.
            return len(result) == numCourses

        indegree = [0] * (numCourses + 1)  # 차수
        graph = defaultdict(list)  # 그래프

        # 1. 과목 edges 순회
        for a, b in prerequisites:
            # 1. b를 들어야 a를 들을 수 있다.
            graph[b].append(a)

            # 2. b -> a로 들어가므로 a의 indegree 증가
            indegree[a] += 1

        # 2. 위상 정렬 시작
        return topo_sort()


s = Solution()
print(s.canFinish(2, [[1, 0]]))  # true
print(s.canFinish(2, [[1, 0], [0, 1]]))  # false
print(s.canFinish(4, [[3, 2], [1, 0]]))  # true
print(s.canFinish(4, [[3, 1], [0, 2]]))  # true
print(s.canFinish(1, []))  # true
print(s.canFinish(2, [[1, 0]]))  # true


'''
문제 핵심
1. 사이클이 있다면 해당 강의 전부 들을 수 없다.
2. 사이클이 없어야만 돌 수 있는 위상정렬을 이용한다.
'''
