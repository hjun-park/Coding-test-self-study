import re


def solution(files):
    # 1) 대소문자 구분 없이 HEAD 기준 정렬 --> x[0].lower()
    # 2) NUMBER 숫자 순으로 정렬 --> re.findall (더 좋은방법은 re.split)
    # 3) 이외에는 원래 주어진 순서를 유지 --> (정렬하고 그대로 두면 된다)

    answer = [re.split(r"([0-9]+)", f) for f in files]  # 찾아보니 나온 더 쉬운 방법
    s = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(x) for x in s]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
