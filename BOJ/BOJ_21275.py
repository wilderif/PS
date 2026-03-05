# BOJ_21275
# 폰 호석만

import sys

inp = sys.stdin.readline


def main():
    char_to_num = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15,
        "g": 16,
        "h": 17,
        "i": 18,
        "j": 19,
        "k": 20,
        "l": 21,
        "m": 22,
        "n": 23,
        "o": 24,
        "p": 25,
        "q": 26,
        "r": 27,
        "s": 28,
        "t": 29,
        "u": 30,
        "v": 31,
        "w": 32,
        "x": 33,
        "y": 34,
        "z": 35,
    }

    LIMIT = 2**63
    num1, num2 = inp().split()
    start1 = max(2, max(char_to_num[x] for x in num1) + 1)
    start2 = max(2, max(char_to_num[x] for x in num2) + 1)

    a_dict = {}
    b_dict = {}

    for a in range(start1, 37):
        tmp1 = 0
        for x in num1:
            tmp1 = tmp1 * a + char_to_num[x]
        if not (tmp1 < LIMIT):
            continue
        a_dict[a] = tmp1

    for b in range(start2, 37):
        tmp2 = 0
        for x in num2:
            tmp2 = tmp2 * b + char_to_num[x]
        if not (tmp2 < LIMIT):
            continue
        b_dict[b] = tmp2

    res = [0, 0, 0]
    for a in a_dict:
        for b in b_dict:
            if a == b:
                continue
            if a_dict[a] == b_dict[b]:
                if res[1]:
                    print("Multiple")
                    return
                res[0] = a_dict[a]
                res[1] = a
                res[2] = b

    if res[1]:
        print(*res)
        return
    print("Impossible")


if __name__ == "__main__":
    main()
