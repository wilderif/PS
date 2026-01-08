# BOJ_33560
# 수상한 어릿광대

import sys

inp = sys.stdin.readline


def main():
    n = int(inp())
    arr = list(map(int, inp().split()))
    res = [0, 0, 0, 0]

    def reset():
        nonlocal cur_point, cur_time, total_point, total_time
        if total_point < 35:
            pass
        elif total_point < 65:
            res[0] += 1
        elif total_point < 95:
            res[1] += 1
        elif total_point < 125:
            res[2] += 1
        else:
            res[3] += 1

        cur_point = 1
        cur_time = 4
        total_point = 0
        total_time = 0

    cur_point = 1
    cur_time = 4
    total_point = 0
    total_time = 0
    for el in arr:
        if total_time > 240:
            reset()

        if el == 1:
            reset()
            continue
        elif el == 2:
            if cur_point > 1:
                cur_point //= 2
            else:
                cur_time += 2
        elif el == 3:
            pass
        elif el == 4:
            total_time += 56
        elif el == 5:
            if cur_time > 1:
                cur_time -= 1
        elif el == 6:
            if cur_point < 32:
                cur_point *= 2

        total_point += cur_point
        total_time += cur_time

    for el in res:
        print(el)


if __name__ == "__main__":
    main()
