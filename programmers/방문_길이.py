# 방문_길이


def solution(dirs):
    x, y = 5, 5

    used = set()

    for d in dirs:
        nx, ny = x, y
        if d == "U":
            if x == 0:
                continue
            nx -= 1
        elif d == "D":
            if x == 10:
                continue
            nx += 1
        elif d == "R":
            if y == 10:
                continue
            ny += 1
        elif d == "L":
            if y == 0:
                continue
            ny -= 1

        if not ((x, y, nx, ny) in used or (nx, ny, x, y) in used):
            used.add((x, y, nx, ny))
        x, y = nx, ny

    return len(used)
