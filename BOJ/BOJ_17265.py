# BOJ_17265
# 나의 인생에는 수학과 함께

import sys


def solution():
    def operate(x, y, o):
        if o == '+':
            return int(x) + int(y)
        elif o == '-':
            return int(x) - int(y)
        elif o == '*':
            return int(x) * int(y)

    n = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(list(sys.stdin.readline().split()))

    mem_1 = [[0 for _ in range(n)] for _ in range(n)]
    mem_2 = [[0 for _ in range(n)] for _ in range(n)]
    mem_1[0][0] = int(arr[0][0])
    mem_2[0][0] = int(arr[0][0])

    for i in range(2, n, 2):
        mem_1[0][i] = operate(mem_1[0][i - 2], arr[0][i], arr[0][i - 1])
        mem_2[0][i] = operate(mem_2[0][i - 2], arr[0][i], arr[0][i - 1])

    for i in range(2, n, 2):
        mem_1[i][0] = operate(mem_1[i - 2][0], arr[i][0], arr[i - 1][0])
        mem_2[i][0] = operate(mem_2[i - 2][0], arr[i][0], arr[i - 1][0])

    for j in range(1, n):
        for i in range(1, n):
            if j == 1 and i == 1:
                mem_1[j][i] = max(
                    operate(mem_1[j - 1][i - 1], arr[j][i], arr[j][i - 1]),
                    operate(mem_1[j - 1][i - 1], arr[j][i], arr[j - 1][i]))
                mem_2[j][i] = min(
                    operate(mem_2[j - 1][i - 1], arr[j][i], arr[j][i - 1]),
                    operate(mem_2[j - 1][i - 1], arr[j][i], arr[j - 1][i]))
            elif arr[j][i].isdigit() and j == 1:
                mem_1[j][i] = max(
                    operate(max(int(mem_1[j - 1][i - 1]), int(mem_1[j][i - 2])), arr[j][i], arr[j][i - 1]),
                    operate(mem_1[j - 1][i - 1], arr[j][i], arr[j - 1][i]))
                mem_2[j][i] = min(
                    operate(min(int(mem_2[j - 1][i - 1]), int(mem_2[j][i - 2])), arr[j][i], arr[j][i - 1]),
                    operate(mem_2[j - 1][i - 1], arr[j][i], arr[j - 1][i]))
            elif arr[j][i].isdigit() and i == 1:
                mem_1[j][i] = max(
                    operate(mem_1[j - 1][i - 1], arr[j][i], arr[j][i - 1]),
                    operate(max(int(mem_1[j - 1][i - 1]), int(mem_1[j - 2][i])), arr[j][i], arr[j - 1][i]))
                mem_2[j][i] = min(
                    operate(mem_2[j - 1][i - 1], arr[j][i], arr[j][i - 1]),
                    operate(min(int(mem_2[j - 1][i - 1]), int(mem_2[j - 2][i])), arr[j][i], arr[j - 1][i]))
            elif arr[j][i].isdigit():
                mem_1[j][i] = max(
                    operate(max(int(mem_1[j - 1][i - 1]), int(mem_1[j][i - 2])), arr[j][i], arr[j][i - 1]),
                    operate(max(int(mem_1[j - 1][i - 1]), int(mem_1[j - 2][i])), arr[j][i], arr[j - 1][i]))
                mem_2[j][i] = min(
                    operate(min(int(mem_2[j - 1][i - 1]), int(mem_2[j][i - 2])), arr[j][i], arr[j][i - 1]),
                    operate(min(int(mem_2[j - 1][i - 1]), int(mem_2[j - 2][i])), arr[j][i], arr[j - 1][i]))

    print(mem_1[n - 1][n - 1], end=' ')
    print(mem_2[n - 1][n - 1])


if __name__ == "__main__":
    solution()
