# 최소직사각형


def solution(sizes):
    max_w = 0
    max_h = 0

    for w, h in sizes:
        if w < h:
            w, h = h, w

        max_w = w if w > max_w else max_w
        max_h = h if h > max_h else max_h

    return max_w * max_h
