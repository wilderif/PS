# 보석_쇼핑


def solution(gems):
    gem_kind = len(set(gems))

    res = [0, len(gems)]
    gem_dict = {}
    start = 0
    end = 0
    while end < len(gems):
        gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
        end += 1

        while len(gem_dict) == gem_kind:
            if end - start < res[1] - res[0]:
                res = [start, end]
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                gem_dict.pop(gems[start])
            start += 1

    return [res[0] + 1, res[1]]
