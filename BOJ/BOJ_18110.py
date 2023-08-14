# BOJ_18110
# solved.ac

import sys
import math


def solution():
    n = int(sys.stdin.readline())
    e = math.trunc(n * 3 / 10 / 2 + 0.5)
    sum_for_average = 0
    numbers = list()

    for _ in range(n):
        numbers.append(int(sys.stdin.readline()))
    numbers.sort()

    if e != 0:
        del numbers[:e]
        del numbers[-e:]

    for i in range(len(numbers)):
        sum_for_average += numbers[i]

    if len(numbers) == 0:
        print(0)
    else:
        print(math.trunc(sum_for_average / len(numbers) + 0.5))


if __name__ == "__main__":
    solution()
