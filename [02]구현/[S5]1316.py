# 그룹 단어 체커
import sys

result = 0
for i in range(int(input())):   # input : 3(number of word)
    word = input()  # words

    # word.find는 아래처럼 정렬이 된다.
    # happy == happy
    # ababa == aaabb
    if list(word) == sorted(word, key=word.find):
        result += 1

print(result)

