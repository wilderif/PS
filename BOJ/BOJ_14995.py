# BOJ_14995
# Horror Film Night

import sys

inp = sys.stdin.readline


def main():
    set_1 = set(list(map(int, inp().split()))[1:])
    set_2 = set(list(map(int, inp().split()))[1:])
    total_idx = sorted(list(set_1 | set_2))

    res = 0
    flag_1 = True
    flag_2 = True
    for i in total_idx:
        if i in set_1:
            if i in set_2:
                res += 1
                flag_1 = True
                flag_2 = True
            else:
                if flag_2:
                    res += 1
                    flag_1 = True
                    flag_2 = False
        else:
            if i in set_2:
                if flag_1:
                    res += 1
                    flag_1 = False
                    flag_2 = True

    print(res)


if __name__ == "__main__":
    main()
