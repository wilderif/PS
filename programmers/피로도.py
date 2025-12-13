# 피로도


import itertools


def solution(k, dungeons):
    n = len(dungeons)

    def check(path):
        cur_k = k
        ret = 0

        for d in path:
            if dungeons[d][0] > cur_k:
                return ret
            cur_k -= dungeons[d][1]
            ret += 1

        return ret

    res = 0

    for path in itertools.permutations(range(n), n):
        res = max(res, check(path))

    return res
