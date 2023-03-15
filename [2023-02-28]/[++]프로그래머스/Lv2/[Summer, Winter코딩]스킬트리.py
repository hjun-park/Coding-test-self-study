def solution(skill, skill_trees):

    cnt = 0
    for tree in skill_trees:
        res = []
        for s in skill:
            try:
                res.append(tree.index(s))
            except:
                res.append(len(tree))
        if res == sorted(res):
            cnt += 1

    return cnt


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
