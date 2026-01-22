# BOJ_17039
# Sleepy Cow Herding (Bronze)

import sys

inp = sys.stdin.readline


def main():
    arr = list(map(int, inp().split()))
    dist_1, dist_2 = arr[1] - arr[0], arr[2] - arr[1]
    dist_1, dist_2 = min(dist_1, dist_2), max(dist_1, dist_2)
    res_min, res_max = 0, 0
    if dist_1 == 1 and dist_2 == 1:
        res_min = 0
    elif dist_1 == 2 or dist_2 == 2:
        res_min = 1
    else:
        res_min = 2

    res_max = dist_2 - 1

    print(res_min)
    print(res_max)


if __name__ == "__main__":
    main()
