# BOJ_1343
# 폴리오미노

import sys


def solution():
    s = input()
    s = s + '.'
    out = list()
    idx = 0
    x_len = 0

    while idx < len(s):
        if s[idx] == '.':
            if x_len == 0:
                out.append(s[idx])
                idx += 1
            else:
                if x_len % 2 != 0:
                    print(-1)
                    sys.exit()
                else:
                    if x_len >= 4:
                        out.append("AAAA" * (x_len // 4))
                    if x_len % 4 == 2:
                        out.append("BB")
            x_len = 0
        else:
            idx += 1
            x_len += 1

    out.pop()
    for i in out:
        print(i, end='')


if __name__ == "__main__":
    solution()
