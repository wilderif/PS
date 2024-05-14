# BOJ_7576
# 토마토

import sys


def solution():
    m, n = map(int, input().split())
    storage = list()
    count = 0
    change_check = True
    point_to_change = list()
    point_to_change_next = list()

    storage.append(list(-1 for _ in range(m + 2)))
    for _ in range(n):
        storage.append([-1] + list(map(int, input().split())) + [-1])
    storage.append(list(-1 for _ in range(m + 2)))

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if storage[j][i] == 1:
                point_to_change.append([j, i])

    while change_check is True:
        change_check = False

        for p in point_to_change:
            if storage[p[0] - 1][p[1]] == 0:
                storage[p[0] - 1][p[1]] = 1
                point_to_change_next.append([p[0] - 1, p[1]])
                change_check = True
            if storage[p[0] + 1][p[1]] == 0:
                storage[p[0] + 1][p[1]] = 1
                point_to_change_next.append([p[0] + 1, p[1]])
                change_check = True
            if storage[p[0]][p[1] - 1] == 0:
                storage[p[0]][p[1] - 1] = 1
                point_to_change_next.append([p[0], p[1] - 1])
                change_check = True
            if storage[p[0]][p[1] + 1] == 0:
                storage[p[0]][p[1] + 1] = 1
                point_to_change_next.append([p[0], p[1] + 1])
                change_check = True
        point_to_change = point_to_change_next
        point_to_change_next = list()

        if change_check is True:
            count += 1

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if storage[j][i] == 0:
                print(-1)
                sys.exit()
    else:
        print(count)


if __name__ == "__main__":
    solution()