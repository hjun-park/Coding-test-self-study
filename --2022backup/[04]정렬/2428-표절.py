import sys

input = sys.stdin.readline

N = int(input().rstrip())
size = list(map(int, input().split()))

count = 0

size.sort()


'''
https://dndi117.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2428%EB%B2%88-%ED%91%9C%EC%A0%88-%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89-%ED%92%80%EC%9D%B4
 정렬된 리스트가 만약 [a,b,c,d,e]라고 한다면,
 a와 b,c,d,e를 비교하고 b와 c,d,e를, c와 d,e를, d와 e를 비교해야 한다
 
 그래서 for문을 돌리는 것이고,
 for문을 돌려서 하나하나 비교하려면 이중 for문이 필요하다. 이 경우는 시간초과난다.
 
 대신에 이진탐색을 이용해서 for문 index 하나하나마다 이진탐색을 수행한다. 
 거기서 파일사이즈가 90% 내로 들어오는 구간의 개수를 구해주는 것이다 (end값이 최대 index값)

'''
for i in range(N):
    start = i
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        # 인덱스를 쭉 바꿔가면서 파일사이즈가 90% 내로 들어오는 인덱스를 찾아감
        if size[i] >= 0.9 * size[mid]:
            start = mid + 1
        else:   # 최종적 end가 a >= b * 0.9 를 만족하는 요소의 최대 인덱스가 들어감
            end = mid - 1

    # 최종적으로 남는 쌍의 개수 end - i
    # 90%에 달하는 최대 index(end) - 90% 영역에 들어가지 않는 이미 계산된 index들(i)
    print(f'end = {end}, i = {i}')
    count += end - i if end > -1 else 0
    print(f'count = {count}')

print(count)
