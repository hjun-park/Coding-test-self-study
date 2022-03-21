import math

'''
    참고: https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A4%84-%EC%84%9C%EB%8A%94-%EB%B0%A9%EB%B2%95-%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C-level3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%98%ED%95%99

    0) 결과를 저장할 리스트 answer를 선언한다.
    1) k와 (n-1)! 를 구한다. 0번째 자리에 있는 수가 바뀌려면 (n-1)! 가짓수가 필요하다.
    2) divmod(k, (n-1)!) 를 한다. 몫, 나머지가 split 되어 나온다.
    3) 나머지는 다시 k에 집어넣고 몫은 numbers에서 몫을 빼내서 answer에 집어넣는다.
     -> 몫은 (n-1)! 가짓수를 몇 개 뛰어넘었는지 알려주는 수,
     -> numbers에서 해당 index를 pop해서 answer에 append 한다.
'''


def solution(n, k):
    numbers = [x for x in range(1, n + 1)]
    answer = []
    k -= 1  # k는 1을 기준으로 하기 때문

    count = 0
    # while n > 0:  # while문을 for문으로 바꾸었는데 효율성 통과한 이유는 ?
    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i - 1))
        answer.append(numbers.pop(div))
        count += 1
        # n -= 1 # https://www.quora.com/Which-is-faster-for-or-while-loop-in-Python
        # while문은 n -= 1 하는 연산의 과정이 있기 때문에 느리다.

    return answer

