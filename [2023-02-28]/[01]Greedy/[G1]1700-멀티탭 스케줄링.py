import sys

input = sys.stdin.readline

'''
    참고: https://pacific-ocean.tistory.com/357
'''

'''
 1) 입력값, 그리고 K 개수만큼 플러그 생성
 2) K만큼 루프를 돌기 시작
 3) 또 K만큼 루프를 돌면서 같은 플러그가 이미 꽂힌 경우나 플러그 빈 자리가 있는 경우 플러그를 꽂아줌
 4) 플러그를 꽂았다면 continue, 아니라면 5)를 돈다.
 5) K만큼 루프를 돌기 시작한다.
 6) i+1번째 콘센트부터 끝까지 확인하여 plug[j]가 있는지 확인
 7) plug[j]가 없을수록 -> 뒤에 있을 수록 플러그를 가장 먼저 뽑아야 효율적이다.
 7) plug[j]가 해당 j값으로 플러그 뽑을 위치 변수 선언 후 뽑아줌
 8) 플러그 뽑은 count 증가
'''

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
plug = [0] * N

cnt = 0
for i in range(K):  # 가전제품 번호 루프
    isPlug = False
    for j in range(N):  # 플러그 루프
        if plug[j] == numbers[i] or plug[j] == 0:  # 플러그에 꽂힌게 없거나 같은게 꽂혀있으면
            plug[j] = numbers[i]  # 플러그를 꽂아준다.
            isPlug = True  # 플러그가 이미 꽂혀있다고 상태 업데이트
            break

    if isPlug:  # 플러그가 꽂힌 상태라면 아래 루프를 실행할 이유가 없으므로 continue
        continue

    else:  # 플러그에 꽂을 공간이 없거나 같은 꽂힌게 없는 경우
        find_index = 0
        plugged_here = 0
        for j in range(N):  # 플러그 루프를 돈다.
            try:
                if find_index < numbers[i + 1:].index(plug[j]):  # 이후에 사용하는 플러그인지 확인한다.
                    # 플러그에 꽂힌 번호 중에서 가전제품 맨 끝번호에 있는 것을 먼저 뽑는게 더 효율적이다.
                    find_index = numbers[i + 1:].index(plug[j])
                    plugged_here = j
            except ValueError:
                # 그렇지만 플러그에 꽂힌 번호(plug)가 가전제품 번호(numbers)에 없다면 그걸 가장 먼저 뽑는다.
                # 앞으로 사용할 일이 없기 때문이다.
                plugged_here = j
                break
        plug[plugged_here] = numbers[i]
        cnt += 1  # 플러그 뽑은 횟수
print(cnt)
