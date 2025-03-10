# 충돌위험_찾기


def move(start, end, start_time, is_new):
    if is_new:
        tmp_key = tuple(start + [start_time])
        if tmp_key in vis:
            vis[tmp_key] += 1
        else:
            vis[tmp_key] = 1

    while start[0] != end[0]:
        if start[0] < end[0]:
            start[0] += 1
        elif start[0] > end[0]:
            start[0] -= 1
        start_time += 1

        tmp_key = tuple(start + [start_time])
        if tmp_key in vis:
            vis[tmp_key] += 1
        else:
            vis[tmp_key] = 1

    while start[1] != end[1]:
        if start[1] < end[1]:
            start[1] += 1
        elif start[1] > end[1]:
            start[1] -= 1
        start_time += 1

        tmp_key = tuple(start + [start_time])
        if tmp_key in vis:
            vis[tmp_key] += 1
        else:
            vis[tmp_key] = 1

    return start_time


def solution(points, routes):
    global vis

    vis = {}

    for el in routes:
        start_time = 0
        for i in range(len(el) - 1):
            start_time = move(
                points[el[i] - 1][:],
                points[el[i + 1] - 1][:],
                start_time,
                True if i == 0 else False,
            )

    res = 0
    for v in vis.values():
        if v > 1:
            res += 1

    return res
