# BOJ_1764
# 듣보잡

import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    h_s = set()
    s_s = set()

    for _ in range(n):
        h_s.add(sys.stdin.readline().rstrip())
    for _ in range(m):
        s_s.add(sys.stdin.readline().rstrip())

    out = list(h_s.intersection(s_s))
    out.sort()

    print(len(out))
    for i in out:
        print(i)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
