import sys

input = sys.stdin.readline

'''
    [Union-find 문제]
    1. 동일한 파티 참석한 사람들을 Union 
    2. Union 하려는 대상 중 사실을 알고 있는 사람이 있다면 해당 사람을 Parent
    3. 만약 두 대상이 모두 사실을 알고 있다면 연결하지 않음
    4. 각 파티에 필요한 정보를 돈다.
        4-1. 파티에 참여하는 사람 중 Parent가 사실을 알고 있는 사람 목록이라면 진실을 이야기 하는 것으로 간주
        
    [조금 더 자세히]
    https://ku-hug.tistory.com/148
    1. know_list와 party_list를 split set으로 입력 받음
    2. 파티를 돌면서 파티와 유니온 간 교집합이 있다면 know_list에 party와 union 한다.
     -> 그렇게 하면 파티에 사실을 아는 사람들과 모르는데 같은 파티에 있는 사람들이 합쳐져감
    3. 다시 한 번 파티를 돌면서 party와 know_list를 교집합한다.
     -> 만약 교집합 내용이 존재하면 파티에 참가하면 안 된다.
     -> 교집합 내용이 없다면 cnt += 1
    
'''

N, M = map(int, input().split())  # 사람, 파티 수
know_list = set(input().split()[1:])  # 진실 아는 사람 수와 번호들
parties = []

for _ in range(M):
    parties.append(set(input().split()[1:]))

# 파티를 순회하면서 같은 파티 내에서 진실을 아는 사람들이 진실을 퍼뜨림
'''
 [파티 여러개를 반복하는 건 이해하지만 왜 파티의 수만큼 또 추가로 돌아야하는가 ?]
 -> 5개의 파티가 있고 진실을 아는 사람이 A라고 치자
 -> 이 경우 5개의 파티 중 A가 참여한 파티가 있는지 확인하면 된다.
 
 -> 하지만 확인하던 중 A가 3번째 파티에 참가했는데 그 때 B 역시 진실을 알게 되었다 치자
 -> 이 경우 마찬가지로 B에 대해서도 5개 파티 중 B가 참여한 파티가 있느지 확인해야 한다.
 -> 따라서 최대로 보자면 매 파티마다 진실을 알게 되는 사람이 생기므로 파티 수만큼 또 돌아준 것이다. 
'''
for _ in range(M):
    for party in parties:
        if party & know_list:
            know_list = know_list.union(party)

cnt = 0
# 다시 파티를 순회하면서 지민이가 참가해도 되는 파티인지 확인
for party in parties:
    if party & know_list:
        continue
    else:
        cnt += 1

print(cnt)
