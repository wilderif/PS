# BOJ_16598
# Achievements

import sys

inp = sys.stdin.readline


def main():
    n, p = map(int, inp().split())
    arr = list(map(int, inp().split()))
    day_set = set(arr)
    remain = p
    cur_max = 0
    right = 0
    for i in range(0, arr[-1] + 1):
        while remain or right in day_set:
            if right not in day_set:
                remain -= 1
            right += 1
        cur_max = max(cur_max, right - i)
        if i not in day_set:
            remain += 1

    print(cur_max)


if __name__ == "__main__":
    main()
