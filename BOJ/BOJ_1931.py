# BOJ_1931
# 회의실 배정

import sys


def solution():
    n = int(sys.stdin.readline())
    meeting = []
    res = 0
    x_end = 0
    for _ in range(n):
        meeting.append(list(map(int, sys.stdin.readline().split())))
    meeting.sort(key=lambda x: (x[1], x[0]))

    for i in meeting:
        if i[0] >= x_end:
            res += 1
            x_end = i[1]
    print(res)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
