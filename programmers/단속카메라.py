# 단속카메라


def solution(routes):
    routes.sort(key=lambda x: x[1])
    cur_end = -30001
    res = 0
    for s, e in routes:
        if s > cur_end:
            res += 1
            cur_end = e

    return res
