# 기지국_설치


def solution(n, stations, w):
    interval = []
    cur_end = 0
    for s in stations:
        start, end = s - w, s + w
        if start - cur_end - 1 > 0:
            interval.append(start - cur_end - 1)

        cur_end = end
    if n - cur_end > 0:
        interval.append(n - cur_end)

    res = 0
    for i in interval:
        q, r = divmod(i, w * 2 + 1)
        res += q if r == 0 else q + 1

    return res
