# BOJ_17143
# 뱀

import sys

inp = sys.stdin.readline


def main():
    def move():
        nonlocal sharks
        new_sharks = {}
        for (x, y), (s, d, z) in sharks.items():
            nx, ny = x, y

            nx, ny, nd = find_new_pos(x, y, d, s)

            key = (nx, ny)
            if key not in new_sharks or new_sharks[key][2] < z:
                new_sharks[key] = (s, nd, z)
        sharks = new_sharks

    def catch(col):
        for x in range(r):
            key = (x, col)
            if key in sharks:
                ret = sharks[key][2]
                del sharks[key]
                return ret
        return 0

    def find_new_pos(x, y, d, s):
        nx, ny = x, y
        nd = -1
        if d == 0 or d == 1:
            cycle = (r - 1) * 2
            nx = x if d == 1 else cycle - x
            nx = (nx + s) % cycle
            if nx < r:
                nd = 1
            else:
                nd = 0
                nx = cycle - nx
        else:
            cycle = (c - 1) * 2
            ny = y if d == 2 else cycle - y
            ny = (ny + s) % cycle
            if ny < c:
                nd = 2
            else:
                nd = 3
                ny = cycle - ny

        return nx, ny, nd

    r, c, m = map(int, inp().split())
    sharks = {}
    for _ in range(m):
        x, y, s, d, z = map(int, inp().split())
        if d == 1 or d == 2:
            s %= (r - 1) * 2
        if d == 3 or d == 4:
            s %= (c - 1) * 2
        sharks[(x - 1, y - 1)] = (s, d - 1, z)

    res = 0
    for i in range(c):
        res += catch(i)
        move()

    print(res)


if __name__ == "__main__":
    main()
