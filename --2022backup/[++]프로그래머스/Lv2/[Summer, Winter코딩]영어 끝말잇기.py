from collections import defaultdict


def solution(n, words):
    result = [0, 0]
    word_dict = defaultdict(list)

    before = words[0]
    word_dict[0].append(before)

    for i in range(1, len(words)):
        nxt = words[i]

        # 룰을 벗어난 경우
        if before[-1] != nxt[0] or nxt in word_dict[0]:
            result[0] = (i % n) + 1  # 탈락자 번호
            result[1] = (i // n) + 1  # 자신의 차례 번호
            return result

        # 룰을 지킨 경우
        word_dict[0].append(nxt)
        before = nxt

    # 4 % 2 == (0+1) // 탈락자 번호
    # 4 // 2 == (2+1) // 자신의 차례번호
    # [탈락자 번호, 자신의 몇 번째 차례]
    return result


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,
               ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
                "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
