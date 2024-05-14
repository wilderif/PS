# BOJ_11508
# 2+1 세일

import sys


def solution():
    n = int(sys.stdin.readline())
    price_list = list()
    total = 0

    for _ in range(n):
        price_list.append(int(sys.stdin.readline()))

    price_list.sort(reverse=True)

    while price_list:
        total += price_list.pop(0)
        if not price_list:
            break
        total += price_list.pop(0)
        if not price_list:
            break
        del price_list[0]
    print(total)


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
