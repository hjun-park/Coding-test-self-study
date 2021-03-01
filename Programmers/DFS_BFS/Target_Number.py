def solution(numbers, target):
    answer = 0
    size = len(numbers)

    def dfs(index, _sum):
        print('index1 : ', index)
        if index >= size:         # 만약 인덱스가 size보다 크거나 같으면 모두 계산한 상태
            print('out of index')
            if _sum == target:    # 계산 결과랑 타겟과 같다면 정답값 +1
                nonlocal answer   # scope 영역 밖의 answer 사용
                answer += 1
            return  # 재귀 종료조건

        else:
            print('index2 : ', index)
            # 아니라면 재귀 이용 dfs(다음 인덱스, 계산 결과에 현재 인덱스 값을 더한 값)
            dfs(index + 1, _sum + numbers[index])  # index 1을 더한 이유는 윗 if문에서 index range 체크 위해
            print('run')
            dfs(index + 1, _sum - numbers[index])

    # 초기 함수 실행
    dfs(0, 0)
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1], 1))
