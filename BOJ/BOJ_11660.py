# BOJ_11660
# 구간 합 구하기 5

import sys


def solution():
    def coord_sum(x_1, y_1, x_2, y_2):
        return table[x_2][y_2] - table[x_2][y_1 - 1] - table[x_1 - 1][y_2] + table[x_1 - 1][y_1 - 1]

    n, m = map(int, sys.stdin.readline().split())
    table = list()

    table.append([0 for _ in range(n + 1)])
    for _ in range(n):
        table.append([0] + list(map(int, sys.stdin.readline().split())))

    for j in range(n + 1):
        for i in range(2, n + 1):
            table[j][i] += table[j][i - 1]
    for j in range(2, n + 1):
        for i in range(n + 1):
            table[j][i] += table[j - 1][i]

    for _ in range(m):
        a, b, c, d = map(int, sys.stdin.readline().split())
        print(coord_sum(a, b, c, d))


if __name__ == "__main__":
<<<<<<< HEAD
    solution()
=======
    solution()
>>>>>>> 5ae11d8804eca0ee95680c2228111cdb04fcc3ac
