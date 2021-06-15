import sys

# 집합 자료형으로 생성
natural_num = set(range(1, 10001))
generated_num = set()

# 1부터 10000까지 루프를 돌면서
# 문자열로 변환하여 각 자리를 더하여 저장함
# set 자료형이기 때문에 중복된 값이 들어가도 유니크하게 유지됨
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)    # 추가

# 1부터 10000이 모여 있는 natural_num 에서 generated_num을 뺀 차집합을 구하면
# 결국 생성자가 없는 self num이 구해지게 된다.
# 이걸 출력하면 됨
self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)
