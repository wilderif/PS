# 스킬트리


def solution(skill, skill_trees):
    skill_set = set(skill)

    def check(skill, skill_tree):
        skill = list(reversed(skill))
        for s in skill_tree:
            if s not in skill_set:
                continue
            if s != skill[-1]:
                return False
            skill.pop()

        return True

    res = 0
    for st in skill_trees:
        if check(skill, st):
            res += 1

    return res
